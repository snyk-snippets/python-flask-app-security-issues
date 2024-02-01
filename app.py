from flask import Flask, request, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import sqlite3

# Insecure Code
api_key = "my_sensitive_api_key" # Set a secret key for CSRF protection
api_url = "https://api.example.com"

app = Flask(__name__)

app.config['SECRET_KEY'] = api_key  
csrf = CSRFProtect(app)

@app.route('/')
def hello_world():
    user_input = request.args.get('input')
    return render_template('index.html', input=user_input)

@app.route('/change_password', methods=['POST'])
def change_password():
    new_password = request.form.get('new_password')
    # Change password logic here
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

    # Secure SQL query using parameterized query
    #query = "SELECT * FROM users WHERE username = ? AND password = ?"
    #cursor.execute(query, (username, password))

    # Execute the query
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
   	 return 'Login successful'
    else:
   	 return 'Login failed'

if __name__ == '__main__':
    app.run(debug=True)
