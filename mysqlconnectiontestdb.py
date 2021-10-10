import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="tanmay"
)
mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdb;")
