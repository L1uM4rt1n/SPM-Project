import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from os import environ
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/skills_based_role_portal'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/skills_based_role_portal'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/skills_based_role_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)
CORS(app)
Session(app)
migrate = Migrate(app, db)

class AccessRights(db.Model):
    __tablename__ = 'AccessRights'

    Access_Rights_ID = db.Column(db.Integer, primary_key=True)
    Access_Rights_Label = db.Column(db.String(50), nullable=False)

    def __init__(self, Access_Rights_ID, Access_Rights_Label):
        self.Access_Rights_ID = Access_Rights_ID
        self.Access_Rights_Label = Access_Rights_Label
        
    def json(self):
        return {
            'Access_Rights_ID': self.Access_Rights_ID,
            'Access_Rights_Label': self.Access_Rights_Label
        }
        
class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Access_Rights = db.Column(db.Integer, db.ForeignKey('AccessRights.Access_Rights_ID'))
    Password = db.Column(db.String(50), nullable=False)

    def __init__(self, Staff_FName, Staff_LName, Dept, Country, Email, Access_Rights, Password):
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Country = Country
        self.Email = Email
        self.Access_Rights = Access_Rights
        self.Password = Password

    def json(self):
        return{
            'Staff_FName': self.Staff_FName,
            'Staff_LName': self.Staff_LName,
            'Dept': self.Dept,
            'Country': self.Country,
            'Email': self.Email,
            'Access_Rights': self.Access_Rights,
            'Password': self.Password
        }

class Role(db.Model):
    __tablename__ = 'Role'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50), nullable=False)
    Date_Posted = db.Column(db.Date, nullable=False)
    App_Deadline = db.Column(db.Date, nullable=False)
    Role_Department = db.Column(db.String(50), nullable=False)
    Role_Description = db.Column(db.String(2600), nullable=False)
    Role_Requirements = db.Column(db.String(2600), nullable=False)
    Availability = db.Column(db.Integer, nullable=False)
    Role_Name_index = db.Index('Role_Name', Role_Name)

    def __init__(self, Role_ID, Role_Name, Date_Posted, App_Deadline, Role_Department, Role_Description, Role_Requirements, Availability):
        self.Role_ID = Role_ID
        self.Role_Name = Role_Name
        self.Date_Posted = Date_Posted
        self.App_Deadline = App_Deadline
        self.Role_Department = Role_Department
        self.Role_Description = Role_Description
        self.Role_Requirements = Role_Requirements
        self.Availability = Availability
        
    def json(self):
        return{
            'Role_ID': self.Role_ID,
            'Role_Name': self.Role_Name,
            'Date_Posted': self.Date_Posted,
            'App_Deadline': self.App_Deadline,
            'Role_Department': self.Role_Department,
            'Role_Description': self.Role_Description,
            'Role_Requirements': self.Role_Requirements,
            'Availability': self.Availability
        }
    
class Role_Skill(db.Model):
    __tablename__ = 'Role_Skill'

    Role_Name = db.Column(db.String(50), db.ForeignKey('Role.Role_Name'), primary_key=True)
    Skill_Name = db.Column(db.String(50), primary_key=True)
    Skill_Name_index = db.Index('Skill_Name', Skill_Name)
    
    def __init__(self, Role_Name, Skill_Name):
        self.Role_Name = Role_Name
        self.Skill_Name = Skill_Name
        
    def json(self):
        return{
            'Role_Name': self.Role_Name,
            'Skill_Name': self.Skill_Name
        }

class Staff_Skill(db.Model):
    __tablename__ = 'Staff_Skill'

    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'), primary_key=True)
    Skill_Name = db.Column(db.String(50), primary_key=True)

    def __init__(self, Staff_ID, Skill_Name):
        self.Staff_ID = Staff_ID
        self.Skill_Name = Skill_Name
        
    def json(self):
        return{
            'Staff_ID': self.Staff_ID,
            'Skill_Name': self.Skill_Name
        }
    
class Staff_Role_Apply(db.Model):
    __tablename__ = 'Staff_Role_Apply'

    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'), primary_key=True)
    Role_ID = db.Column(db.Integer, db.ForeignKey('Role.Role_ID'), primary_key=True)
    Applied = db.Column(db.String(1), nullable=False)

    def __init__(self, Staff_ID, Role_ID, Applied):
        self.Staff_ID = Staff_ID
        self.Role_ID = Role_ID
        self.Applied = Applied
        
    def json(self):
        return{
            'Staff_ID': self.Staff_ID,
            'Role_ID': self.Role_ID,
            'Applied': self.Applied
        }
################ login endpoints ##################################################

