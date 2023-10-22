CREATE DATABASE IF NOT EXISTS skills_based_role_portal;
USE skills_based_role_portal;

DROP TABLE IF EXISTS Staff_Role_Apply;
DROP TABLE IF EXISTS Staff_Skill;
DROP TABLE IF EXISTS Role_Skill;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Staff;
DROP TABLE IF EXISTS AccessRights;


-- ACCESS RIGHTS --------------------------------
CREATE TABLE IF NOT EXISTS AccessRights (
    Access_Rights_ID INT PRIMARY KEY,
    Access_Rights_Label VARCHAR(50) NOT NULL
);

INSERT INTO AccessRights (Access_Rights_ID, Access_Rights_Label)
VALUES
    (1, 'Admin'),
    (2, 'User'),
    (3, 'Manager');
COMMIT;

-- STAFF DETAILS --------------------------------
CREATE TABLE IF NOT EXISTS Staff (
    Staff_ID INT AUTO_INCREMENT PRIMARY KEY,
    Staff_FName VARCHAR(50) NOT NULL,
    Staff_LName VARCHAR(50) NOT NULL,
    Dept VARCHAR(50) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Email VARCHAR(50) UNIQUE NOT NULL,
    Access_Rights INT,
    Password VARCHAR(50) NOT NULL,
    FOREIGN KEY (Access_Rights) REFERENCES AccessRights(Access_Rights_ID)
);

INSERT INTO Staff (Staff_FName, Staff_LName, Dept, Country, Email, Access_Rights, Password)
VALUES
    ('John', 'Doe', 'Human Resources', 'Singapore', 'john.doe@g1t7.com', 1, '123'),
    ('Alice', 'Smith', 'Finance', 'Singapore', 'alice.smith@g1t7.com', 2, '123'),
    ('Elena', 'Garcia', 'IT', 'Singapore', 'elena.garcia@g1t7.com', 2, '123'),
    ('Michael', 'Wang', 'Marketing', 'Singapore', 'michael.wang@g1t7.com', 2, '123'),
    ('Sakura', 'Tanaka', 'Operations', 'Japan', 'sakura.tanaka@g1t7.com', 2, '123');
COMMIT;


-- ROLE/ JOB LISTING --------------------------------
CREATE TABLE IF NOT EXISTS Role (
    Role_ID INT PRIMARY KEY,
    Role_Name VARCHAR(50) NOT NULL,
    Date_Posted DATE NOT NULL,
    App_Deadline DATE NOT NULL,
    Role_Department VARCHAR(50) NOT NULL,
    Role_Description VARCHAR(2600) NOT NULL,
    Role_Requirements VARCHAR(2600) NOT NULL,
    Availability INT NOT NULL,
    INDEX (Role_Name)
);

