from flask import Flask, request, jasonify
from flask_cors import CORS
import datetime, time
import uuid
import base64
import pymongo

mongo_host =
mongo_port = 27017
mongo_database = 

client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
db = client[mongo_database]

app = Flask(__name__)
CORS(app)

@app.route("/jobs", methods=['GET'])
def get_all_jobs():
    