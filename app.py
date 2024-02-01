from flask import Flask, request, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect

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

if __name__ == '__main__':
    app.run(debug=True)
