import mysql.connector

def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password@123",
        port=3307,
        auth_plugin='mysql_native_password',
        database="cms"
    )
    return db