DROP DATABASE IF EXISTS it_recruitment;

CREATE DATABASE IF NOT EXISTS it_recruitment;



USE it_recruitment;





DROP TABLE IF EXISTS interview_scores;

DROP TABLE IF EXISTS interview_results;

DROP TABLE IF EXISTS applications;

DROP TABLE IF EXISTS contacts;

DROP TABLE IF EXISTS vacancies;

DROP TABLE IF EXISTS projects;

DROP TABLE IF EXISTS candidates;

DROP TABLE IF EXISTS companies;

DROP TABLE IF EXISTS interview_areas;

DROP TABLE IF EXISTS english_levels;

DROP TABLE IF EXISTS tech_levels;





CREATE TABLE english_levels (

level_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(50) UNIQUE

);



INSERT INTO english_levels (name) VALUES

('Beginner'),

('Elementary'),

('Pre-Intermediate'),

('Intermediate'),

('Upper-Intermediate'),

('Advanced'),

('Fluent'),

('Proficient'),

('Native'),

('C2 Expert');





CREATE TABLE tech_levels (

tech_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(50) UNIQUE

);



INSERT INTO tech_levels (name) VALUES

('Intern'),

('Junior'),

('Middle'),

('Senior'),

('Lead'),

('Principal'),

('Architect'),

('Expert'),

('Team Lead'),

('CTO');





CREATE TABLE companies (

company_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) NOT NULL,

location VARCHAR(100)

);





INSERT INTO companies (name, location) VALUES

('TechNova', 'Kyiv'),

('SoftVision', 'Lviv'),

('InnoDev', 'Kharkiv'),

('NextGenIT', 'Odesa'),

('CloudCore', 'Dnipro'),

('QuantumSoft', 'Kyiv'),

('PixelForge', 'Lviv'),

('SkyNetLabs', 'Kharkiv'),

('ByteWave', 'Odesa'),

('DataWorks', 'Kyiv');





CREATE TABLE projects (

project_id INT AUTO_INCREMENT PRIMARY KEY,

company_id INT NOT NULL,

name VARCHAR(100) NOT NULL,

description TEXT,

FOREIGN KEY (company_id) REFERENCES companies(company_id)

);





INSERT INTO projects (company_id, name, description) VALUES

(1, 'AI Platform', 'AI-based analytics tool'),

(1, 'FinTech App', 'Mobile banking system'),

(2, 'E-commerce Portal', 'Online marketplace'),

(3, 'Game Engine', '3D engine for games'),

(4, 'Cloud CRM', 'Customer relationship management system'),

(5, 'Data Warehouse', 'Big data storage solution'),

(6, 'Quantum OS', 'Next-gen operating system kernel'),

(7, 'AR Builder', 'Augmented reality design tool'),

(8, 'Cyber Defense Suite', 'AI-powered security platform'),

(9, 'IoT Hub', 'Smart home integration platform');





CREATE TABLE vacancies (

vacancy_id INT AUTO_INCREMENT PRIMARY KEY,

project_id INT NOT NULL,

title VARCHAR(100) NOT NULL,

description TEXT,

salary_from DECIMAL(10,2),

salary_to DECIMAL(10,2),

FOREIGN KEY (project_id) REFERENCES projects(project_id),

KEY idx_vacancies_title (title)

);





INSERT INTO vacancies (project_id, title, description, salary_from, salary_to) VALUES

(1, 'Backend Developer', 'Python, Django', 2000.00, 3000.00),

(1, 'Data Scientist', 'ML, Python, SQL', 2500.00, 4000.00),

(2, 'Frontend Developer', 'React, JS', 1500.00, 2500.00),

(3, 'QA Engineer', 'Manual/Automation testing', 1200.00, 2000.00),

(4, 'Game Developer', 'C++, Unreal Engine', 2500.00, 3500.00),

(5, 'System Administrator', 'Linux, AWS', 1800.00, 2700.00),

(6, 'DevOps Engineer', 'CI/CD, Kubernetes', 3000.00, 4200.00),

(7, 'Project Manager', 'Scrum, Agile', 2200.00, 3100.00),

(8, 'Security Analyst', 'PenTesting, Network Security', 2600.00, 3800.00),

(9, 'UX Designer', 'Figma, Adobe XD', 1900.00, 2600.00);





CREATE TABLE candidates (

candidate_id INT AUTO_INCREMENT PRIMARY KEY,

full_name VARCHAR(100),

email VARCHAR(100) UNIQUE,

phone VARCHAR(20),

english_level_id INT,

tech_level_id INT,

experience_years INT,

FOREIGN KEY (english_level_id) REFERENCES english_levels(level_id),

FOREIGN KEY (tech_level_id) REFERENCES tech_levels(tech_id),

UNIQUE KEY idx_candidates_phone (phone)

);



INSERT INTO candidates (full_name, email, phone, english_level_id, tech_level_id, experience_years) VALUES

('Petro Sydorenko', 'petro@gmail.com', '+380631111111', 3, 4, 3),

