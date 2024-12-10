import psycopg2
from functools import lru_cache
import json
import uuid
import users
import os

postgres_url = os.environ['POSTGRES_URL']

connection = psycopg2.connect(
    database='main', 
    user='postgres', 
    password='postgres', 
    host=postgres_url,
    port=5432
)

cursor = connection.cursor()


def get_messages(uuid):
    try:
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
    except psycopg2.ProgrammingError as e:
            return {"error":e}



def add_message(uuid, messagecontent, fromuser):
    try:
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
        uuid = uuid.uuid4()
        password = generate_hash(password)
        SQL = "INSERT INTO users (uuid, username, password) VALUES (%s, %s, %s)"
        cursor.execute(SQL, (uuid, username, password))
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
