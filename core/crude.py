import sqlite3

# connection to data base
con = sqlite3.connect('mydatabase.db')
cur = con.cursor()


while True:
    command = input("choice your option (create, insert, delete, update, list, exit)")
   
    if command == "list":
        cur.execute("SELECT * from crude")
        data = cur.fetchall()
        for item in data:
            print("id :",item[0], "title : ",item[1], "description : ",item[2], "is_done : ","[x]" if item[3] == True else "[ ]")
   
    elif command == "create":
        name =input("enter name in table :")
        cur.execute(f"""CREATE table IF NOT EXISTS {name}(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, is_done BOOLEAN)""")
        con.commit()
    
    elif command == "insert":
        title = input("enter title: ")
        description = input("enter description: ")
        entity = [title, description, False]
        cur.execute("INSERT INTO crude(title, description, is_done) VALUES (?, ?, ?)", entity)
        con.commit()
        
    elif command == "delete":
        id = input("Enter task id for removal: ")
        cur.execute(f"DELETE FROM crude WHERE id ={id} ")
        con.commit()
    
    elif command == "update":
        id = input("Enter task id for updating to done: ")
        cur.execute(f"UPDATE crude SET is_done=trueWHERE id ={id} ")
        con.commit()
    
        
    elif command =="exit":
        con.close()
        break

  