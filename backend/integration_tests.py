import unittest
import flask_testing
from app import app, db, Role
from datetime import datetime

class TestApp(flask_testing.TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"  # Use an in-memory SQLite database for testing
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for testing
        app.config['TESTING'] = True

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        

class Test_Get_All_Roles(TestApp):
    def test_get_all_roles(self):
        # Initialize the test database with sample data
        r1 = Role(
            Role_ID=1,
            Role_Name='Manager 1',
            Role_Department='HR',
            Date_Posted='2023-11-01',
            App_Deadline='2023-11-02',
            Role_Description='Manager for role 1'
        )

        db.session.add(r1)
        db.session.commit()

        response = self.client.get("/roles/get_all_roles")
        data = response.json.get('data', {}).get('roles_with_details', [])
        expected_data = [
            {
                'App_Deadline': 'Thu, 02 Nov 2023 00:00:00 GMT',
                'Date_Posted': 'Wed, 01 Nov 2023 00:00:00 GMT',
                'Role_Department': 'HR',
                'Role_Description': 'Manager for role 1',
                'Role_ID': 1,
                'Role_Name': 'Manager 1',
            }
        ]
        print("Data from API:", data)
        print("Expected Data:", expected_data)
        self.assertEqual(data, expected_data)



def test_roles_search(self):
    r1 = Role(Role_ID=1, Role_Name='Manager 11', Role_Department='HR', Date_Posted='2023-10-1', App_Deadline='2023-10-2', Role_Description='Manager for role 1')
    
    response = self.client.get("/roles/search")
    data = response.json.get('data', [])
    expected_data = [
        {
            'App_Deadline': '2023-10-2',
            'Date_Posted': '2023-10-1',
            'Role_Department': 'HR',
            'Role_Description': 'Manager for role 1',
            'Role_ID': 1,
            'Role_Name': 'Manager 11',
        }
    ]
    self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
