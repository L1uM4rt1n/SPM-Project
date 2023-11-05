import pytest
import sqlite3
from your_project import create_app, db  # Adjust the import path

# Define a fixture to set up your test environment
@pytest.fixture(scope='module')
def app():
    # Create the app with the 'testing' configuration
    app = create_app(config_name='testing')
    app_context = app.app_context()
    app_context.push()

    # Create a test database by executing the SQL script
    test_db_filename = 'test.db'
    script_filename = 'test.sql'

    conn = sqlite3.connect(test_db_filename)
    cursor = conn.cursor()
    with open(script_filename, 'r') as script_file:
        cursor.executescript(script_file.read())
    conn.commit()
    conn.close()

    # Set up the database URI for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{test_db_filename}'

    # Establish the application context for testing
    with app.test_request_context():
        yield app  # Yield the app as a fixture

    # Teardown: Remove the test database and app context
    os.remove(test_db_filename)
    app_context.pop()

# Optionally, you can define other fixtures or test configuration options here
