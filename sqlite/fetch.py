import sqlite3

#for connect to sqlite database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
#create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE                                            
)
""")
#multiplle users
users=[
    ("jona",25,"jona12@gmail.com"),
    ("aakash",22,"aakash12@gmail.com"),
    ("bikash",29,"bikash12@gmail.com"),
    ("biswash",30,"biswash12@gmail.com")
]
cursor.executemany(
    "INSERT OR IGNORE INTO users(name,age,email) VALUES (?,?,?)",
    users
)
#save changes
conn.commit()

#fetch all users
cursor.execute("SELECT*FROM users")
rows = cursor.fetchall()

print("users in Database")
for row in rows:
    print(row)

#close connection
conn.close()    