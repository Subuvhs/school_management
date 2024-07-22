Software Used:
Python 3.12 
MySQL 3.9
MySQL workbench 8.0 CE


Steps to run the Python File

Step 1: Create 4 Individual Table in the MySQL Database  such as follows:

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    date_of_birth DATE NOT NULL,
    grade_level INT NOT NULL
);

CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    contact_number VARCHAR(15),
    subject_taught VARCHAR(255)
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    teacher_id INT,
    maximum_students INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

CREATE TABLE Grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

Step 2: After created table in the database change the db_config file according to MySQL server or client CMD such as host, user, password, database.

Step 3(optional): after change the db_config check the connection if it is working using MySQL workbench if it positive or not.

Step 4: if the table is created successfully you directly go to python IDLE and run the app.py

Step 5: Using Console in you give input use the application.

Step 6: The Change that you make in console also affect the database file.

