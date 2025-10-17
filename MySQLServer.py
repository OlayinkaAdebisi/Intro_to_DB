import mysql.connector

try:
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="Karonwi006#",
    database="alx_book_store"
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    if mydb.is_connected():
        print(" Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print("Connection error")
mycursor.close()
mydb.close()