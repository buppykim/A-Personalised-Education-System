from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    
    conn.commit()
    conn.close()

def insert_sample_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


    cursor.execute("INSERT OR IGNORE INTO users (email, password) VALUES (?, ?)", ('user@example.com', 'password123'))

    conn.commit()
    conn.close()

create_database()
insert_sample_user()

def validate_user(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()

    conn.close()

    return user  # Returns the user data if found, else None

# Route to display the login page
@app.route('/')
def login_page():
    return render_template('login.html')  # Make sure the login.html is in the templates folder

# Route to handle form submission for login
@app.route('/login', methods=['POST'])
def login():
    email = request.form['exampleInputEmail']
    password = request.form['exampleInputPassword']

    user = validate_user(email, password)

    if user:
        # User found, login successful
        return redirect(url_for('dashboard'))
    else:
        # Invalid credentials, show error message
        flash('Invalid email or password. Please try again.')
        return redirect(url_for('login_page'))

# Route for the dashboard or logged-in page
@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)