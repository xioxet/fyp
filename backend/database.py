import psycopg2
import json

connection = psycopg2.connect(database='main', user='postgres', password='postgres', host='fyp-postgres', port=5432)
#connection.autocommit = True  

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
        return {"error":True, "message":"e"}
    

