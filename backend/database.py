import psycopg2
from dotenv import load_dotenv
import json
import uuid
import login
import os

load_dotenv()
postgres_url = os.getenv('POSTGRES_URL')
secret_key = os.getenv('SECRET_KEY')
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_db = os.getenv('POSTGRES_DB')
connection = psycopg2.connect(
    database=postgres_db, 
    user=postgres_user, 
    password=postgres_password, 
    host=postgres_url,
    port=5432
)

connection.autocommit = True
cursor = connection.cursor()

def get_messages(accesstoken):
    try:
        uuid = login.get_jwt_uuid(accesstoken, secret_key)
        print(accesstoken, uuid)
        SQL = "SELECT * FROM messages WHERE uuid=(%s)"
        cursor.execute(SQL, (uuid,))
        messages = []
        for message in cursor:
            message_json = {
                "uuid":message[0],
                "timestamp":str(message[1]),
                "messagecontent":message[2],
                "fromuser":message[3]
            }
            messages.append(message_json)
        return messages
    except Exception as e:
        print(e)
        return {"error":e}


def add_message(accesstoken, messagecontent, fromuser):
    try:
        uuid = login.get_jwt_uuid(accesstoken, secret_key)
        SQL = "INSERT INTO messages (uuid, messagecontent, fromuser) VALUES (%s, %s, %s)"
        cursor.execute(SQL, (uuid, messagecontent, fromuser))
        return {"error":False}
    except Exception as e:
        return {"error":True, "message":str(e)}
    

def reset_chat():
    try:
        SQL = "DELETE FROM messages WHERE messagecontent!='if you are seeing this, the postgres initialization worked'"
        cursor.execute(SQL)
        return {"error":False}
    except Exception as e:
        return {"error":True, "message":str(e)}


def add_user(username, password):
    try:
        uuid_4 = str(uuid.uuid4())
        password = login.generate_hash(password)
        SQL = "INSERT INTO users (uuid, username, password) VALUES (%s, %s, %s)"
        cursor.execute(SQL, (uuid_4, username, password))
        return {"error":False}
    except Exception as e:
        return {"error":True, "message":str(e)}

def get_users():
    try:
        SQL = "SELECT * FROM users"
        cursor.execute(SQL)
        users = []
        for user in cursor:
            user_json = {
                "uuid":user[0],
                "username":user[1],
                "password":user[2]
            }
            users.append(user_json)
        return users
    except Exception as e:
        return {"error":True, "message":str(e)}

def verify_login(username, password):
    try:
        SQL = "SELECT * FROM users WHERE username = %s"
        cursor.execute(SQL, (username,))
        user = cursor.fetchone()
        if user:
            uuid4, username, hashed = user
            if login.verify_hash(hashed, password):
                jwt = login.create_jwt(
                    {"uuid":uuid4, "username":username}, secret_key
                )
                return {"error":False, "message":jwt, "username":username}
        return {"error":True, "message":"Invalid login credentials!"}
    
    except Exception as e:
        return {"error":True, "message":str(e), "SQL":str(SQL)}, 
