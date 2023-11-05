import sqlite3
import unittest
import os
from app import app, db
import json  # Don't forget to import the json module
from app import Role, Staff, Skill, Role_Skill, Staff_Skill
from datetime import datetime 


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
 


    # def tearDown(self):
    #     # Clear data from the test database
    #     test_db_filename = 'instance/test.db'
    #     conn = sqlite3.connect(test_db_filename)
    #     cursor = conn.cursor()

    #     # # Clear data from all the tables
    #     # tables = [
    #     #     'Staff_Role_Apply',
    #     #     'Staff_Skill',
    #     #     'Role_Skill',
    #     #     'Role',
    #     #     'Skill',
    #     #     'Staff',
    #     #     'Access_Control'
    #     # ]

    #     # for table_name in tables:
    #     #     cursor.execute(f'DELETE FROM {table_name};')
    #     # conn.commit()
    #     # conn.close()
    

    ###################### LOGIN TESTS ###################################
    
    def test_successful_login_staff(self):
        # Send a POST request to the login endpoint
        print("------------Login Test Start------------")
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

        print("------------Login Test End------------")

#     ###################### ROLE ENDPOINT TESTS #####################

    def test_get_all_roles_with_data(self):
        # Test when there are roles in the database
        # You'll need to populate the database with test data
        # before running this test.
        response = self.app.get('/roles/get_all_roles')
        result = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("roles_with_details", result["data"])
        self.assertTrue(isinstance(result["data"]["roles_with_details"], list))

    # def test_get_all_roles_without_data(self):
    #     ### delete db 

    #     # Test when there are no roles in the database
    #     # You'll need to clear the database before running this test.
    #     response = self.app.get('/roles/get_all_roles')
    #     result = json.loads(response.data)

    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("roles_with_details", result["data"])
    #     self.assertTrue(isinstance(result["data"]["roles_with_details"], list))
    #     self.assertEqual(len(result["data"]["roles_with_details"]), 0)


# #     ################ view individual role test cases ######################
    
    
    # def test_get_role_details_success(self):
    #     with app.app_context():  # Create an application context
    #         role = Role(
    #             Role_ID=9999999,
    #             Role_Name='Test Role',
    #             Role_Description='This is a test role',
    #             Role_Department='Sales',
    #             App_Deadline='Fri, 29 Dec 2023 00:00:00 GMT',
    #             Date_Posted='Wed, 11 Oct 2023 00:00:00 GMT',
    #         )
    #         # Create role skills for the role
    #         role_skills = [
    #             Role_Skill(Role_Name='Account Manager', Skill_Name='Account Management'),
    #         ]
    #         db.session.add(role)
    #         db.session.add_all(role_skills)
    #         db.session.commit()
    
    #     # Assuming you have a valid role_id for an existing role in your database
    #     role_id = 9999999
    #     response = self.app.get(f'/role/view_role?role_id={role_id}')

    #     # Check the response status code (200 for success)
    #     self.assertEqual(response.status_code, 200)
    #     self.maxDiff = None
    #     # Assuming you know the expected JSON structure for the role details
    #     expected_data = {      
    #         'App_Deadline': 'Fri, 29 Dec 2023 00:00:00 GMT', 
    #         'Date_Posted': 'Wed, 11 Oct 2023 00:00:00 GMT', 
    #         'Role_Department': 'Sales', 
    #         'Role_Description': 'This is a test role',
    #         'Role_ID': 1000001,
    #         'Role_Name': 'Test Role',
    #         'Role_Skills': ['Account Management']
    #         }
        
    #     # Check if the response data matches the expected data
    #     data = json.loads(response.data)
    #     self.assertEqual(data, expected_data)


    # def test_get_role_details_role_not_found(self):
    #     # Assuming you're providing an invalid role_id that does not exist
    #     role_id = 999  
    #     response = self.app.get(f'/role/view_role?role_id={role_id}')

    #     # Check the response status code (404 for "Role not found")
    #     self.assertEqual(response.status_code, 404)

    #     # Check if the response message indicates that the role was not found
    #     response_data = json.loads(response.data)
    #     self.assertEqual(response_data['message'], 'Role not found')


    
