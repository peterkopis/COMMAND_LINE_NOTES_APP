from datetime import datetime
from pickle import FALSE
from conection_db import connection 

class Action_notes():

    def __init__(self,user_id): 
        self.user_id = user_id
        self.connect_db = connection.Connection()
        

    def create_note(self):
        create_at = datetime.now()
        name_the_note = input("How is the name of the Note ?: ")
        content_note = input("write your note: ")
        #print(self.user_id)
        notes_values = ( create_at,name_the_note,content_note,self.user_id)
        sql = "INSERT INTO notes(create_at,name_the_note,content_note,user_id) VALUES (?,?,?,?)"
        self.connect_db.write_account_in(sql,notes_values)
        print(f"Your note is save in the app !!")

    def delete_note(self):
        name_of_note_for_deleting = input("how is the Name of note, which you want deleting")
        sql = "DELETE FROM notes WHERE (name_the_note LIKE ?) AND (user_id = ?)"
        deleting_values = (name_of_note_for_deleting,self.user_id)
        self.connect_db.write_account_in(sql,deleting_values)
        if self.connect_db.cursor.rowcount >=1:
            print("Your note is deleted !")
        else:
            print("Sorry this note not exist!")

    def read_the_notes(self):
        sql = "SELECT * FROM notes WHERE user_id = ?"
        id_user = (self.user_id,)
        result = self.connect_db.verify_user_login(sql,id_user,False)

    def close_the_db(self):
        self.connect_db.connection.close()
        