# for staff to login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['Email']
    password = data['Password']
    access_rights = data['Access_Rights']

    staff = Staff.query.filter_by(Email=email).first()
    if not staff:
        return jsonify({'message': 'Staff member not found'}), 404

    if staff.Password != password:
        return jsonify({'message': 'Incorrect password'}), 401

    if access_rights == 'HR':
        access_rights = 1
    elif access_rights == 'Staff':
        access_rights = 2

    #staff.Access_Rights = 1 can access HR and Staff pages
    #staff.Access_Rights = 2 can only access Staff pages

    if access_rights == 1 and staff.Access_Rights != 1:
        return jsonify({'message': 'Restricted Access'}), 401

    
    session['staff_id'] = staff.Staff_ID
    session['access_rights'] = staff.Access_Rights

    return jsonify(staff.json()), 200


################ role endpoints ##################################################

# for staff to read/view all roles
@app.route('/roles/get_all_roles', methods=['GET'])
def get_all():
    role_list = Role.query.all()
    roles_with_details = []
    for role in role_list:
        role_skills = Role_Skill.query.filter_by(Role_Name=role.Role_Name).all()
        role_data = role.json()
        role_data['Role_Skills'] = [role_skill.Skill_Name for role_skill in role_skills]
        roles_with_details.append(role_data)

    if len(roles_with_details) > 0:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "roles_with_details": roles_with_details
                }
            }
        ), 200
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles available."
        }
    ), 404

# for staff to search for specific role (browse & filter)
@app.route('/roles/search', methods=['GET'])
def search_roles():
    search_term = request.args.get('search_query', '')
    roles = Role.query.filter(
        (Role.Role_Name.ilike(f"%{search_term}%")) |
        (Role.Role_Description.ilike(f"%{search_term}%"))
    ).all()

    results = [role.json() for role in roles]

    return jsonify(results)

# for staff to view individual role details
@app.route('/role/<int:Role_ID>', methods=['GET'])
def get_role_details(Role_ID):
    role = Role.query.filter_by(Role_ID=Role_ID).first()
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    role_skills = Role_Skill.query.filter_by(Role_Name=role.Role_Name).all()
    role_details = role.json()
    role_details['Role_Skills'] = [role_skill.Skill_Name for role_skill in role_skills]

    return jsonify(role_details)


# to generate Role_ID
def generate_unique_role_id():
    max_existing_role = db.session.query(db.func.max(Role.Role_ID)).scalar()
    if max_existing_role is None:
        return 1000001
    next_role_id = max_existing_role + 1
    return next_role_id

# for HR to create new role
@app.route('/roles/create', methods=['POST'])
def create_role():
    data = request.get_json()
    
    try:
        role_name = data['Role_Name']
        date_posted = data['Date_Posted']
        app_deadline = data['App_Deadline']
        role_department = data['Role_Department']
        role_description = data['Role_Description']
        role_requirements = data['Role_Requirements']
        availability = data['Availability']
    except KeyError as e:
        return jsonify(
            {
                "code": 400,
                "message": f"Missing required field: {str(e)}"
            }
        ), 400
    except ValueError as e:
        return jsonify(
            {
                "code": 400,
                "message": f"Invalid value for field: {str(e)}"
            }
        ), 400

    # Check if the role already exists by name
    if Role.query.filter_by(Role_Name=role_name).first():
        return jsonify(
            {
                "code": 400,
                "message": "Role with this name already exists!"
            }
        ), 400

    # If the role doesn't exist, insert it into the database
    role_id = generate_unique_role_id()
    new_role = Role(
        Role_ID=role_id,
        Role_Name=role_name,
        Date_Posted=date_posted,
        App_Deadline=app_deadline,
        Role_Department=role_department,
        Role_Description=role_description,
        Role_Requirements=role_requirements,
        Availability=availability
    )

    try:
        db.session.add(new_role)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 409,
                "message": "Integrity violation: " + str(e)
            }
        ), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_role.json(),
            "message": "Role listing created successfully"
        }
    ), 201

# for HR to update role
@app.route('/role/update/<int:role_id>', methods=['PUT'])
def update_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    # link data to frontend to pass info
    data = request.get_json()
    role.Role_Name = data['Role_Name']
    role.Date_Posted = data['Date_Posted']
    role.App_Deadline = data['App_Deadline']
    role.Role_Department = data['Role_Department']
    role.Role_Description = data['Role_Description']
    role.Role_Requirements = data['Role_Requirements']
    role.Availability = data['Availability']

    skills = data.get('Role_Skills', [])  # assuming Role_Skills is a list of skill names
    # clear existing role skills
    Role_Skill.query.filter_by(Role_Name=role.Role_Name).delete()
    # add updated role skills
    for skill_name in skills:
        role_skill = Role_Skill(Role_Name=role.Role_Name, Skill_Name=skill_name)
        db.session.add(role_skill)

    db.session.commit()

    return jsonify({'message': 'Role updated successfully'}), 200