# #     ############### End of view individual role test cases #################
    
# #     ###################### create new role test cases #####################

#     def test_create_role_success(self):
#         # Test creating a new role with valid data
#         role_data = {
#             'Role_Name': 'Content Creator',
#             'Role_Department': 'Marketing',
#             'Date_Posted': '2023-11-01',
#             'App_Deadline': '2023-11-15',
#             'Role_Description': 'Create content for the company',
#             'Role_Skills': ['Budgeting', 'Business Development']
#         }
#         response = self.app.post('/role/create', data=json.dumps(role_data), content_type='application/json')

#         data = json.loads(response.data)

#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(data['message'], 'Role listing created successfully.')

    

#     def test_create_role_missing_fields(self):
#         # Test creating a new role with missing required fields
#         role_data = {
#             'Role_Name': 'New Role',
#             'Role_Department': 'HR',
#             # Missing 'Date_Posted', 'App_Deadline', 'Role_Description', 'Role_Skills'
#         }
#         response = self.app.post('/role/create', data=json.dumps(role_data), content_type='application/json')

#         data = json.loads(response.data)

#         self.assertEqual(response.status_code, 400)
#         self.assertIn('Missing required fields', data['message'])


#     def test_create_role_invalid_date_format(self):
#         # Test creating a new role with invalid date format
#         role_data = {
#             'Role_Name': 'New Role',
#             'Role_Department': 'HR',
#             'Date_Posted': '2023-11-01',
#             'App_Deadline': '15/11/2023',  # Invalid date format
#             'Role_Description': 'Description of the new role',
#             'Role_Skills': ['Budgeting', 'Business Development']
#         }
#         response = self.app.post('/role/create', data=json.dumps(role_data), content_type='application/json')

#         data = json.loads(response.data)

#         self.assertEqual(response.status_code, 400)
#         self.assertIn('Invalid date format', data['message'])

#     def test_create_role_existing_role(self):
#         # Test creating a new role with a name that already exists
#         role_data = {
#             'Role_Name': 'Account Manager',  # Use an existing role name
#             'Role_Department': 'HR',
#             'Date_Posted': '2023-11-01',
#             'App_Deadline': '2023-11-15',
#             'Role_Description': 'Description of the new role',
#             'Role_Skills': ['Budgeting', 'Business Development']
#         }
#         response = self.app.post('/role/create', data=json.dumps(role_data), content_type='application/json')

#         data = json.loads(response.data)

#         self.assertEqual(response.status_code, 400)
#         self.assertIn('Role with this name already exists', data['message'])

    
# #         ############# Update role listing endpoint test cases #########


#     def test_update_role_success(self):

#         with app.app_context():  # Create an application context
            
#             role = Role(
#                 Role_Name= 'Account Manager',
#                 Role_Department= 'Finance',
#                 Date_Posted= '2023-02-01',
#                 App_Deadline= '2023/02/15',
#                 Role_Description= "The Account Manager acts as a key point of contact between an organization and its clients. He/She possesses thorough product knowledge and oversees product and/or service sales. He works with customers to identify their wants and prepares reports by collecting, analyzing, and summarizing sales information. He contacts existing customers to discuss and give recommendations on how specific products or services can meet their needs. He maintains customer relationships to strategically place new products and drive sales for long-term growth. He works in a fast-paced and dynamic environment, and travels frequently to clients' premises for meetings. He is familiar with client relationship management and sales tools. He is knowledgeable of the organization's products and services, as well as trends, developments, and challenges of the industry domain. The Sales Account Manager is a resourceful, people-focused, and persistent individual who takes rejection as a personal challenge to succeed when given the opportunity. He appreciates the value of long-lasting relationships and prioritizes efforts to build trust with existing and potential customers. He exhibits good listening skills and is able to establish rapport with customers and team members alike easily.",
#                 Role_ID = 1000001,
#             )

