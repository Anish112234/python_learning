import sqlite3

def update_users(user_id,name,age,email):
  conn = sqlite3.connect("database.db")
  c=conn.cursor()

  c.execute("""
       UPDATE users
       SET name=?,age=?,email=?
          WHERE id = ?
         """,(name, age, email,user_id))

  conn.commit()
  conn.commit()
 
update_users(1,"Shyam",30,"shyam12@gmail.com,")



   #inventory management system
    #validation system or tracker 