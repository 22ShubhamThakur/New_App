
### Assignment With Flask

#### To ensure your system can run the Flask application smoothly, please verify that the following prerequisites are installed:

--> Python software (Version 3.12 or other)

--> PIP (Python Package Installer)

--> Flask (Web framework)

--> MySql (Database)

--> flask_mysqldb,MySQLdb (Library)

### For setting-up the flask application:

1.To clone or download the application source code from the repository.

2.Open a terminal or command prompt on your computer and navigate to the Directory Where You Want to Clone the Repository.

3.Create a virtual environment [optional but recommended]. Run the following command: - Syntax : python3 -m venv flaskenv

4.Activate the virtual environment. Run the appropriate command: - Syntax : flaskenv\Scripts\activate.bat

5.Run the following command to install the required dependencies:pip install -r requirements.txt.

## Configuration to connect Flask with MySql.

#### MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'Your hostname'<br>
app.config['MYSQL_DATABASE_USER'] = 'your_username'<br>
app.config['MYSQL_DATABASE_PASSWORD'] = 'your_password'<br>
app.config['MYSQL_DATABASE_DB'] = 'your_database_name'<br>

### To Run the apllication, follow these steps:
1.Make sure you are in the project directory and the virtual environment is activated (if you created one).

2.Once the virtual environment is activated and the FLASK_APP environment variable is set (if necessary), run the Flask application using the flask run command.

3.Open a web browser and navigate to http://localhost:5000 to access the Flask application. You should see the application running in the browser.

### Database Schema {Sql queries used in Task-2(c)}
1. To create a database with the name "users":- 
   Query --> CREATE DATABASE users;

2. To create a table with the name "users":-
  Query--> CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                role VARCHAR(255)
                ); 

3. For inserting data into users table:-
  Query--> INSERT INTO users (name, email, role) VALUES
            ('Shubham', 'shubham@gmail.com', 'Admin'),
            ('Sakshi', 'sak@gmail.com', 'java_Developer'),
            ('Virat', 'viru@gmail.com', 'ITsupport');

4. For retrieve all users from the "users" table:-
  Query--> SELECT * FROM users;

5. For retrieve a specific user by their ID:-
  Query--> SELECT * FROM users WHERE id = 1;


### GIT WORKFLOW

1. Fork the repository to your own GitHub account.
Command --> Git remote add origin https://github.com/22ShubhamThakur/New_App.

2. Clone your forked repository to your local machine.

3. Create a new branch for your changes:
Command--> Git branch -m steptech_assignment.

4. Implement your changes, commit them, and push to your forked repository:
Command--> Git init  
           Git add .
           Git commit -m "Your commit message"
           Git push origin steptech_assignment

5. Create a pull request from your feature branch to the main (or master) branch of the original repository.

6. If any changes are requested, make the necessary modifications in my local branch, commit the changes, and push them to forked repository. The PR will be automatically updated with the new changes.

7. Now merge pull request into the main codebase.






## Output1
![hello](https://github.com/22ShubhamThakur/New_App/blob/steptech_assignment/Output/Output1.png?raw=true)
## Output2
![Users](https://github.com/22ShubhamThakur/New_App/blob/steptech_assignment/Output/Output2.png?raw=true)
## Output3
![new_user](https://github.com/22ShubhamThakur/New_App/blob/steptech_assignment/Output/output3.png?raw=true)
## Output4
![users/id](https://github.com/22ShubhamThakur/New_App/blob/steptech_assignment/Output/output4.png?raw=true)
