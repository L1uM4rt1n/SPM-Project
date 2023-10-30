import unittest

from app import Staff, Skill, Role, Role_Skill, Staff_Skill

class TestStaff(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_staff(self):
        # Your test methods go here
        pass

class TestSkill(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_skill(self):
        # Your test methods go here
        pass

class TestRole(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_role(self):
        # Your test methods go here
        pass


class ViewRoleListing(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Your test methods go here

class EditRoleListing(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Your test methods go here

class ViewApplicants(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Your test methods go here

class SearchRoleListing(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
        # Insert test data into the test database
        # This can include mock job listings for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # Your test methods go here