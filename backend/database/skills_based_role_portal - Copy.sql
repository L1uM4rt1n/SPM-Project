GRANT FILE ON *.* TO 'root'@'127.0.0.1';

CREATE DATABASE IF NOT EXISTS skills_based_role_portal;
USE skills_based_role_portal;

DROP TABLE IF EXISTS Staff_Role_Apply;
DROP TABLE IF EXISTS Staff_Skill;
DROP TABLE IF EXISTS Role_Skill;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Skill;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS Access_Control;


-- ACCESS RIGHTS --------------------------------
CREATE TABLE IF NOT EXISTS Access_Control (
    Access_ID INT PRIMARY KEY,
    Access_Control_Name VARCHAR(50) NOT NULL
);

LOAD DATA INFILE './customer_csv_files/Final_Access_Control.csv'
INTO TABLE Access_Control
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Access_ID, Access_Control_Name);


-- STAFF DETAILS --------------------------------
CREATE TABLE IF NOT EXISTS Staff (
    Staff_ID INT PRIMARY KEY,
    Staff_FName VARCHAR(50) NOT NULL,
    Staff_LName VARCHAR(50) NOT NULL,
    Dept VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE NOT NULL,
    Access_Role INT,
    FOREIGN KEY (Access_Role) REFERENCES Access_Control(Access_ID)
);

LOAD DATA INFILE './customer_csv_files/Final_Staff.csv'
INTO TABLE Staff
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Staff_ID, Staff_FName, Staff_LName, Dept, Country, Email, Access_Role);


-- SKILL DETAILS --------------------------------
CREATE TABLE IF NOT EXISTS Skill (
    Skill_Name VARCHAR(50) PRIMARY KEY,
    Skill_Desc VARCHAR(2600) NOT NULL
);

LOAD DATA INFILE './customer_csv_files/Final_Skill.csv'
INTO TABLE Skill
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Skill_Name, Skill_Desc);


-- ROLE/ JOB LISTING --------------------------------
CREATE TABLE IF NOT EXISTS Role (
    Role_ID INT PRIMARY KEY,
    Role_Name VARCHAR(50) NOT NULL,
    Role_Department VARCHAR(50) NOT NULL,
    Date_Posted DATE NOT NULL,
    App_Deadline DATE NOT NULL,
    Role_Description VARCHAR(2600) NOT NULL,
    INDEX (Role_Name)
);

LOAD DATA INFILE './customer_csv_files/Final_Role.csv'
INTO TABLE Role
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Role_ID, Role_Name, Role_Department, Date_Posted, App_Deadline, Role_Description);


-- SKILLS REQ OF A ROLE --------------------------------
CREATE TABLE IF NOT EXISTS Role_Skill (
    Role_Name VARCHAR(50),
    Skill_Name VARCHAR(50),
    PRIMARY KEY (Role_Name, Skill_Name),
    FOREIGN KEY (Role_Name) REFERENCES Role(Role_Name),
    FOREIGN KEY (Skill_Name) REFERENCES Skill(Skill_Name)
    -- INDEX (Skill_Name)
);

LOAD DATA INFILE './customer_csv_files/Final_Role_Skill.csv'
INTO TABLE Role_Skill
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Role_Name, Skill_Name);


-- STAFF SKILLS --------------------------------
CREATE TABLE IF NOT EXISTS Staff_Skill (
    Staff_ID INT,
    Skill_Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Staff_ID, Skill_Name),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Skill_Name) REFERENCES Skill(Skill_Name)
);

LOAD DATA INFILE './customer_csv_files/Final_Staff_Skill.csv'
INTO TABLE Staff_Skill
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(Staff_ID, Skill_Name);


-- Staff Role Apply --------------------------------
CREATE TABLE IF NOT EXISTS Staff_Role_Apply (
    Staff_ID INT,
    Role_ID INT,
    Applied VARCHAR(1) NOT NULL,
    PRIMARY KEY (Staff_ID, Role_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Role_ID) REFERENCES Role(Role_ID)
);

-- INSERT INTO Staff_Role_Apply (Staff_ID, Role_ID, Applied)
-- VALUES
--     (4, 1000004, '1');
-- COMMIT;