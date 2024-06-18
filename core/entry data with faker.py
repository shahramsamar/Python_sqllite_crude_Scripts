import sqlite3
from faker import Faker
import random
fake = Faker()


conn = sqlite3.connect("mydatabase2.db")
cur = conn.cursor()



cur.execute("Create table IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE,email TEXT UNIQUE, password TEXT)")
# cur.execute("Create table IF NOT EXISTS profiles (id INTEGER PRIMARY KEY AUTOINCREMENT,full_name TEXT NOT NULL, age INTEGER, bio TEXT ,user_id INTEGER UNIQUE , FOREIGN KEY(user_id)REFERENCES users(id) )")
cur.execute("Create table IF NOT EXISTS profiles (full_name TEXT NOT NULL, age INTEGER, bio TEXT ,user_id INTEGER UNIQUE PRIMARY KEY , FOREIGN KEY(user_id)REFERENCES users(id) )")
conn.commit()

for _ in range(5):
    profile =fake.profile()
    user = []
    
    cur.execute("INSERT INTO users(username,email,password) Values (?,?,?)",[profile.get("username"),profile.get("mail"),"Aa123456"])
    cur.execute(f"SELECT id FROM users WHERE username = '{profile.get('username')}' ")
    user_id = cur.fetchone()[0]
    cur.execute("INSERT INTO profiles(full_name,age,bio,user_id) Values (?,?,?,?)",[profile.get("name"),random.randint(20,45),fake.paragraph(nb_sentences=2),user_id])
    conn.commit()

    
# cur.execute("INSERT INTO users(username,email,password) Values ('mohammad','mohammad@gmail.com','123')")
# cur.execute("INSERT INTO profiles(full_name,age,bio,user_id) Values ('mohammad mohammadi',30,'a person alive',1)")
# conn.commit()

# get data in table users
# cur.execute('SELECT * FROM users')
# data = cur.fetchall()
# print(data)

# get data in table users
# cur.execute('SELECT * FROM profiles')
# data = cur.fetchall()
# print(data)

# get data in table users
# cur.execute('SELECT * FROM users JOIN profiles ON users.id=profiles.user_id')
# data = cur.fetchall()
# print(data)

cur.execute('SELECT id,full_name FROM users JOIN profiles ON users.id=profiles.user_id')
data = cur.fetchall()
print(data)