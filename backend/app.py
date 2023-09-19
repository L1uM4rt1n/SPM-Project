from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
from urllib.parse import quote
from dotenv import load_dotenv
load_dotenv()

password = os.getenv("MONGODB_PASSWORD").encode()
encoded_password = quote(password)
connection_string = f"mongodb+srv://g1t7-is212-dev:{encoded_password}@sbrp.wtds9l8.mongodb.net/?retryWrites=true&w=majority" 
client = MongoClient(connection_string)

db = client['skills_based_role_portal']

try:
    database_list = client.list_database_names()
    print("Connection to MongoDB established successfully.")
    print("Available databases:", database_list)
except Exception as e:
    print("Connection to MongoDB failed:", e)
    
app = Flask(__name__)
CORS(app)

@app.route('/get_all_jobs', methods=['GET'])
def get_all_jobs():
    job_listings = db.job_listings.find()
    job_listings = [job for job in job_listings]

    if job_listings:
        jobs = []
        for job in job_listings:
            job['_id'] = str(job['_id'])
            jobs.append(job)
        print(jobs)
        return jsonify(
            {
                "code": 200, 
                'job_listings': jobs
            }
        )
    return jsonify(
        {
            "code": 404, 
            "message": "Jobs not found."
            }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)