import sqlite3

# connection to data base
# con =sqlite3.connect('./core/mydatabase.db')
con = sqlite3.connect('mydatabase.db')

# cursor execute command & con command deploy (commit)
# CREATE 
cur = con.cursor()
cur.execute("""CREATE table IF NOT EXISTS Crude(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, is_done BOOLEAN)""")
con.commit()

# testing query 
# for i in range(3):
#     cur.execute("INSERT INTO crude(title, description,is_done)VALUES ('do homework','do your homework title midnight', 'false')")
# con.commit()

# added my data into table
# create (One) dynamically
entity = ['new task', 'some description', False]
# cur.execute("INSERT INTO crude(title, description,is_done)VALUES ('do homework','do your homework title midnight', 'false')")
# cur.execute("INSERT INTO crude(title, description,is_done)VALUES (?,?, ?)",entity)

entities =[['new task 1', 'some description', False],['new task 2', 'some description', False]]
cur.executemany("INSERT INTO crude(title, description,is_done)VALUES (?,?, ?)",entities)
con.commit()
# print("executed successfully")

# deleted item in table 
# DELETE
# cur.execute("DELETE FROM crude WHERE id =7")
# con.commit()

# updated item in table record
# UPDATE
# cur.execute("UPDATE crude SET is_done=true WHERE id=6")
# con.commit()


# READ [list]
cur.execute("SELECT * FROM crude")
data = cur.fetchall()
# data = cur.fetchone()

for item  in data:
    print(item[1])

print(data)


con.close()
