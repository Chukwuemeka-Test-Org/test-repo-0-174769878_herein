# BAD: Hardcoded API Key
API_KEY = "AIzaSyD3fake-InsecureKey123456789"

from flask import Flask, request

app = Flask(__name__)

# BAD: Using query param for authentication
@app.route("/secure-data")
def insecure_api():
    token = request.args.get("token")
    if token == "letmein":  # hardcoded weak token
        return {"secret": "Sensitive data exposed!"}
    return {"error": "Unauthorized"}, 401


import sqlite3
from flask import request

def get_user_data():
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # BAD: unsanitized user input in SQL
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchall()


import pickle
from flask import request

@app.route("/load")
def load():
    data = request.data
    # BAD: Deserializing untrusted input
    obj = pickle.loads(data)
    return str(obj)