('Oksana Ivanova', 'oksana@gmail.com', '+380931111222', 5, 3, 5),

('Mykola Kravchuk', 'mykola@gmail.com', '+380501112233', 2, 2, 1),

('Iryna Tkachenko', 'iryna@gmail.com', '+380671122333', 6, 3, 6),

('Andriy Shevchenko', 'andriy@gmail.com', '+380971144555', 3, 2, 3),

('Olena Pavlenko', 'olena@gmail.com', '+380931122334', 7, 5, 7),

('Taras Melnyk', 'taras@gmail.com', '+380501234567', 4, 4, 4),

('Kateryna Bondar', 'kateryna@gmail.com', '+380931233445', 5, 5, 8),

('Oleksandr Khoma', 'oleksandr@gmail.com', '+380671212121', 8, 6, 9),

('Yuliia Veres', 'yuliia@gmail.com', '+380991234111', 9, 7, 10);





CREATE TABLE applications (

application_id INT AUTO_INCREMENT PRIMARY KEY,

candidate_id INT NOT NULL,

vacancy_id INT NOT NULL,

applied_date DATE,

UNIQUE(candidate_id, vacancy_id),

FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),

FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id)

);





INSERT INTO applications (candidate_id, vacancy_id, applied_date) VALUES

(1,1,'2025-01-12'),

(2,2,'2025-01-15'),

(3,3,'2025-02-01'),

(4,4,'2025-02-10'),

(5,5,'2025-02-15'),

(6,6,'2025-03-01'),

(7,7,'2025-03-05'),

(8,8,'2025-03-10'),

(9,9,'2025-03-15'),

(10,10,'2025-03-20');





CREATE TABLE contacts (

contact_id INT AUTO_INCREMENT PRIMARY KEY,

project_id INT NOT NULL,

full_name VARCHAR(100),

email VARCHAR(100) UNIQUE,

phone VARCHAR(20),

FOREIGN KEY (project_id) REFERENCES projects(project_id)

);





INSERT INTO contacts (project_id, full_name, email, phone) VALUES

(1,'Ivan Petrenko','ivan@technova.com','+380671112233'),

(2,'Olga Shevchenko','olga@softvision.com','+380931234567'),

(3,'Dmytro Bondar','dmytro@softvision.com','+380501234111'),

(4,'Anna Kovalenko','anna@innodev.com','+380971234222'),

(5,'Serhii Horodny','serhii@cloudcore.com','+380991234000'),

(6,'Oleh Tymoshenko','oleh@quantumsoft.com','+380501000123'),

(7,'Nadiia Makarova','nadiia@pixelforge.com','+380931223344'),

(8,'Pavlo Zinchenko','pavlo@skynetlabs.com','+380671223311'),

(9,'Viktor Samoylenko','viktor@bytewave.com','+380991122333'),

(10,'Svitlana Kryvonis','svitlana@dataworks.com','+380931119988');





CREATE TABLE interview_areas (

area_id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100) UNIQUE

);





INSERT INTO interview_areas (name) VALUES

('Algorithms'),

('Databases'),

('OOP'),

('Communication'),

('Teamwork'),

('Problem Solving'),

('System Design'),

('Leadership'),

('Time Management'),

('Testing');





CREATE TABLE interview_results (

interview_id INT AUTO_INCREMENT PRIMARY KEY,

candidate_id INT NOT NULL,

vacancy_id INT NOT NULL,

interview_date DATE,

FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),

FOREIGN KEY (vacancy_id) REFERENCES vacancies(vacancy_id)

);





INSERT INTO interview_results (candidate_id, vacancy_id, interview_date) VALUES

(1,1,'2025-01-20'),

(2,2,'2025-01-25'),

(3,3,'2025-02-05'),

(4,4,'2025-02-10'),

(5,5,'2025-02-15'),

(6,6,'2025-03-01'),

(7,7,'2025-03-05'),

(8,8,'2025-03-10'),

(9,9,'2025-03-15'),

(10,10,'2025-03-20');





CREATE TABLE interview_scores (

score_id INT AUTO_INCREMENT PRIMARY KEY,

interview_id INT NOT NULL,

area_id INT NOT NULL,

score ENUM('Excellent','Good','Satisfactory') NOT NULL,

comment TEXT,

FOREIGN KEY (interview_id) REFERENCES interview_results(interview_id),

FOREIGN KEY (area_id) REFERENCES interview_areas(area_id)

);





INSERT INTO interview_scores (interview_id, area_id, score, comment) VALUES

(1,1,'Good','Knows basics, needs practice'),

(1,2,'Excellent','Strong SQL knowledge'),

(2,3,'Excellent','Great OOP understanding'),

(2,4,'Good','Confident speaker'),

(3,5,'Satisfactory','Shy but willing to improve'),

(4,6,'Good','Good logical thinking'),

(5,7,'Excellent','Strong system design skills'),

(6,8,'Excellent','Leadership potential'),

(7,9,'Good','Manages time well'),

(8,10,'Satisfactory','Needs better testing knowledge');