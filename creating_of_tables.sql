"""
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
( id INTEGER PRIMARY KEY AUTOINCREMENT,
  reg_time DATE,
  u_name VARCHAR(355),
  mail VARCHAR(355) NOT NULL UNIQUE,
  psswrd VARCHAR(355) NOT NULL)''')
  

cursor.execute('''CREATE TABLE IF NOT EXISTS notes
(id INTEGER PRIMARY KEY AUTOINCREMENT,
 create_at DATE,
 name_the_note VARCHAR(355),
 content_note TEXT,
 user_id INTEGER,
 CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE) ''')
"""