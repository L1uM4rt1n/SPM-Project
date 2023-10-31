import io
import os
import unittest
import json
from app import app, db

class LoginEndpointTest(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
    def test_successful_login_staff(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'Staff' access rights

        # Send a POST request to the login endpoint
        response = self.app.post('/login', data=json.dumps({
            'Email': 'Susan.Goh@allinone.com.sg',
            'Password': 'nCK8Xe18',
            'Access_Rights': 'Staff'
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    def test_successful_login_staff_hr(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'HR' access rights

        # Send a POST request to the login endpoint
        response = self.app.post('/login', data=json.dumps({
            'Email': 'Sophia.Fu@allinone.com.sg',
            'Password': 'FhJxXgEV',
            'Access_Rights': 'HR'
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    def test_unsuccessful_login_staff_hr(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'HR' access rights

        # Send a POST request with incorrect password
        response = self.app.post('/login', data=json.dumps({
            'Email': 'Sophia.Fu@allinone.com.sg',
            'Password': 'FhjkXgEV1',
            'Access_Rights': 'HR'
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Incorrect password')

    def test_unsuccessful_login_staff_trying_hr_access(self):
        # Create a test staff member in the database
        # Add the necessary data for a staff with 'Staff' access rights

        # Send a POST request trying to access 'HR'
        response = self.app.post('/login', data=json.dumps({
            'Email': 'Susan.Goh@allinone.com.sg',
            'Password': 'nCK8Xe18',
            'Access_Rights': 'HR'
        }), content_type='application/json')

        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Restricted Access')



if __name__ == '__main__':
    unittest.main()       