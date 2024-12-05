from fastapi import FastAPI
from pydantic import BaseModel
from random import randint

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "ok i pull up hop out at the afterparty"}

class Message(BaseModel):
    message: str

@app.post('/process_message/')
async def process_message(message: Message):
    messagecontent = message.message
    return {"message": transform(messagecontent)}

# should take in a string and output a string
def transform(message):
    return f'{randint(1000, 9999)} {message}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)