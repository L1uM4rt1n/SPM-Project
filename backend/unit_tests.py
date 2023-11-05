import unittest

from app import AccessRights, Staff, Skill, Role, Role_Skill, Staff_Skill, Staff_Role_Apply
        
class TestAccessRights(unittest.TestCase):
    def test_json(self):
        AR1 = AccessRights(Access_ID = 2 , Access_Control_Name = 'CEO')
        self.assertEqual(AR1.json(), {
            'Access_ID': 2,
            'Access_Control_Name': 'CEO'
        })
        
class TestStaff(unittest.TestCase):
    def test_json(self):
        S1 = Staff(Staff_ID = 1, Staff_FName = 'Martin', Staff_LName = 'Garrix', Dept = 'HR', Country = 'USA', Email = '123@gmail.com', Access_Role = 2, Password = '123')
        self.assertEqual(S1.json(), {
            'Staff_ID': 1,
            'Staff_FName': 'Martin',
            'Staff_LName': 'Garrix',
            'Dept': 'HR',
            'Country': 'USA',
            'Email': '123@gmail.com',
            'Access_Role': 2,
            'Password': '123',
        })
        
class TestSkill(unittest.TestCase):
    def test_json(self):
        Sk1 = Skill(Skill_Name = 'Punch', Skill_Desc = 'punching')
        self.assertEqual(Sk1.json(), {
            'Skill_Name': 'Punch',
            'Skill_Desc': 'punching'
        })
        
class TestRole(unittest.TestCase):
    def test_json(self):
        R1 = Role(Role_ID = 1, Role_Name = 'tester', Role_Department = 'HR', Date_Posted = '2023-11-1', App_Deadline = '2023-11-2', Role_Description = 'testing')
        self.assertEqual(R1.json(), {
            'Role_ID': 1,
            'Role_Name': 'tester',
            'Role_Department': 'HR',
            'Date_Posted': '2023-11-1',
            'App_Deadline': '2023-11-2',
            'Role_Description': 'testing',
        })
        
class TestRoleSkill(unittest.TestCase):
    def test_json(self):
        RS1 = Role_Skill(Role_Name = 'tester', Skill_Name = 'testing')
        self.assertEqual(RS1.json(), {
            'Role_Name': 'tester',
            'Skill_Name': 'testing'
        }) 
        
class TestStaffSkill(unittest.TestCase):
    def test_json(self):
        SS1 = Staff_Skill(Staff_ID = 1, Skill_Name = 'java')
        self.assertEqual(SS1.json(), {
            'Staff_ID': 1,
            'Skill_Name': 'java'
        }) 
        
class TestStaffRoleApply(unittest.TestCase):
    def test_json(self):
        SRA1 = Staff_Role_Apply(Staff_ID = 1, Role_ID = 2)
        self.assertEqual(SRA1.json(), {
            'Staff_ID': 1,
            'Role_ID': 2
        }) 
        
if __name__ == "__main__":
    unittest.main()