#             updated_role_data = {
#                 'Role_Name': 'Account Manager',
#                 'Role_Department': 'Finance',
#                 'Date_Posted': '2023-02-01',
#                 'App_Deadline': '2023-02-15',
#                 'Role_Description': 'Updated Description',
#                 'Role_Skills': [
#                     'Account Management', 'Budgeting', 'Business Development',
#                     'Business Needs Analysis', 'Business Negotiation', 'Collaboration',
#                     'Communication', 'Data Analytics', 'Pricing Strategy',
#                     'Problem Solving', 'Product Management', 'Sales Strategy',
#                     'Stakeholder Management'
#                 ]
#             }
            

#             # Send a PUT request to update the role
#             response = self.app.put('/role/update?role_id=' + str(role.Role_ID), data=json.dumps(updated_role_data), content_type='application/json')
#             updated_role = Role.query.get(role.Role_ID)
#             self.assertEqual(response.status_code, 200)
#             data = json.loads(response.data)
            
            
#             updated_role = Role.query.get(role.Role_ID)

#             # Verify that the role has been updated in the database
#             self.assertEqual(updated_role.Date_Posted, datetime.strptime(updated_role_data['Date_Posted'], '%Y-%m-%d').date())
#             self.assertEqual(updated_role.Role_Name, updated_role_data['Role_Name'])
#             self.assertEqual(updated_role.Role_Department, updated_role_data['Role_Department'])
#             self.assertEqual(updated_role.App_Deadline, datetime.strptime(updated_role_data['App_Deadline'], '%Y-%m-%d').date())
#             self.assertEqual(updated_role.Role_Description, updated_role_data['Role_Description'])
#             self.assertEqual(data['message'], 'Role updated successfully.')


#     def test_update_role_not_found(self):
#         # Test updating a role that does not exist
#         role_id = 9999
#         updated_role_data = {
#             'Role_Name': 'Updated Role Name',
#             'Role_Department': 'Updated Department',
#             'Date_Posted': '2023-11-01',
#             'App_Deadline': '2023-11-15',
#             'Role_Description': 'Updated Description',
#             'Role_Skills': ['Account Management', 'Budgeting']
#         }
#         response = self.app.put(f'/role/update?role_id={role_id}', data=json.dumps(updated_role_data), content_type='application/json')
        
#         self.assertEqual(response.status_code, 404)
#         data = json.loads(response.data)
#         self.assertEqual(data['message'], 'Role not found')

#     def test_update_role_with_invalid_dates(self):
#         # Test updating a role with invalid date formats
#         role_id = 1000001
#         updated_role_data = {
#             'Role_Name': 'Account Manager',
#             'Role_Department': 'Finance',
#             'Date_Posted': '2023-02-01',
#             'App_Deadline': '2023/02/15',
#             'Role_Description': 'Updated Description',
#             'Role_Skills': [
#                 'Account Management', 'Budgeting', 'Business Development',
#                 'Business Needs Analysis', 'Business Negotiation', 'Collaboration',
#                 'Communication', 'Data Analytics', 'Pricing Strategy',
#                 'Problem Solving', 'Product Management', 'Sales Strategy',
#                 'Stakeholder Management'
#             ]
#         }
#         response = self.app.put(f'/role/update?role_id={role_id}', data=json.dumps(updated_role_data), content_type='application/json')
        
#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.data)
#         self.assertIn('Invalid date format for', data['message'])

#     # def test_update_role_change_name(self):
#     #     # Test updating a role with a changed name, which should create a new role
#     #     role_id = 1000001
#     #     updated_role_data = {
#     #         'Role_Name': 'Account Manager 2',
#     #         'Role_Department': 'Finance',
#     #         'Date_Posted': '2023-02-01',
#     #         'App_Deadline': '2023-02-15',
#     #         'Role_Description': 'Updated Description',
#     #         'Role_Skills': [
#     #             'Account Management', 'Budgeting', 'Business Development',
#     #             'Business Needs Analysis', 'Business Negotiation', 'Collaboration',
#     #             'Communication', 'Data Analytics', 'Pricing Strategy',
#     #             'Problem Solving', 'Product Management', 'Sales Strategy',
#     #             'Stakeholder Management'
#     #         ]
#     #     }
#     #     response = self.app.put(f'/role/update?role_id={role_id}', data=json.dumps(updated_role_data), content_type='application/json')
        
