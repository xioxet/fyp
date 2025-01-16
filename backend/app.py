from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from random import randint
import asyncio
from database import add_message
import database
import login
import os
from werkzeug.utils import secure_filename

# old backend
import backendChat
import backendClassification
from TextExtraction import get_pdf_text, get_docx_text, get_pptx_text, get_xlsx_text, get_file_text
#from DataChunking import clean_and_chunk_file, preprocess_chunk, remove_duplicates, insert_data_into_db, read_and_chunk_file
from DataChunking import main as DataChunking_main
from DataChunking import db, insert_data_into_db, chunk_text

DATA_PATH = os.getenv("DATA_PATH", "./modelling/extracted_text.txt")
UPLOAD_FOLDER = 'uploads'

app = FastAPI()

class Message(BaseModel):
    jwt: str
    messagecontent: str
    fromuser: bool

class User(BaseModel):
    username: str
    password: str

ALLOWED_EXTENSIONS = {'docx', 'pdf', 'pptx', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Helper function to extract text based on file type
def extract_text(filepath, file_type):
    try:
        if file_type == 'pdf':
            return get_pdf_text([filepath])
        elif file_type == 'docx':
            return get_docx_text([filepath])
        elif file_type == 'xlsx':
            return get_xlsx_text([filepath])
        elif file_type == 'pptx':
            return get_pptx_text([filepath])
    except Exception as e:
        raise
    return ""

@app.get("/")
async def index():
    return {"message": "ok i pull up hop out at the afterparty"}

@app.get("/get_messages/{accesstoken}/")
async def get_messages(accesstoken: str):
    messages = database.get_messages(accesstoken)
    return messages

@app.post("/add_message/")
async def add_message(message: Message):
    accesstoken, messagecontent, fromuser = message.jwt, message.messagecontent, message.fromuser
    database.add_message(accesstoken, messagecontent, fromuser)
    print(messagecontent)
    print(f'successfully added message')
    #message_response = await transform(messagecontent)
    message_response = await backendChat.transform(messagecontent)
    print(f"{message_response['answer'] = }")
    message = message_response['answer']
    database.add_message(accesstoken, message, False)
    return database.get_messages(accesstoken)

@app.post("/reset_chat/")
async def reset_chat():
    return database.reset_chat()
     
# account system

@app.post("/register/")
async def register(user: User):
    return database.add_user(user.username, user.password)

@app.get("/get_users/")
async def get_users():
    return database.get_users()

@app.post("/login/")
async def login(user: User):
    return database.verify_login(user.username, user.password)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        extension = file.filename.split(".")[1]
        if extension not in ['pdf', 'docx', 'pptx', 'xlsx']:
            raise Exception(detail="Filetype not allowed")
        # set upload directory and create if it doesn't exist
        directory = os.path.join('uploads', 'data', f'{extension}_files')
        os.makedirs(directory, exist_ok=True)

        print(f'retrieved file {file.filename} with extension {extension}')
        file_path = os.path.join(directory, file.filename)
        print(file_path)

        with open(file_path, 'wb') as f:
            f.write(contents)
            f.close()

        # temporarily add new stuff to database
        file_text = get_file_text(extension, file_path)
        print(file_text)
        chunks = chunk_text(file_text)
        print(chunks)
        insert_data_into_db(chunks, db)
        # ???

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'File upload error: {str(e)}')
    finally:
        file.file.close()
    
    return {"message": f"Successfully uploaded {file.filename}"}

@app.post("/classify/")
async def classify(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        extension = file.filename.split(".")[1]
        if extension not in ['pdf', 'docx', 'pptx', 'xlsx']:
            raise Exception(detail="Filetype not allowed")
        
        # set upload directory and create if it doesn't exist
        directory = os.path.join('uploads', 'classify', f'{extension}_files')
        os.makedirs(directory, exist_ok=True)

        print(f'retrieved file {file.filename} with extension {extension}')
        file_path = os.path.join(directory, file.filename)
        print(file_path)

        with open(file_path, 'wb') as f:
            f.write(contents)
            f.close()

        # temporarily add new stuff to database
        file_text = get_file_text(extension, file_path)
        print("classifying text")
        message_response = await backendClassification.classify_text(file_text)
        print(f"{message_response['answer'] = }")

        # Return the classification and summary in the response
        return JSONResponse(content={
            "success": True,
            "classification": message_response['answer'],
        })
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'File upload error: {str(e)}')
    finally:
        file.file.close()


async def transform(message):
    # simulating time taken for the AI to respond
    await asyncio.sleep(1)
    return f'{randint(1000, 9999)} {message}'

# Checks if vector database is empty and if so, populates it. 
DataChunking_main()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
    