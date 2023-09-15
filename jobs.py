from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import quote
import os
import datetime, time
import uuid
import base64
import pymongo

load_dotenv()

password = os.getenv("MONGODB_PASSWORD").encode()
encoded_password = quote(password)
connection_string = f"mongodb+srv://g1t7-is212-dev:{encoded_password}@sbrp.wtds9l8.mongodb.net/?retryWrites=true&w=majority" 

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
    jobs_collection_ref = db.get_collection('job_listings')
    
    try:
        job_doc_ref = jobs_collection_ref.find()
        jobs = []

        for job in job_doc_ref:
            job_dict = job  
            job_dict['jobid'] = str(job['_id']) 
            jobs.append(job_dict)


        if len(jobs) == 0:
            return jsonify(
                {
                    "code": 404,
                    "message": "No jobs found"
                }
            )
        
        return jsonify(
            {
                "code": 200,
                "data": {
                    "jobs": jobs
                } 
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": f"Error retrieving jobs: {str(e)}"
            }
        )
    

#####################################
# RUN SCRIPT
#####################################

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5007, debug=True)