import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_session import Session
from os import environ
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import logging

app = Flask(__name__)
if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/skills_based_role_portal'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/test_db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/skills_based_role_portal'
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:@localhost:3306/skills_based_role_portal'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8809/skills_based_role_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)
CORS(app)
Session(app)
migrate = Migrate(app, db)

class AccessRights(db.Model):
    __tablename__ = 'AccessRights'

    Access_ID = db.Column(db.Integer, primary_key=True)
    Access_Control_Name = db.Column(db.String(50), nullable=False)

    def __init__(self, Access_ID, Access_Control_Name):
        self.Access_ID = Access_ID
        self.Access_Control_Name = Access_Control_Name
        
    def json(self):
        return {
            'Access_ID': self.Access_ID,
            'Access_Control_Name': self.Access_Control_Name
        }
        
class Staff(db.Model):
    __tablename__ = 'Staff'

    Staff_ID = db.Column(db.Integer, primary_key=True)
    Staff_FName = db.Column(db.String(50), nullable=False)
    Staff_LName = db.Column(db.String(50), nullable=False)
    Dept = db.Column(db.String(50), nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Access_Role = db.Column(db.Integer, db.ForeignKey('AccessRights.Access_ID'))
    Password = db.Column(db.String(50), nullable=True)

    def __init__(self, Staff_ID, Staff_FName, Staff_LName, Dept, Country, Email, Access_Role, Password):
        self.Staff_ID = Staff_ID
        self.Staff_FName = Staff_FName
        self.Staff_LName = Staff_LName
        self.Dept = Dept
        self.Country = Country
        self.Email = Email
        self.Access_Role = Access_Role
        self.Password = Password
        
    def json(self):
        return{
            'Staff_ID': self.Staff_ID,
            'Staff_FName': self.Staff_FName,
            'Staff_LName': self.Staff_LName,
            'Dept': self.Dept,
            'Country': self.Country,
            'Email': self.Email,
            'Access_Role': self.Access_Role,
            'Password': self.Password
        }

class Skill(db.Model):
    __tablename__ = 'Skill'
    
    Skill_Name = db.Column(db.String(50), primary_key=True)
    Skill_Desc = db.Column(db.String(2600), nullable=False)
    
    def __init__(self, Skill_Name, Skill_Desc):
        self.Skill_Name = Skill_Name
        self.Skill_Desc = Skill_Desc
        
    def json(self):
        return{
            'Skill_Name': self.Skill_Name,
            'Skill_Desc': self.Skill_Desc
        }
        
class Role(db.Model):
    __tablename__ = 'Role'

    Role_ID = db.Column(db.Integer, primary_key=True)
    Role_Name = db.Column(db.String(50), nullable=False)
    Role_Department = db.Column(db.String(50), nullable=False)
    Date_Posted = db.Column(db.Date, nullable=False)
    App_Deadline = db.Column(db.Date, nullable=False)
    Role_Description = db.Column(db.String(2600), nullable=False)
    Role_Name_index = db.Index('Role_Name', Role_Name)

    def __init__(self, Role_ID, Role_Name, Role_Department, Date_Posted, App_Deadline, Role_Description):
        self.Role_ID = Role_ID
        self.Role_Name = Role_Name
        self.Role_Department = Role_Department
        self.Date_Posted = Date_Posted
        self.App_Deadline = App_Deadline
        self.Role_Description = Role_Description
        
    def json(self):
        return{
            'Role_ID': self.Role_ID,
            'Role_Name': self.Role_Name,
            'Role_Department': self.Role_Department,
            'Date_Posted': self.Date_Posted,
            'App_Deadline': self.App_Deadline,
            'Role_Description': self.Role_Description
        }
    
class Role_Skill(db.Model):
    __tablename__ = 'Role_Skill'

    Role_Name = db.Column(db.String(50), db.ForeignKey('Role.Role_Name'), primary_key=True)
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'), primary_key=True)

    def __init__(self, Role_Name, Skill_Name):
        self.Role_Name = Role_Name
        self.Skill_Name = Skill_Name

    def json(self):
        return {
            'Role_Name': self.Role_Name,
            'Skill_Name': self.Skill_Name
        }

class Staff_Skill(db.Model):
    __tablename__ = 'Staff_Skill'

    Staff_ID = db.Column(db.Integer, db.ForeignKey('Staff.Staff_ID'), primary_key=True)
    Skill_Name = db.Column(db.String(50), db.ForeignKey('Skill.Skill_Name'), primary_key=True)

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

    def __init__(self, Staff_ID, Role_ID):
        self.Staff_ID = Staff_ID
        self.Role_ID = Role_ID
        
    def json(self):
        return{
            'Staff_ID': self.Staff_ID,
            'Role_ID': self.Role_ID
        }

################ 5 role endpoints ##################################################

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

    if (results):
        return jsonify(
            {
                "code": 200,
                "data": results
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 404,
                "message": "No results found."
            }
        ), 404

# for staff to view individual role details
@app.route('/role/view_role', methods=['GET'])
def get_role_details():
    role_id = request.args.get('role_id')
    role = Role.query.filter_by(Role_ID=role_id).first()
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

# to validate date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
# for HR to create a new role
@app.route('/role/create', methods=['POST'])
def create_role():
    data = request.get_json()
    # check NOTNULL condition
    required_fields = ['Role_Name', 'Role_Department', 'Date_Posted', 'App_Deadline', 'Role_Description', 'Role_Skills']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify(
            {
                "code": 400, 
                "message": f"Missing required fields: {', '.join(missing_fields)}"
            }
        ), 400

    # check date format
    date_fields = ['Date_Posted', 'App_Deadline']
    date_errors = [field for field in date_fields if not is_valid_date(data.get(field, ''))]
    if date_errors:
        return jsonify(
            {
                "code": 400, 
                "message": f"Invalid date format for {', '.join(date_errors)}. Please use the format: YYYY-MM-DD."
            }
        ), 400

    # check if role already exists
    role_name = data['Role_Name']
    existing_role = Role.query.filter_by(Role_Name=role_name).first()
    if existing_role:
        return jsonify(
            {
                "code": 400,
                "message": "Role with this name already exists!"
            }
        ), 400
        
    try:
        # create new role
        role_id = generate_unique_role_id()
        new_role_data = {key: data[key] for key in data if key != 'Role_Skills'}
        new_role = Role(Role_ID=role_id, **new_role_data)
        db.session.add(new_role)
        
        # create role_skill entries
        role_skills = []
        for skill_name in data['Role_Skills']:
            role_skill = Role_Skill(Role_Name=role_name, Skill_Name=skill_name)
            db.session.add(role_skill)
            role_skills.append(skill_name)
            
        db.session.commit()
        response_data = new_role.json()
        response_data['Role_Skills'] = role_skills
        return jsonify(
            {
                "code": 201,
                "data": response_data, 
                "message": "Role listing created successfully."
            }
        ), 201
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify(
            {
                "code": 409,
                "message": "Integrity violation: " + str(integrity_error)
            }
        ), 409
    except ValueError as value_error:
        db.session.rollback()
        return jsonify(
            {
                "code": 400,
                "message": "Invalid value: " + str(value_error)
            }
        ), 400
    # pylint: disable=W0718
    except Exception as error:
        db.session.rollback()
        return jsonify(
            {
                'code': 500,
                'error': str(error)
            }
        ), 500
    # pylint: enable=W0718

# for HR to update role
@app.route('/role/update', methods=['PUT'])
def update_role():
    role_id = request.args.get('role_id')
    role = Role.query.get(role_id)
    if not role:
        return jsonify(
            {
                'code': 404,
                'message': 'Role not found'
            }
        ), 404

    data = request.get_json()
    new_role_name = data.get('Role_Name', role.Role_Name)

    # check date format before processing
    date_fields = ['Date_Posted', 'App_Deadline']
    date_errors = [field for field in date_fields if field in data and not is_valid_date(data[field])]
    if date_errors:
        return jsonify(
            {
                'code': 400,
                'message': f'Invalid date format for {", ".join(date_errors)}. Please use the format: YYYY-MM-DD.'
            }
        ), 400

    # if role name has changed, create a new role & transfer data
    # to avoid IntegrityError due to role_skill table
    if new_role_name != role.Role_Name:
        # update role table
        new_role = Role(
            Role_ID=generate_unique_role_id(),
            Role_Name=new_role_name,
            **{key: data.get(key, getattr(role, key)) for key in Role.__table__.columns.keys() if key != 'Role_ID'  and key != 'Role_Name'},
        )

        skills = data.get('Role_Skills', [])
        db.session.query(Role_Skill).filter_by(Role_Name=role.Role_Name).delete()
        db.session.add(new_role)
        # update skill table
        for skill_name in skills:
            db.session.add(Role_Skill(Role_Name=new_role.Role_Name, Skill_Name=skill_name))

        db.session.delete(role)
        db.session.commit()
        return jsonify(
            {
                'code': 201,
                'message': f'Role updated successfully, new Role_ID ({new_role.Role_ID}) generated\
                as Role_Name has changed. Old role has been deleted.'
            }
        ), 201
    else:
        for key in Role.__table__.columns.keys():
            if key != 'Role_ID':
                setattr(role, key, data.get(key, getattr(role, key)))

        skills = data.get('Role_Skills', [])
        db.session.query(Role_Skill).filter_by(Role_Name=role.Role_Name).delete()

        for skill_name in skills:
            db.session.add(Role_Skill(Role_Name=role.Role_Name, Skill_Name=skill_name))

        db.session.commit()
        return jsonify(
            {
                'code': 200,
                'message': 'Role updated successfully.'
            }
        ), 200


########################## 5 staff endpoints #########################################
# to generate Staff_ID
def generate_unique_staff_id():
    current_year = datetime.now().year % 100
    max_existing_staff = db.session.query(db.func.max(Staff.Staff_ID)).scalar()
    next_staff_id = (current_year * 10000 + 1) if max_existing_staff is None \
            else max(max_existing_staff + 1, current_year * 10000 + 1)
    return next_staff_id

# to create new staff
@app.route('/staff/create', methods=['POST'])
def create_staff():
    data = request.get_json()
    required_fields = ['Staff_FName', 'Staff_LName', 'Dept', 'Country', 'Email', 'Access_Role']

    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify(
            {
                "code": 400,
                "message": f"Missing required fields: {', '.join(missing_fields)}"
            }
        ), 400

    try:
        staff_fname = data['Staff_FName']
        staff_lname = data['Staff_LName']
        dept = data['Dept']
        country = data['Country']
        email = data['Email']
        Access_Role = data['Access_Role']
        # no need password to be sent, null values allowed
        # if existing staff, it'll be retrieved from db
        # else, staff can set his own password later
    except KeyError as key_error:
        return jsonify(
            {
                "code": 400,
                "message": f"Missing required field: {str(key_error)}"
            }
        ), 400
    except ValueError as value_error:
        return jsonify(
            {
                "code": 400,
                "message": f"Invalid value for field: {str(value_error)}"
            }
        ), 400

    staff_id = generate_unique_staff_id()
    existing_staff_email = Staff.query.filter_by(Email=email).first()
    if existing_staff_email:
        # check if staff member, with ALL exact details, already exists
        if (
            existing_staff_email.Staff_FName == staff_fname and
            existing_staff_email.Staff_LName == staff_lname and
            existing_staff_email.Dept == dept and
            existing_staff_email.Country == country and
            existing_staff_email.Access_Role == Access_Role
        ):
            return jsonify(
                {
                    "code": 400,
                    "message": "Staff member with the same attributes already exists!"
                }
            ), 400
        else:
            Password = existing_staff_email.Password
    else:
        Password = None

    new_staff = Staff(
        Staff_ID=staff_id,
        Staff_FName=staff_fname,
        Staff_LName=staff_lname,
        Dept=dept,
        Country=country,
        Email=email,
        Access_Role=Access_Role,
        Password=Password
    )
    
    try:
        db.session.add(new_staff)
        db.session.commit()
    except IntegrityError as integrity_error:
        db.session.rollback()
        return jsonify(
            {
                "code": 409,
                "message": "Integrity violation: " + str(integrity_error)
            }
        ), 409
    # pylint: disable=W0718
    except Exception as error:
        db.session.rollback()
        logging.error("An error occurred: %s", str(error))
        return jsonify({
            'message': 'An error occurred while creating the role listing. Please try again later.'
            }
        ), 500
    # pylint: enable=W0718

    return jsonify(
        {
            "code": 202,
            "data": new_staff.json(),
            "message": "Staff member created successfully"
        }
    ), 202

# get staff profile, including staff skill
@app.route('/staff/get_profile', methods=['GET'])
def get_staff_profile():
    staff_id = request.args.get('staff_id')
    staff = Staff.query.get(staff_id)
    if not staff:
        return jsonify(
            {
                'code': 404,
                'message': 'Staff not found'
            }
        ), 404

    staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff_id).all()
    staff_details = staff.json()
    staff_details['Staff_Skills'] = [staff_skill.Skill_Name for staff_skill in staff_skills]

    return jsonify(
        {
            
            'code': 200,
            'staff_profile': staff_details
        }
    ), 200


