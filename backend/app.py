from flask import Flask, request, render_template_string, send_file, redirect
import os
import mysql.connector
import requests
import config
import utils
import pickle
import hashlib
import xml.etree.ElementTree as ET

app = Flask(__name__)

# SQL Injection Vulnerable Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return "Logged in!"
    else:
        return "Invalid credentials"

# SQL Injection Vulnerable Search
@app.route('/search')
def search():
    q = request.args.get('q')
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()
    query = f"SELECT * FROM products WHERE name LIKE '%{q}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    return str(results)

# Command Injection
@app.route('/ping')
def ping():
    host = request.args.get('host')
    stream = os.popen(f"ping -c 1 {host}")
    output = stream.read()
    return f"<pre>{output}</pre>"

# SSRF
@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    r = requests.get(url)
    return r.text

# Hardcoded AWS Key Usage
@app.route('/aws-creds')
def aws_creds():
    return f"AWS Key: {config.AWS_ACCESS_KEY_ID}, Secret: {config.AWS_SECRET_ACCESS_KEY}"

# Slack User Info (using hardcoded token)
@app.route('/slack-user')
def slack_user():
    user_id = request.args.get('user_id')
    return utils.get_slack_user_info(user_id)

# Insecure Deserialization
@app.route('/deserialize', methods=['POST'])
def deserialize():
    data = request.files['data'].read()
    obj = pickle.loads(data)
    return str(obj)

# Path Traversal
@app.route('/readfile')
def readfile():
    filename = request.args.get('filename')
    with open(filename, 'r') as f:
        return f.read()

# Insecure Direct Object Reference (IDOR)
@app.route('/user')
def user():
    user_id = request.args.get('id')
    # No auth check
    conn = mysql.connector.connect(user='root', password='root', database='test')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    result = cursor.fetchone()
    return str(result)

# Sensitive Data Exposure
@app.route('/env')
def env():
    return str(dict(os.environ))

# Weak Hashing
@app.route('/hash', methods=['POST'])
def hash_password():
    password = request.form['password']
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

# Open Redirect
@app.route('/redirect')
def open_redirect():
    url = request.args.get('url')
    return redirect(url)

# Unrestricted File Upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f"/tmp/{file.filename}")
    return "File uploaded!"

# XXE
@app.route('/xml', methods=['POST'])
def xml():
    xml_data = request.data.decode()
    root = ET.fromstring(xml_data)
    return ET.tostring(root)

if __name__ == '__main__':
    app.run(debug=True) 