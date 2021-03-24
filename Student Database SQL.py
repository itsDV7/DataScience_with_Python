import mysql.connector

# Establishing connection to SQL Server
conn = mysql.connector.connect(host="localhost", user="root", password="")
db = conn.cursor()

# Create New Database
try:
    db.execute("CREATE DATABASE Student")
except mysql.connector.errors.DatabaseError:
    pass
conn.close()

# Connect to Student Database
conn = mysql.connector.connect(host="localhost", user="root", password="", database="Student")
db = conn.cursor()

# Create New Table
try:
    db.execute("CREATE TABLE Class (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50)"
               ", number BIGINT, department VARCHAR(50))")
except mysql.connector.errors.ProgrammingError:
    pass

# Menu
while 1:
    try:
        ch = int(input("1. Add Student to Database\n2. Delete Student from Database\n3. Show Database\n4. Exit\n"))
    except ValueError:
        print("\nIncorrect Input!\n")
        continue
    # Add Record
    if ch == 1:
        name = input("Enter Student Name: ")
        number = input("Enter Number: ")
        dept = input("Enter Department: ")
        query = "INSERT INTO Class (name, number, department) VALUES (%s, %s, %s)"
        db.execute(query, (name, number, dept))
        conn.commit()
        print("\nRecord Inserted Successfully\n")
    # Delete Record
    elif ch == 2:
        query = "SELECT * FROM Class ORDER BY id"
        db.execute(query)
        data = db.fetchall()
        if data:
            ID = input("Enter ID: ")
            query = "DELETE FROM Class WHERE id = %s"
            db.execute(query, (ID,))
            conn.commit()
            print("\nRecord Deleted\n")
        else:
            print("Database is Empty!\n")
    # Show Records
    elif ch == 3:
        query = "SELECT * FROM Class ORDER BY id"
        db.execute(query)
        data = db.fetchall()
        if data:
            print("\n")
            for i in data:
                print(i)
            print("\n")
        else:
            print("Database is Empty!\n")
    # Exit Program
    elif ch == 4:
        print("\nExiting...")
        conn.close()
        break
    # Delete Database
    elif ch == 777:
        query = "DROP DATABASE Student"
        db.execute(query)
        print("Database Deleted\nExiting...")
        conn.close()
        break
    # Error Handling
    else:
        print("\nIncorrect Input!\n")