# to calculate the percentage skills matched for 2 endpoints
def calculate_percentage_matched(staff_skills, role_skills):
    matched_skills = set(staff_skill.Skill_Name for staff_skill in staff_skills).intersection(
        set(role_skill.Skill_Name for role_skill in role_skills))

    total_skills = len(role_skills)
    if total_skills == 0:
        return 0
    
    percentage_matched = (len(matched_skills) / total_skills) * 100
    formatted_percentage = f"{round(percentage_matched, 2)}%"
    return formatted_percentage

# for Staff, to calculate Role-Skill % Match & display matched & skills gap for all roles
@app.route('/staff/role-matches', methods=['GET'])
def calculate_role_matches():
    staff_id = request.args.get('staff_id')
    staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff_id).all()
    if not staff_skills:
        return jsonify(
            {
                'code': 404,
                'message': 'Staff member not found or has no skills'
            }
        ), 404
        
    role_matches = []
    roles = Role.query.all()
    for role in roles:
        role_skills = Role_Skill.query.filter_by(Role_Name=role.Role_Name).all()
        matched_skills = set(staff_skill.Skill_Name for staff_skill in staff_skills).intersection(
            set(role_skill.Skill_Name for role_skill in role_skills))
        
        percentage_matched = calculate_percentage_matched(staff_skills, role_skills)
        if isinstance(percentage_matched, int):
            formatted_percentage = "0%"
        else:
            formatted_percentage = percentage_matched
        gap_skills = set(role_skill.Skill_Name for role_skill in role_skills) - matched_skills
        
        role_matches.append({
            'Role_Name': role.Role_Name,
            'Percentage_Matched': formatted_percentage,
            'Skills_Matched': list(matched_skills),
            'Skills_Gap': list(gap_skills)
        })
    role_matches.sort(key=lambda x: float(x['Percentage_Matched'].strip('%')), reverse=True)

    return jsonify(
        {
            'code': 200,
            'data': role_matches
        }
    ), 200

