SET @csv_directory = (SELECT @@secure_file_priv);
SELECT @csv_directory;
-- see your directory, then move cleaned_csv_folders into that directory

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

LOAD DATA LOCAL INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/databasecleaned_csv_files/Final_Access_Control.csv'
INTO TABLE Access_Control
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Access_ID, Access_Control_Name);


-- STAFF DETAILS --------------------------------
CREATE TABLE IF NOT EXISTS Staff (
    Staff_ID INT PRIMARY KEY,
    Staff_FName VARCHAR(50) NOT NULL,
    Staff_LName VARCHAR(50) NOT NULL,
    Dept VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Email VARCHAR(50) NOT NULL,
    Access_Role INT,
    Password VARCHAR(50),
    FOREIGN KEY (Access_Role) REFERENCES Access_Control(Access_ID)
);

LOAD DATA  LOCAL INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/database/cleaned_csv_files/Final_Skill.csv'
INTO TABLE Staff
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Staff_ID, Staff_FName, Staff_LName, Dept, Country, Email, Access_Role, Password);

-- SKILL DETAILS --------------------------------
CREATE TABLE IF NOT EXISTS Skill (
    Skill_Name VARCHAR(50) PRIMARY KEY,
    Skill_Desc VARCHAR(2600) NOT NULL
);

LOAD DATA LOCAL INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/database/cleaned_csv_files/Final_Skill.csv'
INTO TABLE Skill
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
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

LOAD DATA INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/database/cleaned_csv_files/Final_Role.csv'
INTO TABLE Role
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '\\'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
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

LOAD DATA  LOCAL INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/database/cleaned_csv_files/Final_Role_Skill.csv'
INTO TABLE Role_Skill
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Role_Name, Skill_Name);


-- STAFF SKILLS --------------------------------
CREATE TABLE IF NOT EXISTS Staff_Skill (
    Staff_ID INT,
    Skill_Name VARCHAR(50),
    PRIMARY KEY (Staff_ID, Skill_Name),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Skill_Name) REFERENCES Skill(Skill_Name)
);

LOAD DATA LOCAL INFILE '/Users/tanshanmei/Downloads/IS212 - Software Project Management/project/SPM-Project/SPM-Project/backend/database/cleaned_csv_files/Final_Staff_Skill.csv'
INTO TABLE Staff_Skill
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES
(Staff_ID, Skill_Name);


-- Staff Role Apply --------------------------------
CREATE TABLE IF NOT EXISTS Staff_Role_Apply (
    Staff_ID INT,
    Role_ID INT,
    PRIMARY KEY (Staff_ID, Role_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Role_ID) REFERENCES Role(Role_ID)
);

INSERT INTO Staff_Role_Apply (Staff_ID, Role_ID)
VALUES
    (210039, 1000005),
    (210040, 1000005),
    (210041, 1000005),
    (210042, 1000005),
    (210043, 1000005),
    (210040, 1000015),
    (140003, 1000015),
    (130001, 1000001),
    (130002, 1000002),
    (140001, 1000003),
    (140002, 1000004),
    (140004, 1000006),
    (140008, 1000010),
    (140015, 1000015),
    (140025, 1000001),
    (140036, 1000002),
    (140078, 1000003),
    (140102, 1000004),
    (140103, 1000005),
    (140108, 1000006),
    (140115, 1000007),
    (140525, 1000008);
COMMIT;
