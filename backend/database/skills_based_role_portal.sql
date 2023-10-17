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
    FOREIGN KEY (Access_Rights) REFERENCES AccessRights(Access_Rights_ID)
);

INSERT INTO Staff (Staff_FName, Staff_LName, Dept, Country, Email, Access_Rights)
VALUES
    ('John', 'Doe', 'Human Resources', 'Singapore', 'john.doe@g1t7.com', 1),
    ('Alice', 'Smith', 'Finance', 'Singapore', 'alice.smith@g1t7.com', 2),
    ('Elena', 'Garcia', 'IT', 'Singapore', 'elena.garcia@g1t7.com', 2),
    ('Michael', 'Wang', 'Marketing', 'Singapore', 'michael.wang@g1t7.com', 2),
    ('Sakura', 'Tanaka', 'Operations', 'Japan', 'sakura.tanaka@g1t7.com', 2);
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
    (1000001, 'Operations Manager', '2023-09-15', '2023-10-15', 'Operations', 'As an Operations Manager, you will play a pivotal role in ensuring the smooth and efficient functioning of our day-to-day operations.', 'Some requirements we look out for include having a Bachelor''s degree in Management or equivalent work experience. We are looking for someone with the ability to portray strong leadership and team management skills. You need to have excellent problem-solving and decision-making abilities. We hope to have someone onboard with exceptional communication and interpersonal skills. A plus would be knowledge in the SAP ERP system. You should be able to thrive in a fast-paced and dynamic work environment. Lastely, we need someone who has a strong commitment to quality and customer satisfaction.', 8),
    (1000002, 'Marketing Manager', '2023-09-18', '2023-10-18', 'Marketing', 'As a Marketing Manager, you will be at the forefront of our marketing efforts, leading strategic initiatives to promote our products and brand. Your role will involve developing marketing campaigns, analyzing market trends, and collaborating with cross-functional teams to drive business growth.', 'Some requirements we look out for include having a Bachelor''s degree in Marketing, Business, or a related field. One must have proven experience in marketing, with a track record of successful campaigns and strategy development. One should aldo display strong leadership and team management skills. One must definitely be an excellent analytical and problem-solving abilities.One must display exceptional communication and interpersonal skills. One definitely needs to be proficient in the use of digital marketing and analytics tools. One should also have the ability to thrive in a fast-paced and dynamic work environment. One needs to exihibit creative thinking and a passion for innovation in marketing.', 6),
    (1000003, 'Customer Service Representative', '2023-09-20', '2023-10-20', 'Customer Service', 'As a Customer Service Representative, you will be the first point of contact for our customers, providing assistance and resolving inquiries. This entry-level role is an excellent opportunity to learn about our products and services while delivering exceptional customer experiences.', 'Some requirements we look out for include having a High school diploma or equivalent. One should have strong communication and interpersonal skills. It will be good if one has a basic computer skills. One must display the ability to work well in a team. One should display willingness to learn and adapt in a fast-paced environment.', 5),
    (1000004, 'Project Coordinator', '2023-09-22', '2023-10-22', 'Project Management', 'As a Project Coordinator, you will support the planning and execution of projects. This intermediate-level role involves coordinating project activities, tracking progress, and ensuring timely delivery. You will collaborate with cross-functional teams to achieve project goals.', 'Some requirements we look out for include having a Bachelor''s degree in Business, Project Management, or a related field. One needs to have over 2 years of experience in project coordination or a similar role. One should have strong organizational and multitasking abilities. One needs to have excellent communication and teamwork skills. One needs to have high proficiency in project management software.', 6),
    (1000005, 'Software Developer', '2023-09-25', '2023-10-25', 'Information Technology', 'As a Junior Software Developer, you will be part of our software development team, working on coding, testing, and debugging software applications. This role is ideal for recent graduates or individuals with limited professional experience in software development.', 'Some requirements we look out for include having a Bachelor''s degree in Computer Science or related field. One needs to have basic knowledge of programming languages (e.g., Java, Python, C++). One needs to display strong problem-solving and analytical skills. One needs to protray an eagerness to learn and adapt to new technologies. One needs to be a team player with good communication skills.', 7),
    (1000006, 'Financial Analyst', '2023-09-28', '2023-10-28', 'Finance', 'As a Financial Analyst, you will play a key role in financial planning, analysis, and reporting. This mid-level position involves evaluating financial data, preparing forecasts, and providing insights to support strategic decision-making.', 'Some requirements we look out for include having a Bachelor''s degree in Finance, Accounting, or a related field. One needs to have over 3 years of experience in financial analysis. One needs to portray a strong analytical and quantitative skills. One should display a high proficiency in financial modeling and data analysis tools. One must be an excellent communication and presentation skills.', 4),
    (1000007, 'Senior Product Manager', '2023-10-01', '2023-10-31', 'Product Management', 'As a Senior Product Manager, you will lead the strategic development and management of our product portfolio. This senior-level role involves defining product vision, setting goals, and driving cross-functional teams to deliver innovative and successful products to market.', 'Some requirements we look out for include having a Bachelor''s degree in Business, Marketing, or a related field; MBA preferred. One should have over 5 years of experience in product management, including leadership roles. One must have a proven track record of successful product launches. One should also display strong strategic thinking and market analysis skills. One must display exceptional leadership and communication abilities.', 2);
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