# for HR to view skills (& details) of role applicants
@app.route('/role_application/view_applicants', methods=['GET'])
def get_role_applicants_skills():
    role_name = request.args.get('role_name')
    role_skills = Role_Skill.query.filter_by(Role_Name=role_name).all()
    role = Role.query.filter_by(Role_Name=role_name).first()
    if not role:
        return jsonify(
            {
                'code': 404,
                'message': 'Role not found'
            }
        ), 404

    role_applicants = (
        db.session.query(Staff, Staff_Role_Apply)
        .join(Staff_Role_Apply, Staff_Role_Apply.Staff_ID == Staff.Staff_ID)
        .filter(Staff_Role_Apply.Role_ID == role.Role_ID)
        .all()
    )
    # print(role_applicants)
    if not role_applicants:
        return jsonify(
            {
                'code': 404,
                'message': 'No applicants for this role'
            }
        ), 404
        
    applicant_details = []
    for staff, apply in role_applicants:
        staff_skills = Staff_Skill.query.filter_by(Staff_ID=staff.Staff_ID).all()
        percentage_matched = calculate_percentage_matched(staff_skills, role_skills)
        applicant_details.append(
            {
                'Applicant_ID': staff.Staff_ID,
                'Applicant_Email': staff.Email,
                'Applicant_Department': staff.Dept,
                'Applicant_Country': staff.Country,
                'Applicant_Name': f'{staff.Staff_FName} {staff.Staff_LName}',
                'Applicant_Skills': [s.Skill_Name for s in staff_skills],
                'Applicant_Skills_Percentage_Matched': percentage_matched
            }
        )
        
    return jsonify(
        {
            'code': 200,
            'data': applicant_details
        }
    ), 200

