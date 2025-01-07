from fastapi import FastAPI
from pydantic import BaseModel
from random import randint
import asyncio
import database
import login

# old backend
import old_backend

app = FastAPI()

class Message(BaseModel):
    jwt: str
    messagecontent: str
    fromuser: bool

class User(BaseModel):
    username: str
    password: str

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
    #message_response = await transform(messagecontent)
    message_response = await old_backend.transform(messagecontent)
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

async def transform(message):
    # simulating time taken for the AI to respond
    await asyncio.sleep(1)
    return f'{randint(1000, 9999)} {message}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)