import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",      
    password="",      d
    database="my_python_db"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE
    )
""")

print("Connected to MySQL and table checked/created successfully! ✅")

def insert_user(name, email):
    try:
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        cursor.execute(sql, values)
        db.commit()
        print(f"User {name} added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

insert_user("John Doe", "john@example.com")
insert_user("Jane Smith", "jane@example.com")

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

print("\nAll Users:")
for user in users:
    print(user)

# Close the connection
db.close()
