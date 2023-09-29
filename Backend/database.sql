CREATE SCHEMA spm_project;
USE spm_project;

CREATE TABLE staff (
    staff_id INT AUTO_INCREMENT PRIMARY KEY,
    staff_fname VARCHAR(50) NOT NULL,
    staff_lname VARCHAR(50) NOT NULL,
    dept VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    access_right INT
);

CREATE TABLE role_skill (
	role_name VARCHAR(20),
    skill_name VARCHAR(50),
    PRIMARY KEY (role_name, skill_name)
);

CREATE TABLE staff_skill (
	staff_id INT,
    role_name VARCHAR(20),
    skill_name VARCHAR(50),
	FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (role_name, skill_name) REFERENCES role_skill(role_name, skill_name)
);
