import sqlite3
import unittest
import os,sys
from app import app, db
import json  # Don't forget to import the json module

# os.environ['FLASK_ENV'] = 'testing'


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        # Create a test database by executing the SQL script
        # Ensure the script is located in the same directory as this test script
        test_db_filename = 'instance/test.db' 
        script_filename = 'test.sql'
        print(test_db_filename)
        print("Current working directory:", os.getcwd())
        # Use SQLite to execute the SQL script

        # Set Flask configuration to use the test database
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///'
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        with app.app_context():
            db.create_all()

        
        conn = sqlite3.connect(test_db_filename)
        cursor = conn.cursor()
        with open(script_filename, 'r') as script_file:
            cursor.executescript(script_file.read())
        conn.commit()
        conn.close()
 

    def tearDown(self):
        # Clear data from the test database
        test_db_filename = 'instance/test.db'
        conn = sqlite3.connect(test_db_filename)
        cursor = conn.cursor()

        # Clear data from all the tables
        tables = [
            'Staff_Role_Apply',
            'Staff_Skill',
            'Role_Skill',
            'Role',
            'Skill',
            'Staff',
            'Access_Control'
        ]

        for table_name in tables:
            cursor.execute(f'DELETE FROM {table_name};')
        conn.commit()
        conn.close()

################ LOGIN ##################################################

    def test_successful_login_staff(self):
        # Send a POST request to the login endpoint
        print("Test Start")
        response = self.app.post('/login', data=json.dumps({
            "Email": "Susan.Goh@allinone.com.sg",
            "Password": "nCK8Xe18",
            "Access_Role": "Staff"
        }), content_type='application/json')

        data = json.loads(response.data)
        print(data["message"])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Login successful")
        print("Test End")

    def test_successful_login_staff_hr(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'HR' access rights

        # Send a POST request to the login endpoint
        response = self.app.post('/login', data=json.dumps({
            "Email": "Sophia.Fu@allinone.com.sg",
            "Password": "FhJxXgEV",
            "Access_Role": "HR"
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Login successful")

    def test_unsuccessful_login_staff_hr(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'HR' access rights

        # Send a POST request with incorrect password
        response = self.app.post('/login', data=json.dumps({
            "Email": "Sophia.Fu@allinone.com.sg",
            "Password": "FhjkXgEV1",
            "Access_Role": "HR"
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["message"], "Incorrect password")

    def test_unsuccessful_login_staff_trying_hr_access(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'Staff' access rights

        # Send a POST request trying to access 'HR'
        response = self.app.post('/login', data=json.dumps({
            "Email": "Susan.Goh@allinone.com.sg",
            "Password": "nCK8Xe18",
            "Access_Role": "HR"
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["message"], "Staff has no HR Rights")

# ################ STAFF ##################################################

    def test_get_all_roles(self):

        # Send a GET request to the /roles/get_all_roles endpoint
        response = self.app.get('/roles/get_all_roles')
        data = json.loads(response.data)

        # Check if the response code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected JSON structure
        self.assertIn("code", data)
        self.assertEqual(data["code"], 200)
        self.assertIn("data", data)
        self.assertIn("roles_with_details", data["data"])

        # Check if the response data includes role details and skills
        roles_with_details = data["data"]["roles_with_details"]
        self.assertTrue(isinstance(roles_with_details, list))
        self.assertTrue(len(roles_with_details) > 0)
        for role in roles_with_details:
            self.assertIn("Role_ID", role)
            self.assertIn("Role_Name", role)
            self.assertIn("Role_Department", role)
            self.assertIn("Role_Description", role)
            self.assertIn("Date_Posted", role)
            self.assertIn("App_Deadline", role)

    
    def test_get_role_details_success(self):
        # Assuming you have a valid role_id for an existing role in your database
        role_id = 1000001
        response = self.app.get(f'/role/view_role?role_id={role_id}')

        # Check the response status code (200 for success)
        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        # Assuming you know the expected JSON structure for the role details
        expected_data = {      
            'App_Deadline': 'Fri, 29 Dec 2023 00:00:00 GMT', 
            'Date_Posted': 'Wed, 11 Oct 2023 00:00:00 GMT', 
            'Role_Department': 'Sales', 
            'Role_Description': "The Account Manager acts as a key point of contact between an organisation and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analysing, and summarising sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organisation's products and services, as well as trends, developments and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused and persistent individual, who takes rejection as a personal challenge to succeed when given opportunity. He appreciates the value of long lasting relationships and prioritises efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily.",
            'Role_ID': 1000001,
            'Role_Name': 'Account Manager',
            'Role_Skills': ['Account Management','Budgeting','Business Development', 'Business Needs Analysis', 'Business Negotiation','Collaboration','Communication','Data Analytics', 'Pricing Strategy','Problem Solving','Product Management', 'Sales Strategy','Stakeholder Management']
            }
        
        # Check if the response data matches the expected data
        data = json.loads(response.data)
        self.assertEqual(data, expected_data)
        
if __name__ == '__main__':
    unittest.main()