#     #     self.assertEqual(response.status_code, 201)
#     #     data = json.loads(response.data)
#     #     self.assertIn('Role updated successfully', data['message'])




# #     ############### End of update new role test cases #####################

# #     ############## create new staff endpoint test cases #####################

#     def test_create_staff_success(self):
#         # Test creating a new staff member
#         staff_data = {
#             'Staff_FName': 'Shan',
#             'Staff_LName': 'Mei',
#             'Dept': 'IT',
#             'Country': 'Singapore',
#             'Email': 'shanmei@allinone.com',
#             'Access_Role': 2,
#             'Password': '12345678',
#         }
#         response = self.app.post('/staff/create', data=json.dumps(staff_data), content_type='application/json')

#         self.assertEqual(response.status_code, 202)  # Expect a successful creation
#         data = json.loads(response.data)
#         self.assertEqual(data['message'], 'Staff member created successfully')
#         self.assertIsNotNone(data['data']['Staff_ID'])  # Staff ID should be generated


#     def test_create_staff_missing_field(self):
#         # Test creating a staff member with a missing required field
#         staff_data = {
#             'Staff_FName': 'Alice',
#             'Dept': 'Finance',
#             'Country': 'Canada',
#             'Email': 'alice@example.com',
#             'Access_Role': 'Admin'
#         }
#         response = self.app.post('/staff/create', data=json.dumps(staff_data), content_type='application/json')

#         self.assertEqual(response.status_code, 400)  # Expect a bad request
#         data = json.loads(response.data)
#         self.assertIn('Missing required field', data['message'])
    
    
#     def test_create_staff_duplicate_attributes(self):
#         # Test creating a staff member with attributes that already exist
#         staff_data = {
#             'Staff_FName': 'Shan',
#             'Staff_LName': 'Mei',
#             'Dept': 'IT',
#             'Country': 'Singapore',
#             'Email': 'shanmei@allinone.com',
#             'Access_Role': 2,
#             'Password': '12345678',
#         }
#         response = self.app.post('/staff/create', data=json.dumps(staff_data), content_type='application/json')

#         self.assertEqual(response.status_code, 400)  # Expect a bad request
#         data = json.loads(response.data)
#         self.assertIn('Staff member with the same attributes already exists', data['message'])


#     ############# End of create new staff endpoint test cases ##########

#     ######## get staff profile endpoint test cases #####################

    # def test_get_staff_profile_success(self):
    #     # Assuming that a staff record with Staff_ID 123 exists in your database
    #     response = self.app.get('/staff/get_profile?staff_id=130001')

    #     # Check the response status code (should be 200 for success)
    #     self.assertEqual(response.status_code, 200)

    #     # Check the JSON response for the expected structure
    #     response_data = json.loads(response.data.decode('utf-8'))
    #     self.assertIn('staff_profile', response_data)
    #     staff_profile = response_data['staff_profile']
    #     self.assertIn('Staff_ID', staff_profile)
    #     self.assertIn('Staff_FName', staff_profile)
    #     self.assertIn('Staff_LName', staff_profile)
    #     self.assertIn('Staff_Skills', staff_profile)

    #     # Optionally, you can check the values of specific fields
    #     self.assertEqual(staff_profile['Staff_FName'], 'John')
    #     self.assertEqual(staff_profile['Staff_LName'], 'Sim')

    # def test_get_staff_profile_negative(self):
    #     # Assuming that there is no staff record with Staff_ID 999 in your database
    #     response = self.app.get('/staff/get_profile?staff_id=9999999')

    #     # Check the response status code (should be 404 for not found)
    #     self.assertEqual(response.status_code, 404)

    #     # Check the JSON response for the expected error message
    #     response_data = json.loads(response.data.decode('utf-8'))
    #     self.assertIn('message', response_data)
    #     self.assertEqual(response_data['message'], 'Staff not found')