# when Staff applies for role
@app.route('/staff/submit_application', methods=['POST'])
def submit_application():
    # staff_id = 140008
    staff_id = request.args.get('staff_id') # make sure to pass in the staff_id to the endpoint, based on user session
    ##################### check how to retrieve
    # staff_id = session.get('staff_id')
    role_id = request.form.get('role_id')
    # role_id = 1000004
    # check if staff has already applied for this role
    existing_application = Staff_Role_Apply.query.filter_by(
        Staff_ID=staff_id,
        Role_ID=role_id
    ).first()

    if existing_application:
        return "You have already applied for this role."

    new_application = Staff_Role_Apply(
        Staff_ID=staff_id,
        Role_ID=role_id
    )

    db.session.add(new_application)
    db.session.commit()

    role = Role.query.filter_by(Role_ID=role_id).first()
    db.session.commit()
    
    # after this, code the js to change status bar to 'Applied', since there's a entry in
    # staff_role_apply table => means staff has applied for the role

    return "Application submitted successfully."

# for staff to view all roles they have applied for
@app.route('/staff/applied_roles', methods=['GET'])
def get_applied_roles():
    staff_id = request.args.get('staff_id')
    applied_roles = Staff_Role_Apply.query.filter_by(Staff_ID=staff_id).all()
    if not applied_roles:
        return jsonify(
            {
                'code': 404,
                'message': 'You have not applied for any roles yet.'
            }
        ), 404

    results = []
    for applied_role in applied_roles:
        role = Role.query.get(applied_role.Role_ID)
        role_skills = Role_Skill.query.filter_by(Role_Name=role.Role_Name).all()
        role_details = role.json()
        role_details['Role_Skills'] = [role_skill.Skill_Name for role_skill in role_skills]
        results.append(role_details)

    return jsonify(
        {
            'code': 200,
            'data': results
        }
    ), 200


