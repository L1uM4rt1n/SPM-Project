import unittest
from app import app, db, AccessRights, Staff, Skill, Role, Role_Skill, Staff_Skill, Staff_Role_Apply

# This is an optional testing library to set up a test environment
from flask_testing import TestCase

class AppTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory SQLite database
        return app

    def setUp(self):
        db.create_all()
        # Initialize the test database with sample data if needed

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        # Clean up the test database after each test

    # Write test cases for each class and their methods

    def test_AccessRights(self):
        access_right = AccessRights(Access_Control_Name="Test Access Control")
        db.session.add(access_right)
        db.session.commit()

        retrieved_access_right = AccessRights.query.first()
        self.assertEqual(retrieved_access_right.Access_Control_Name, "Test Access Control")

    def test_Staff(self):
        staff = Staff(Staff_FName="John", Staff_LName="Doe", Dept="Test Dept", Country="Test Country", Email="test@example.com")
        db.session.add(staff)
        db.session.commit()

        retrieved_staff = Staff.query.first()
        self.assertEqual(retrieved_staff.Staff_FName, "John")
        self.assertEqual(retrieved_staff.Staff_LName, "Doe")
        # Add more assertions for other attributes

    def test_Skill(self):
        skill = Skill(Skill_Name="Test Skill", Skill_Desc="Test Skill Description")
        db.session.add(skill)
        db.session.commit()

        retrieved_skill = Skill.query.first()
        self.assertEqual(retrieved_skill.Skill_Name, "Test Skill")
        # Add more assertions for other attributes

    def test_Role(self):
        role = Role(Role_Name="Test Role", Role_Department="Test Department")
        db.session.add(role)
        db.session.commit()

        retrieved_role = Role.query.first()
        self.assertEqual(retrieved_role.Role_Name, "Test Role")
        # Add more assertions for other attributes

def test_Role_Skill(self):
        role = Role(Role_Name="Test Role", Role_Department="Test Department")
        skill = Skill(Skill_Name="Test Skill", Skill_Desc="Test Skill Description")

        db.session.add(role)
        db.session.add(skill)
        db.session.commit()

        role_skill = Role_Skill(Role_Name=role.Role_Name, Skill_Name=skill.Skill_Name)
        db.session.add(role_skill)
        db.session.commit()

        retrieved_role_skill = Role_Skill.query.first()
        self.assertEqual(retrieved_role_skill.Role_Name, "Test Role")
        self.assertEqual(retrieved_role_skill.Skill_Name, "Test Skill")
        # Add more assertions for other attributes

    def test_Staff_Skill(self):
        staff = Staff(Staff_FName="John", Staff_LName="Doe", Dept="Test Dept", Country="Test Country", Email="test@example.com")
        skill = Skill(Skill_Name="Test Skill", Skill_Desc="Test Skill Description")

        db.session.add(staff)
        db.session.add(skill)
        db.session.commit()

        staff_skill = Staff_Skill(Staff_ID=staff.Staff_ID, Skill_Name=skill.Skill_Name)
        db.session.add(staff_skill)
        db.session.commit()

        retrieved_staff_skill = Staff_Skill.query.first()
        self.assertEqual(retrieved_staff_skill.Staff_ID, staff.Staff_ID)
        self.assertEqual(retrieved_staff_skill.Skill_Name, "Test Skill")
        # Add more assertions for other attributes

    def test_Staff_Role_Apply(self):
        staff = Staff(Staff_FName="John", Staff_LName="Doe", Dept="Test Dept", Country="Test Country", Email="test@example.com")
        role = Role(Role_Name="Test Role", Role_Department="Test Department")

        db.session.add(staff)
        db.session.add(role)
        db.session.commit()

        staff_role_apply = Staff_Role_Apply(Staff_ID=staff.Staff_ID, Role_ID=role.Role_ID)
        db.session.add(staff_role_apply)
        db.session.commit()

        retrieved_staff_role_apply = Staff_Role_Apply.query.first()
        self.assertEqual(retrieved_staff_role_apply.Staff_ID, staff.Staff_ID)
        self.assertEqual(retrieved_staff_role_apply.Role_ID, role.Role_ID)
        # Add more assertions for other attributes

if __name__ == '__main__':
    unittest.main()