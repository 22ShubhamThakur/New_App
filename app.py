from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from MySQLdb import MySQLError

app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Honey2206@#'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/hello')
def hello():
    return render_template('Hello.html', users=users)

@app.route('/users')
def users():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        cur.close()
        return render_template('users.html', users=users)
    except Exception as e:
        return str(e), 500

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            role = request.form['role']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users (name, email,role) VALUES (%s, %s, %s)", (name, email, role))
            mysql.connection.commit()
            cur.close()
            return redirect('/users')
        except Exception as e:
            return str(e), 500
    else:
        return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def user_details(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        cur.close()
        if user:
            return render_template('user_details.html', user=user)
        else:
            return "User not found", 404
    except Exception as e:
        return str(e), 500

@app.errorhandler(404)
def page_not_found(error):
    return "404 - Page not found", 404

@app.errorhandler(MySQLError)
def handle_database_error(error):
    return "Database error occurred", 500

if __name__ == '__main__':
    app.run(debug=True)