INSERT INTO Role (Role_ID, Role_Name, Date_Posted, App_Deadline, Role_Department, Role_Description, Role_Requirements, Availability)
VALUES
    (1000001, 'Operations Manager', '2023-09-15', '2023-11-15', 'Operations', 'As an Operations Manager, you will play a pivotal role in ensuring the smooth and efficient functioning of our day-to-day operations...', 'Requirements:\n- Bachelor''s degree in Management or equivalent work experience.\n- Strong leadership and team management skills.\n- Excellent problem-solving and decision-making abilities.\n- Exceptional communication and interpersonal skills.\n- Proficiency in SAP ERP system.\n- Ability to thrive in a fast-paced and dynamic work environment.\n- Strong commitment to quality and customer satisfaction.', 8),
    (1000002, 'Marketing Manager', '2023-09-18', '2023-11-18', 'Marketing', 'As a Marketing Manager, you will be at the forefront of our marketing efforts, leading strategic initiatives to promote our products and brand. Your role will involve developing marketing campaigns, analyzing market trends, and collaborating with cross-functional teams to drive business growth...', 'Requirements:\n- Bachelor''s degree in Marketing, Business, or a related field.\n- Proven experience in marketing, with a track record of successful campaigns and strategy development.\n- Strong leadership and team management skills.\n- Excellent analytical and problem-solving abilities.\n- Exceptional communication and interpersonal skills.\n- Proficiency in digital marketing tools and analytics.\n- Ability to thrive in a fast-paced and dynamic work environment.\n- Creative thinking and a passion for innovation in marketing.', 6),
    (1000003, 'Customer Service Representative', '2023-11-20', '2023-10-20', 'Customer Service', 'As a Customer Service Representative, you will be the first point of contact for our customers, providing assistance and resolving inquiries. This entry-level role is an excellent opportunity to learn about our products and services while delivering exceptional customer experiences.', 'Requirements:\n- High school diploma or equivalent.\n- Strong communication and interpersonal skills.\n- Basic computer skills.\n- Ability to work well in a team.\n- Willingness to learn and adapt in a fast-paced environment.', 5),
    (1000004, 'Project Coordinator', '2023-09-22', '2023-11-22', 'Project Management', 'As a Project Coordinator, you will support the planning and execution of projects. This intermediate-level role involves coordinating project activities, tracking progress, and ensuring timely delivery. You will collaborate with cross-functional teams to achieve project goals.', 'Requirements:\n- Bachelor''s degree in Business, Project Management, or a related field.\n- 2+ years of experience in project coordination or a similar role.\n- Strong organizational and multitasking abilities.\n- Excellent communication and teamwork skills.\n- Proficiency in project management software.', 6),
    (1000005, 'Software Developer', '2023-09-25', '2023-11-25', 'Information Technology', 'As a Junior Software Developer, you will be part of our software development team, working on coding, testing, and debugging software applications. This role is ideal for recent graduates or individuals with limited professional experience in software development.', 'Requirements:\n- Bachelor''s degree in Computer Science or related field.\n- Basic knowledge of programming languages (e.g., Java, Python, C++).\n- Strong problem-solving and analytical skills.\n- Eagerness to learn and adapt to new technologies.\n- Team player with good communication skills.', 7),
    (1000006, 'Financial Analyst', '2023-09-28', '2023-11-28', 'Finance', 'As a Financial Analyst, you will play a key role in financial planning, analysis, and reporting. This mid-level position involves evaluating financial data, preparing forecasts, and providing insights to support strategic decision-making.', 'Requirements:\n- Bachelor''s degree in Finance, Accounting, or a related field.\n- 3+ years of experience in financial analysis.\n- Strong analytical and quantitative skills.\n- Proficiency in financial modeling and data analysis tools.\n- Excellent communication and presentation skills.', 4),
    (1000007, 'Senior Product Manager', '2023-10-01', '2023-11-30', 'Product Management', 'As a Senior Product Manager, you will lead the strategic development and management of our product portfolio. This senior-level role involves defining product vision, setting goals, and driving cross-functional teams to deliver innovative and successful products to market.', 'Requirements:\n- Bachelor''s degree in Business, Marketing, or a related field; MBA preferred.\n- 5+ years of experience in product management, including leadership roles.\n- Proven track record of successful product launches.\n- Strong strategic thinking and market analysis skills.\n- Exceptional leadership and communication abilities.', 2);
COMMIT;

-- SKILLS REQ OF A ROLE --------------------------------
CREATE TABLE IF NOT EXISTS Role_Skill (
    Role_Name VARCHAR(50),
    Skill_Name VARCHAR(50),
    PRIMARY KEY (Role_Name, Skill_Name),
    FOREIGN KEY (Role_Name) REFERENCES Role(Role_Name),
    INDEX (Skill_Name)
);