######################## skill endpoint ###################################
# get all skill names
@app.route('/skills/get_all_skills', methods=['GET'])
def get_all_skills():
    skill_names = [skill.Skill_Name for skill in Skill.query.all()]
    return jsonify(
            {
                "code": 200,
                "data": {
                    "skill_names": skill_names
                }
            }
        ), 200
    
################ login endpoints ##################################################

# for staff to login
@app.route('/login', methods=['POST'])
def login():
    try: 
        data = request.get_json()
        email = data['Email']
        password = data['Password']
        access_role = data['Access_Role']

        staff = Staff.query.filter_by(Email=email).first()
        if not staff:
            return jsonify(
                {
                    'code': 404,
                    'message': 'Staff member not found'
                }
            ), 404

        if staff.Password != password:
            return jsonify(
                {
                    'code': 401,
                    'message': 'Incorrect password'
                }
            ), 401

        if access_role == 'HR':
            if staff.Access_Role != 4:
                return jsonify(
                    {
                        'code': 401,
                        'message': 'Staff has no HR Rights'
                    }
                ), 401

        elif access_role == 'Staff':
            if staff.Access_Role != 2:
                return jsonify(
                    {
                        'code': 401,
                        'message': 'HR has no Staff Rights'
                    }
                ), 401

        return jsonify(
            {
                'code': 200,
                'message': 'Login successful',
                'data': staff.json()
            }
        ), 200
    except KeyError as key_error:
        return jsonify({'message': str(key_error)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# for validation of email if in database
@app.route('/validate-email', methods=['POST'])
def validate_email():
    try:
        data = request.get_json()
        email = data['email']
        staff = Staff.query.filter_by(Email=email).first()
        if staff:
            return jsonify({'valid': True}), 200
        else:
            return jsonify({'valid': False}), 200
    except KeyError as key_error:
        return jsonify({'message': str(key_error)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# for validation of password if in database
@app.route('/validate-password', methods=['POST'])
def validate_password():
    try:
        data = request.get_json()
        password = data['password']
        staff = Staff.query.filter_by(Password=password).first()
        if staff:
            return jsonify({'valid': True}), 200
        else:
            return jsonify({'valid': False}), 200
    except KeyError as key_error:
        return jsonify({'message': str(key_error)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)
