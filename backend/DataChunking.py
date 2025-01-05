# import libraries for document processing, embeddings, database operations and file handling
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
import openai
import os
import re
import shutil
import chromadb
from dotenv import load_dotenv

# load environment variables for secure configuration
load_dotenv()

# set up configuration variables from environment
CHROMA_PATH = os.getenv("CHROMA_PATH")
DATA_PATH = os.getenv("DATA_PATH")
openai.api_key = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

def main():
    persistent_client = chromadb.PersistentClient(CHROMA_PATH)
    try:
        db = persistent_client.get_collection("documents")
        print("db already initialized")
    except:
        db = Chroma(
            collection_name="documents",
            embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL),
            persist_directory=CHROMA_PATH,
        )
        print("Initialized new Chroma database.")
        # Step 1: Read and chunk the text file
        chunks = clean_and_chunk_file(DATA_PATH, chunk_size=512)
        print("1")
        # Step 2: Preprocess the chunks, filtering out any empty or invalid chunks
        cleaned_chunks = [preprocess_chunk(chunk) for chunk in chunks]
        print("2")  
        # Filter out any chunks that became None or empty after preprocessing
        cleaned_chunks = [chunk for chunk in cleaned_chunks if chunk]
        print("3")
        cleaned_chunks = remove_duplicates(cleaned_chunks)
        print("4")
        documents = [Document(page_content=chunk) for chunk in cleaned_chunks]
        print("converted)")
        # Create embeddings and initialize the database
        db.add_documents(documents=documents)
        print(f"Initializing new database at {CHROMA_PATH}.")

# Your existing chunking function
def read_and_chunk_file(file_path, chunk_size=512):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
    
    # Split text into chunks based on paragraphs separated by double line breaks
    chunks = text.split("\n\n")  # Assumes paragraphs are separated by double line breaks
    
    return chunks

# Function to clean non-text characters and format issues
def clean_text(text):
    # Remove non-printable characters except for newlines and carriage returns
    cleaned_text = ''.join(char for char in text if char.isprintable() or char in ['\n', '\r'])
    # Optionally remove HTML tags
    cleaned_text = re.sub(r'<.*?>', '', cleaned_text)
    return cleaned_text.strip()

# Function to split a chunk into smaller sub-chunks if it exceeds the chunk size
def chunk_text(text, chunk_size=512):
    words = text.split()  # Split the text into words
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    return [' '.join(chunk) for chunk in chunks]

# Main function to read, clean, preprocess, and chunk the file
def clean_and_chunk_file(file_path, chunk_size=512):
    # Step 1: Read and split file into initial chunks
    chunks = read_and_chunk_file(file_path, chunk_size)
    
    # Step 2: Clean each chunk and preprocess, filter out invalid chunks
    i = 0  # Use index to iterate safely when popping
    while i < len(chunks):
        chunk = chunks[i]
        processed_chunk = preprocess_chunk(clean_text(chunk))
        
        # If the processed chunk is None (empty), remove it from the list
        if processed_chunk is None:
            chunks.pop(i)  # Remove the invalid chunk
        else:
            chunks[i] = processed_chunk  # Update with the cleaned chunk
            i += 1  # Only move to the next chunk if the current one is valid

    # Step 3: Further chunk large cleaned chunks if needed
    all_chunks = []
    for chunk in chunks:
        if len(chunk.split()) > chunk_size:
            # If the chunk is too large, break it into smaller sub-chunks
            sub_chunks = chunk_text(chunk, chunk_size)
            all_chunks.extend(sub_chunks)
        else:
            all_chunks.append(chunk)
    
    return all_chunks

# Updated preprocess_chunk to avoid empty chunks
def preprocess_chunk(chunk):
    # Remove non-alphabetic characters (except spaces)
    cleaned_chunk = re.sub(r'[^a-zA-Z\s]', '', chunk)
    
    # Ensure the chunk is not empty or just whitespace
    cleaned_chunk = cleaned_chunk.strip()
    
    # Return the chunk if it's not empty; otherwise, return None
    if cleaned_chunk:
        return cleaned_chunk
    else:
        return None  # Return None if the chunk is empty

def get_embeddings(text_chunks):
    embeddings = []
    ids = []
    for chunk in text_chunks:
        print(text_chunks.index(chunk))
        response = openai.embeddings.create(
            input = [chunk],
            model="text-embedding-3-small").data[0].embedding
        embeddings.append(response)
        ids.append(str(text_chunks.index(chunk)))
    return embeddings, ids

def remove_duplicates(chunks):
    seen = set()  # Set to track seen chunks
    unique_chunks = []  # List to store unique chunks
    
    for chunk in chunks:
        if chunk not in seen:  # Check if the chunk has been encountered before
            unique_chunks.append(chunk)  # Add it to the unique list
            seen.add(chunk)  # Mark it as seen
            
    return unique_chunks

# Function to insert data into the Chroma database
def insert_data_into_db(split_chunks, db):
    print("converting....")
    # Wrap each chunk in a Document object
    documents = [Document(page_content=chunk) for chunk in split_chunks]
    print("converted")
    # Add documents to the database
    db.add_documents(documents=documents)
    print(f"Added {len(documents)} chunks to the database.")

def create_db2(split_chunks):
    # remove existing database if present
    db_exists = os.path.exists(CHROMA_PATH)

    print("converting....")
    # Wrap each chunk in a Document object
    documents = [Document(page_content=chunk) for chunk in split_chunks]
    print("converted)")
    # Create embeddings and initialize the database
    db = Chroma.from_documents(
        documents=documents,
        embedding=OpenAIEmbeddings(model=EMBEDDING_MODEL),
        persist_directory=CHROMA_PATH,
    )
    print(f"Added {len(documents)} chunks to the database.")

# script entry point
if __name__ == "__main__":
    main()