# ############ Role Skill Match Percentage Test Cases #####################
#     # def test_calculate_role_matches_positive(self):

#     #     response = self.app.get('/staff/role-matches?staff_id=1400001')

#     #     # Check the response status code (should be 200 for success)
#     #     self.assertEqual(response.status_code, 200)

#     #     # Check the JSON response for the expected structure
#     #     response_data = json.loads(response.data.decode('utf-8'))
#     #     self.assertIn('data', response_data)
#     #     data = response_data['data']
#     #     self.assertTrue(data)  # Ensure that there are role matches

#     #     # Optionally, you can check the values of specific fields in the role matches
#     #     role_match = data[0]  # Assuming you want to check the first role match
#     #     self.assertIn('Role_Name', role_match)
#     #     self.assertIn('Percentage_Matched', role_match)
#     #     self.assertIn('Skills_Matched', role_match)
#     #     self.assertIn('Skills_Gap', role_match)

#     # def test_calculate_role_matches_success(self):
#     #     response = self.app.get('/staff/role-matches?staff_id=1400001')

#     #     # Check the response status code (should be 200 for success)
#     #     self.assertEqual(response.status_code, 200)

#     #     # Check the JSON response for the expected structure
#     #     response_data = json.loads(response.data.decode('utf-8'))
#     #     self.assertIn('data', response_data)
#     #     data = response_data['data']
#     #     self.assertTrue(data)  # Ensure that there are role matches

#     #     # Optionally, you can check the values of specific fields in the role matches
#     #     role_match = data[0]  # Assuming you want to check the first role match
#     #     self.assertIn('Role_Name', role_match)
#     #     self.assertIn('Percentage_Matched', role_match)
#     #     self.assertIn('Skills_Matched', role_match)
#     #     self.assertIn('Skills_Gap', role_match)

#     # def test_calculate_role_matches_no_skills(self):
#     #     # Assuming that there is no staff record with Staff_ID 999 in your database
#     #     response = self.app.get('/staff/role-matches?staff_id=999')

#     #     # Check the response status code (should be 404 for not found)
#     #     self.assertEqual(response.status_code, 404)

#     #     # Check the JSON response for the expected error message
#     #     response_data = json.loads(response.data.decode('utf-8'))
#     #     self.assertIn('message', response_data)
#     #     self.assertEqual(response_data['message'], 'Staff member not found or has no skills')


# ########## View applicants endpoint test cases #####################
#     def test_view_applicants_skills_positive(self):
#         # Prepare the test data: Insert a role, applicants, and their skills into your database
#         role_name = 'Admin Executive'
#         # Make an HTTP GET request to the endpoint with a valid role name
#         response = self.app.get("/role_application/view_applicants?role_name=" + role_name)

#         # Check the response status code (should be 200 for success)
#         self.assertEqual(response.status_code, 200)

#         # Check the JSON response for the expected structure
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertIn('data', response_data)
#         data = response_data['data']
#         self.assertTrue(data)  # Ensure that there are applicants

#         # Optionally, you can check the values of specific fields in the applicant details
#         applicant = data[0]  # Assuming you want to check the first applicant
#         self.assertIn('Applicant_ID', applicant)
#         self.assertIn('Applicant_Email', applicant)
#         self.assertIn('Applicant_Department', applicant)
#         self.assertIn('Applicant_Country', applicant)
#         self.assertIn('Applicant_Name', applicant)
#         self.assertIn('Applicant_Skills', applicant)
#         self.assertIn('Applicant_Skills_Percentage_Matched', applicant)
    
#     def test_view_applicants_skills_invalid_role(self):
#         # Ensure that the test database is empty or does not contain the specified role
#         # Make an HTTP GET request to the endpoint with an invalid role name
#         response = self.app.get('/role_application/view_applicants?role_name=InvalidRole')

#         # Check the response status code (should be 404 for not found)
#         self.assertEqual(response.status_code, 404)

#         # Check the JSON response for the expected error message
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertIn('message', response_data)
#         self.assertEqual(response_data['message'], 'Role not found')


