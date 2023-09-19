from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from urllib.parse import quote
from bson import ObjectId
import json, os
from datetime import datetime, time
import pymongo

load_dotenv()

password = os.getenv("MONGODB_PASSWORD").encode()
encoded_password = quote(password)
connection_string = f"mongodb+srv://g1t7-is212-dev:{encoded_password}@sbrp.wtds9l8.mongodb.net/?retryWrites=true&w=majority" 

client = pymongo.MongoClient(connection_string)
db = client["skills_based_role_portal"]

try:
    # List available databases (a simple operation to check connection)
    database_list = client.list_database_names()
    print("Connection to MongoDB established successfully.")
    print("Available databases:", database_list)
except Exception as e:
    print("Connection to MongoDB failed:", e)

app = Flask(__name__)
CORS(app)

#Get all jobs
@app.route("/jobs", methods=['GET'])
def get_all_jobs():
    jobs_collection_ref = db.get_collection('job_listings')
    
    try:
        job_doc_ref = jobs_collection_ref.find()
        job_doc_ref = [job for job in job_doc_ref]
        jobs = []

        for job in job_doc_ref:
            job['_id'] = str(job['_id'])
            job['App_Deadline'] = job['App_Deadline'].isoformat()
            job['Date_Posted'] = job['Date_Posted'].isoformat()
            jobs.append(job)
            
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
                "code": 500,
                "message": f"Error retrieving jobs: {str(e)}"
            }
        )

# Get job by specific job_id (represented by '_id')
@app.route("/jobs/<string:jobid>", methods=['GET'])
def get_listing_by_listingid(jobid):

    jobs_collection_ref = db.get_collection('job_listings')
    
    try:
        job_doc_ref = jobs_collection_ref.find_one({"_id": ObjectId(jobid)})
    except Exception as e:
        return jsonify(
            {
                "code": 404,
                "message": f"Error retrieving listing: {str(e)}"
            }
        ), 404
    
    if job_doc_ref is None:
        return jsonify(
            {
                "code": 404,
                "message": "There is no job with this job_id"
            }
        ), 404

    job_doc_ref['_id'] = str(job_doc_ref['_id'])

    return jsonify(
            {
                "code": 200,
                "data": job_doc_ref
            }
        )

#Search for job by specific keyword that matches words in job title
@app.route("/jobs/search", methods=['GET'])
def search_jobs():
    # Get the search query from the request parameters
    search_query = request.args.get('query', '')

    # Query the job_listings collection to find job titles that contain the search query
    jobs_collection_ref = db.get_collection('job_listings')
    matching_jobs = []

    try:
        job_doc_ref = jobs_collection_ref.find({"Role_Name": {"$regex": search_query, "$options": "i"}})

        for job in job_doc_ref:
            job['_id'] = str(job['_id'])
            matching_jobs.append(job)

        return jsonify(
            {
                "code": 200,
                "data": {
                    "jobs": matching_jobs
                }
            }
        )
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": f"Error searching jobs: {str(e)}"
            }
        )

#####################################
# RUN SCRIPT
#####################################

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5007, debug=True)