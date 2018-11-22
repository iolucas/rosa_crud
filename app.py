from flask import Flask
app = Flask(__name__)

import random

#Setup database connection
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['rosa_database']
complaint = db['complaint']


@app.route("/")
def hello():
    return "Hello World!"

def get_random_id():
    return random.randint(10000, 99999)

def get_new_id():
    random_id = get_random_id()
    while complaint.find_one({"_id": random_id}):
        random_id = get_random_id()
        
    new_id = complaint.insert_one({"_id": random_id}).inserted_id
    
    return new_id

@app.route("/complaint")
def new_complaint():
    new_id = get_new_id()
    return str(new_id)


# def status_queixa():
#     pass

# def atualizar_queixa():
#     pass


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)