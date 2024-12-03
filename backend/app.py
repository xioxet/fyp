from flask import Flask
from flask import request
from random import randint
app = Flask(__name__)

@app.route('/process_message', methods = ['POST'])
def process_message_endpoint():
    message = request.form.get('message')
    return {
        'messagecontent':
        process_message(message)
        }

def process_message(message):
    # sample function
    return f"hello {randint(1, 100000)}"


if __name__ == '__main__':
   app.run(debug=True)
