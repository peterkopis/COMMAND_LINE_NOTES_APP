#for first the connection to the sqlite!
import sqlite3


connection = sqlite3.connect('note_project.sqlite') 
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
( id INTEGER PRIMARY KEY AUTOINCREMENT,
  reg_time DATE,
  u_name VARCHAR(355),
  mail VARCHAR(355) NOT NULL UNIQUE,
  psswrd VARCHAR(355) NOT NULL)''')
  
#cursor.execute("INSERT INTO users(u_name,mail,psswrd) VALUES ('EBOK','Edi@ebok.cz','edi2')")
cursor.execute('''CREATE TABLE IF NOT EXISTS notes
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 create_at DATE,
 name_the_note VARCHAR(355),
 content_note TEXT,
 user_id INTEGER,
 CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE) ''')

#cursor.execute("INSERT INTO notes(name_the_note,user_id) VALUES ('Huhu',1) ")
cursor.execute("DELETE FROM users ")
connection.commit()
connection.close()