from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import JSONResponse
import json
import aiofiles
from pydantic import BaseModel
from random import randint
import asyncio
from database import add_message
import database
import login
import os
from werkzeug.utils import secure_filename
from fastapi.middleware.cors import CORSMiddleware


# old backend
import backendChat
import backendClassification
from TextExtraction import get_pdf_text, get_docx_text, get_pptx_text, get_xlsx_text, get_file_text
#from DataChunking import clean_and_chunk_file, preprocess_chunk, remove_duplicates, insert_data_into_db, read_and_chunk_file
from DataChunking import main as DataChunking_main
from DataChunking import db, insert_data_into_db, chunk_text

DATA_PATH = os.getenv("DATA_PATH", "./modelling/extracted_text.txt")
PUBLIC_FRONTEND_URL = os.getenv("PUBLIC_FRONTEND_URL", "http://localhost:4173")
UPLOAD_FOLDER = 'uploads'

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[PUBLIC_FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
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
    print("wahaha")
    return {"message": "ok i pull up hop out at the afterparty"}

@app.get("/get_messages/")
async def get_messages(request: Request):
    accesstoken = request.headers['Authorization']
    messages = database.get_messages(accesstoken)
    return messages

@app.post("/add_message/")
async def add_message(request: Request, message: Message):
    accesstoken = request.headers['Authorization']
    messagecontent, fromuser = message.messagecontent, message.fromuser
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
        return {"success":False, "error":True, "message": f"File upload error: {str(e)}"}
        #raise HTTPException(status_code=500, error=True, detail=f'File upload error: {str(e)}')
    finally:
        file.file.close()
    
    return {"success": True, "message": f"Successfully uploaded {file.filename}"}

@app.post("/classify/")
async def classify(file: UploadFile = File(...)):
    try:
        print("reading file")
        contents = await file.read()
        extension = file.filename.split(".")[1]
        if extension not in ['pdf', 'docx', 'pptx', 'xlsx']:
            raise Exception(detail="Filetype not allowed")
        
        # set upload directory and create if it doesn't exist
        directory = os.path.join('uploads', 'classify', f'{extension}_files')
        os.makedirs(directory, exist_ok=True)

        print(f'retrieved file {file.filename} with extension {extension}')
        file_path = os.path.join(directory, file.filename)
        print(file_path)

        # Write file asynchronously
        async with aiofiles.open(file_path, 'wb') as f:
            await f.write(contents)

        # extract text
        file_text = get_file_text(extension, file_path)

        # If uploaded file very large, prevent overusing token by truncating middle
        # 80,000 characters = 20,000 tokens
        print("the length of this file is: " + str(len(file_text)))
        if len(file_text) > 80000:
            print("file too large, truncating text")
            file_text = file_text[:40000] + file_text[-40000:]
        print("classifying text")
        message_response = await backendClassification.classify_text(file_text)
        print(f"{message_response['answer'] = }")
        # Remove code block markers from the response string
        json_str = message_response['answer'].strip('``[json').strip('](http://_vscodecontentref_/1)``').strip()

        answer_json = json.loads(json_str)
        print("answer converted to json")
        # Extract classification and reasoning from the response
        classification = answer_json['classification']
        reasoning = answer_json['reasoning']

        # Return the classification and reasoning in the response
        return JSONResponse(content={
            "success": True,
            "classification": classification,
            "reasoning": reasoning,
        })
    
    except Exception as e:
        return {"success":False, "error":True, "message": f"File upload error: {str(e)}"}
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
    