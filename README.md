Assignment With Flask
To ensure your system can run the Flask application smoothly, please verify that the following prerequisites are installed:
Python software (Version 3.12 or other)

PIP (Python Package Installer)

Flask (Web framework)

MySql (Database)

flask_mysqldb,MySQLdb (Library)

For setting-up the flask application:
1.To clone or download the application source code from the repository.

2.Open a terminal or command prompt on your computer and navigate to the Directory Where You Want to Clone the Repository.

3.Create a virtual environment [optional but recommended]. Run the following command: - Syntax : python3 -m venv flaskenv

4.Activate the virtual environment. Run the appropriate command: - Syntax : flaskenv\Scripts\activate.bat

5.Run the following command to install the required dependencies:pip install -r requirements.txt.

Configuration to connect Flask with MySql.
MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'Your hostname' app.config['MYSQL_DATABASE_USER'] = 'your_username' app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password' app.config['MYSQL_DATABASE_DB'] = 'your_database_name'

To Run the apllication, follow these steps:
1.Make sure you are in the project directory and the virtual environment is activated (if you created one). 2.Once the virtual environment is activated and the FLASK_APP environment variable is set (if necessary), run the Flask application using the flask run command. 3.Open a web browser and navigate to http://localhost:5000 to access the Flask application. You should see the application running in the browser.

Database Schema {Sql queries used in Task-2(c)}
To create a database with the name "users":- Query --> CREATE DATABASE users;

To create a table with the name "users":-

Query--> CREATE TABLE users ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), role VARCHAR(255) );

For inserting data into users table:-
Query--> INSERT INTO users (name, email, role) VALUES ('Shubham', 'shubham@gmail.com', 'Admin'), ('Sakshi', 'sak@gmail.com', 'java_Developer'), ('Virat', 'viru@gmail.com', 'ITsupport');

For retrieve all users from the "users" table:-
Query--> SELECT * FROM users;

For retrieve a specific user by their ID:-
Query--> SELECT * FROM users WHERE id = 1;

GIT WORKFLOW