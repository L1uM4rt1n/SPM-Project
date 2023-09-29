from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db = None
# Function to establish the database connection
def connect_to_database():
    global db
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="spm_project"
        )
        return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False

# Check the database connection on application startup
if connect_to_database():
    print("Connected to MySQL database successfully.")
else:
    print("Failed to connect to MySQL database.")

@app.route('/addstaff', methods=['POST'])
def add_staff():
    try:
        cursor = db.cursor()
        data = request.json
        query = "INSERT INTO staff (staff_fname, staff_lname, dept, country, email, access_right) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (data['staff_fname'], data['staff_lname'], data['dept'], data['country'], data['email'], data['access_right']))
        db.commit()
        return jsonify({"message": "Staff added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)