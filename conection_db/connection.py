#for first the connection to the sqlite!
import sqlite3

class Connection:
    def __init__(self):
        self.connection = sqlite3.connect('note_project.sqlite') 
        self.cursor = self.connection.cursor()

    def write_in_or_delete_from_db(self,sql,values):
        try:
            self.cursor.execute(sql,values)
            self.connection.commit()
        except:
            print("Sorry anything is wrong, try it again")
            

    def verify_user_or_read_the_notes_from_db(self,sql,values,user_login):
        try:
            self.cursor.execute(sql,values)
            if user_login:
                result =self.cursor.fetchone()
                print(f"\n Welcome {result[2]}, your login is succesfully !!\n")
            else:
                result = self.cursor.fetchall()
            return result
        except:
            print("Sorry login is incorrect , try it again")

    def close_the_db(self):
        self.connection.close()
