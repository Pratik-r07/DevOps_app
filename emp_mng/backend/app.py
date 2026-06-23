from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("DB_NAME")
)

@app.route('/employees', methods=['GET'])
def get_employees():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    return jsonify(result)

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO employees(name,email,department) VALUES(%s,%s,%s)",
        (data['name'], data['email'], data['department'])
    )
    db.commit()

    return jsonify({"message": "Employee Added"}), 201

host="host.docker.internal"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)