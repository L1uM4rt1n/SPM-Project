import json
from datetime import datetime
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

collection_schemas = {
    "job_listings": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["Job_ID", "Role_Name", "Date_Posted", "App_Deadline", "Job_Department", "Job_Description", "Job_Requirements", "Skills_Req"],
            "properties": {
                "_id": None,
                "Job_ID": {
                    "bsonType": "int32"
                },
                "Role_Name": {
                    "bsonType": "string"
                },
                "Date_Posted": {
                    "bsonType": "date"
                },
                "App_Deadline": {
                    "bsonType": "date"
                },
                "Job_Department": {
                    "bsonType": "string"
                },
                "Job_Description": {
                    "bsonType": "string"
                },
                "Job_Requirements": {
                    "bsonType": "string"
                }
            }
        }
    },
    "role_skill": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["Role_Name", "Skill_Name"],
            "properties": {
                "Role_Name": {
                    "bsonType": "string"
                },
                "Skills_Req": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "string"
                    }
                }
            }
        }
    },
    "staff": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["Staff_ID", "Staff_FName", "Staff_LName", "Dept", "Country", "Email", "Access_Rights"],
            "properties": {
            "_id": None,
            "Staff_ID": {
                "bsonType": "int32"
            },
            "Staff_FName": {
                "bsonType": "string"
            },
            "Staff_LName": {
                "bsonType": "string"
            },
            "Dept": {
                "bsonType": "string"
            },
            "Country": {
                "bsonType": "string"
            },
            "Email": {
                "bsonType": "string"
            },
            "Access_Rights": {
                "bsonType": "int32"
            }
        }
        }
    },
    "staff_skill": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["Staff_ID", "Skill_Name"],
            "properties": {
                "_id": None,
                "Staff_ID": {
                    "bsonType": "int32"
                },
                "Skill_Name": {
                    "bsonType": "string"
                }
            }
        }
    }
}

for collection_name, schema in collection_schemas.items():
    json_file_path = f'{collection_name}.json'
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    for document in data:
        unique_field = "Job_ID" if collection_name == "job_listings" else "Staff_ID"
        existing_document = db[collection_name].find_one({unique_field: document[unique_field]})

        if existing_document is None:
            if "Date_Posted" in document:
                document["Date_Posted"] = datetime.fromisoformat(document["Date_Posted"])
            if "App_Deadline" in document:
                document["App_Deadline"] = datetime.fromisoformat(document["App_Deadline"])
            db[collection_name].insert_one(document)
            
        else:
            if existing_document != document:
                print(f"Updating document with {unique_field} {document[unique_field]}")
                db[collection_name].replace_one({unique_field: document[unique_field]}, document)
            else:
                print(f"Document with {unique_field} {document[unique_field]} already exists.")
            
client.close()