import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="devops",
    password="password123",
    database="emp_db"
)

print("Connected Successfully!")

conn.close() dsfd