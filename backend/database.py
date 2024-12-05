import psycopg2

connection = psycopg2.connect(database='main', user='postgres', password='postgres', host='fyp-postgres', port=5432)

cursor = connection.cursor()

def get_messages(uuid):
    SQL = "SELECT * FROM messages WHERE "