INSERT INTO Role_Skill (Role_Name, Skill_Name)
VALUES
    ('Operations Manager', 'Operations Management'),
    ('Operations Manager', 'Process Improvement'),
    ('Operations Manager', 'Team Leadership'),
    ('Operations Manager', 'Quality Control'),
    ('Operations Manager', 'Vendor Relations'),
    
    ('Marketing Manager', 'Marketing Strategy'),
    ('Marketing Manager', 'Campaign Management'),
    ('Marketing Manager', 'Market Research'),
    ('Marketing Manager', 'Team Leadership'),
    ('Marketing Manager', 'Budget Management'),
    
    ('Customer Service Representative', 'Customer Service'),
    ('Customer Service Representative', 'Communication'),
    ('Customer Service Representative', 'Interpersonal Skills'),
    ('Customer Service Representative', 'Teamwork'),
    
    ('Project Coordinator', 'Project Coordination'),
    ('Project Coordinator', 'Organizational Skills'),
    ('Project Coordinator', 'Communication'),
    ('Project Coordinator', 'Teamwork'),
    ('Project Coordinator', 'Project Management'),
    
    ('Software Developer', 'Software Development'),
    ('Software Developer', 'Programming'),
    ('Software Developer', 'Problem-Solving'),
    ('Software Developer', 'Adaptability'),
    ('Software Developer', 'Teamwork'),
    
    ('Financial Analyst', 'Financial Analysis'),
    ('Financial Analyst', 'Financial Modeling'),
    ('Financial Analyst', 'Data Analysis'),
    ('Financial Analyst', 'Quantitative Skills'),
    ('Financial Analyst', 'Communication'),
    
    ('Senior Product Manager', 'Product Management'),
    ('Senior Product Manager', 'Strategic Thinking'),
    ('Senior Product Manager', 'Product Launches'),
    ('Senior Product Manager', 'Market Analysis'),
    ('Senior Product Manager', 'Leadership');

    -- ('Human Resources Manager', 'Recruitment'),
    -- ('Human Resources Manager', 'Employee Relations'),
    -- ('Human Resources Manager', 'Communication'),
    -- ('Human Resources Manager', 'Teamwork'),
    -- ('Human Resources Manager', 'Leadership'),

    -- ('Finance Executive', 'Budgeting'),
    -- ('Finance Executive', 'Accounting'),
    -- ('Finance Executive', 'Communication'),
    -- ('Finance Executive', 'Teamwork'),
    -- ('Finance Executive', 'Analytical Skills'),

    -- ('IT Manager', 'Networking'),
    -- ('IT Manager', 'Database Management'),
    -- ('IT Manager', 'Communication'),
    -- ('IT Manager', 'Teamwork'),
    -- ('IT Manager', 'Leadership'),

    -- ('IT Executive', 'Software Development'),
    -- ('IT Executive', 'Programming'),
    -- ('IT Executive', 'Problem-Solving'),
    -- ('IT Executive', 'Adaptability'),
    -- ('IT Executive', 'Teamwork'),

    -- ('Marketing Executive', 'Digital Marketing'),
    -- ('Marketing Executive', 'Market Research'),
    -- ('Marketing Executive', 'Communication'),
    -- ('Marketing Executive', 'Campaign Management'),
    -- ('Marketing Executive', 'Analytical Skills'),

    -- ('Operations Executive', 'Supply Chain Management'),
    -- ('Operations Executive', 'Process Optimization'),
    -- ('Operations Executive', 'Communication'),
    -- ('Operations Executive', 'Teamwork'),
    -- ('Operations Executive', 'Analytical Skills');
COMMIT;


-- STAFF SKILLS --------------------------------
CREATE TABLE IF NOT EXISTS Staff_Skill (
    Staff_ID INT,
    Skill_Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (Staff_ID, Skill_Name),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
    -- FOREIGN KEY (Skill_Name) REFERENCES Role_Skill(Skill_Name)
);

INSERT INTO Staff_Skill (Staff_ID, Skill_Name)
VALUES
    (1, 'Communication'),
    (1, 'Recruitment'),
    (1, 'Employee Relations'),
    (2, 'Financial Analysis'),
    (2, 'Budgeting'),
    (2, 'Accounting'),
    (3, 'Software Development'),
    (3, 'Database Management'),
    (3, 'Networking'),
    (4, 'Digital Marketing'),
    (4, 'Market Research'),
    (4, 'Campaign Management'),
    (5, 'Supply Chain Management'),
    (5, 'Process Optimization'),
    (5, 'Quality Control');
COMMIT;

CREATE TABLE IF NOT EXISTS Staff_Role_Apply (
    Staff_ID INT,
    Role_ID INT,
    Applied VARCHAR(1) NOT NULL,
    PRIMARY KEY (Staff_ID, Role_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY (Role_ID) REFERENCES Role(Role_ID)
);

INSERT INTO Staff_Role_Apply (Staff_ID, Role_ID, Applied)
VALUES
    (4, 1000004, '1');
COMMIT;