##########################3 staff endpoints #########################################

# to create new staff
@app.route('/staff/create', methods=['POST'])
def create_staff():
    data = request.get_json()

    try:
        staff_fname = data['Staff_FName']
        staff_lname = data['Staff_LName']
        dept = data['Dept']
        country = data['Country']
        email = data['Email']
        access_rights = data['Access_Rights']
    except KeyError as e:
        return jsonify(
            {
                "code": 400,
                "message": f"Missing required field: {str(e)}"
            }
        ), 400
    except ValueError as e:
        return jsonify(
            {
                "code": 400,
                "message": f"Invalid value for field: {str(e)}"
            }
        ), 400

    # Check if staff member already exists by email
    if Staff.query.filter_by(Email=email).first():
        return jsonify(
            {
                "code": 400,
                "message": "Staff member with this email already exists!"
            }
        ), 400

    # If staff member doesn't exist, insert into the database
    new_staff = Staff(
        Staff_FName=staff_fname,
        Staff_LName=staff_lname,
        Dept=dept,
        Country=country,
        Email=email,
        Access_Rights=access_rights
    )
    
    try:
        db.session.add(new_staff)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        return jsonify(
            {
                "code": 409,
                "message": "Integrity violation: " + str(e)
            }
        ), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 202,
            "data": new_staff.json(),
            "message": "Staff member created successfully"
        }
    ), 202

# for HR to view skills of role applicants
@app.route('/role/<string:role_name>/applicants/skills', methods=['GET'])
def get_role_applicants_skills(role_name):
    # find Role_ID based on role name
    role = Role.query.filter_by(Role_Name=role_name).first()
    if not role:
        return jsonify({'message': 'Role not found'}), 404

    # get staff members who applied for specified role
    role_applicants = Staff_Role_Apply.query.filter_by(Role_ID=role.Role_ID).all()
    if not role_applicants:
        return jsonify({'message': 'No applicants for this role'}), 404

    # retrieve the skills of the applicants
    applicant_skills = []
    for applicant in role_applicants:
        staff_member = Staff.query.get(applicant.Staff_ID)
        staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff_member.Staff_ID).all()
        applicant_skills.append({'Staff_Name': f'{staff_member.Staff_FName} {staff_member.Staff_LName}', 'Skills': [skill.Skill_Name for skill in staff_skills]})

    return jsonify(applicant_skills)

# for Staff, to calculate Role-Skill % Match & display matched & skills gap
@app.route('/staff/<int:staff_id>/role-matches', methods=['GET'])
def calculate_role_matches(staff_id):
    staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff_id).all()
    if not staff_skills:
        return jsonify({'message': 'Staff member not found or has no skills'}), 404
    
    role_matches = []
    roles = Role.query.all()
    for role in roles:
        role_skills = Role_Skill.query.filter_by(Role_Name=role.Role_Name).all()
        matched_skills = set(staff_skill.Skill_Name for staff_skill in staff_skills).intersection(
            set(role_skill.Skill_Name for role_skill in role_skills))

        total_skills = len(role_skills)
        if total_skills == 0:
            percentage_matched = 0
        else:
            percentage_matched = (len(matched_skills) / total_skills) * 100

        gap_skills = set(role_skill.Skill_Name for role_skill in role_skills) - matched_skills
        
        role_matches.append({
            'Role_Name': role.Role_Name,
            'Percentage_Matched': percentage_matched,
            'Skills_Matched': list(matched_skills),
            'Skills_Gap': list(gap_skills)
        })
    role_matches.sort(key=lambda x: x['Percentage_Matched'], reverse=True)

    return jsonify(role_matches)

# when Staff applies for role
@app.route('/staff/submit_application', methods=['POST'])
def submit_application():
    staff_id = 3  # discuss how to fetch the staff ID based on the user#######################################
    role_id = request.form.get('role')
    # role_id = 1000003
    # check if staff has already applied for this role
    existing_application = Staff_Role_Apply.query.filter_by(
        Staff_ID=staff_id,
        Role_ID=role_id
    ).first()

    if existing_application:
        return "You have already applied for this role."

    new_application = Staff_Role_Apply(
        Staff_ID=staff_id,
        Role_ID=role_id,
        Applied='1'
    )

    db.session.add(new_application)
    db.session.commit()

    role = Role.query.filter_by(Role_ID=role_id).first()
    role.Availability -= 1
    db.session.commit()
    
    # after this, code the js to change status bar to 'Applied', since there's a entry in
    # staff_role_apply table => means staff has applied for the role

    return "Application submitted successfully."



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)