from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import quote
import os
import datetime, time
import uuid
import base64
import pymongo

password = os.getenv("MONGODB_PASSWORD").encode()
encoded_password = quote(password)
connection_string = f"mongodb+srv://g1t7-is212-dev:{password}@sbrp.wtds9l8.mongodb.net/?retryWrites=true&w=majority" 

client = pymongo.MongoClient(connection_string)
db = client["g1t7-is212-dev"]

try:
    # List available databases (a simple operation to check connection)
    database_list = client.list_database_names()
    print("Connection to MongoDB established successfully.")
    print("Available databases:", database_list)
except Exception as e:
    print("Connection to MongoDB failed:", e)

app = Flask(__name__)
CORS(app)

@app.route("/jobs", methods=['GET'])
def get_all_jobs():
    return 1