#     def test_view_applicants_skills_no_applicants(self):
#         # Assuming that the database is empty or no applicants for the specified role
#         role_name = "Content Creator"

#         response = self.app.get(f'/role_application/view_applicants?role_name={role_name}')

#         # Check the response status code (should be 404 for no applicants)
#         self.assertEqual(response.status_code, 404)

#         # Check the JSON response for the expected error message
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertIn('message', response_data)
#         self.assertEqual(response_data['message'], 'No applicants for this role')
# # ############# apply role endpoint test cases ##################

#     def test_submit_application_success(self):
#         # Assuming you have a staff and role in your test database
#         staff_id = 140008  # Replace with a valid staff ID
#         role_id = 1000004  # Replace with a valid role ID

#         # Make a POST request to the endpoint
#         response = self.app.post(f'/staff/submit_application?staff_id={staff_id}', data={'role_id': role_id})

#         # Check the response content (should be "Application submitted successfully.")
#         self.assertEqual(response.data.decode('utf-8'), "Application submitted successfully.")
#         self.assertEqual(response.status_code, 200)

#     def test_submit_application_duplicate(self):
#         # Assuming you have a staff, role, and an existing application in your test database
#         staff_id = 130001  # Replace with a valid staff ID
#         role_id = 1000001  # Replace with a valid role ID


#         # Make a POST request to the endpoint
#         response = self.app.post(f'/staff/submit_application?staff_id={staff_id}', data={'role_id': role_id})

#         # Check the response content (should be "You have already applied for this role.")
#         self.assertEqual(response.data.decode('utf-8'), "You have already applied for this role.")
#         self.assertEqual(response.status_code, 200)


# #     ############  view applied roles endpoint test cases ##################
#     def test_get_applied_roles_positive(self):
#         staff_id = 130001  # Replace with a valid staff ID from your test data

#         response = self.app.get(f'/staff/applied_roles?staff_id={staff_id}')

#         # Check the response status code (should be 200 for success)
#         self.assertEqual(response.status_code, 200)

#         # Check the JSON response for the expected structure
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertIn('data', response_data)
#         data = response_data['data']
#         self.assertTrue(data)  # Ensure that there are applied roles

#         # Optionally, you can check the values of specific fields in the applied roles
#         applied_role = data[0]  # Assuming you want to check the first applied role
#         self.assertIn('Role_Name', applied_role)
#         self.assertIn('Role_Description', applied_role)
#         self.assertIn('Role_Skills', applied_role)  # Assuming you want to check the role skills

#     def test_get_applied_roles_no_data(self):
#         staff_id = 140003  # Replace with a valid staff ID from your test data

#         response = self.app.get(f'/staff/applied_roles?staff_id={staff_id}')

#         # Check the response status code (should be 404 for no applied roles)
#         self.assertEqual(response.status_code, 404)

#         # Check the JSON response for the expected error message
#         response_data = json.loads(response.data.decode('utf-8'))
#         self.assertIn('message', response_data)
#         self.assertEqual(response_data['message'], 'You have not applied for any roles yet.')

    
    # def test_get_all_skills(self):
    #         with app.app_context():  # Create an application context
    #             # Add sample skills to the test database
    #             skills_data = ['A1', 'A2', 'A3']
    #             for skill_name in skills_data:
    #                 skill = Skill(Skill_Name=skill_name, Skill_Desc="Skill Description")
    #                 db.session.add(skill)
    #             db.session.commit()

    #             # Make a GET request to the /skills/get_all_skills endpoint
    #             response = self.app.get('/skills/get_all_skills')

    #             # Check the response status code (should be 200)
    #             self.assertEqual(response.status_code, 200)

    #             # Check the JSON response for the expected structure
    #             response_data = response.get_json()
    #             self.assertIn('data', response_data)
    #             self.assertIn('skill_names', response_data['data'])

    #             # Check if skill names in the response match the added skills
    #             skill_names_response = response_data['data']['skill_names']
    #             self.assertEqual(sorted(skill_names_response), sorted(skills_data))







if __name__ == '__main__':
    unittest.main()