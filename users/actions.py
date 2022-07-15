
from datetime import datetime
from conection_db import connection 
from notes import actions_notes

class Actions:
   
   def __init__(self):
          self.connect_db = connection.Connection()
   
   def create_acount(self):
             
      u_name = input("\nWrite please your Name\n")
      mail = input("\n your mail\n")
      psswrd = input("\nand your password!\n")
      #created_user = user.User(datetime.now(),u_name,mail,psswrd)
      user_values = (datetime.now(),u_name,mail,psswrd) #(created_user.reg_time,created_user.u_name,created_user.mail,created_user.psswrd)
      
      sql = "INSERT INTO users(reg_time,u_name,mail,psswrd) VALUES (?,?,?,?)"
      #print(connect_db)
      #connect_db.execute(sql,created_user.reg_time,created_user.u_name,created_user.mail,created_user.psswrd)
      self.connect_db.write_account_in(sql,user_values)
      if self.connect_db.cursor ==1:
         print(f"\nThanks for creating of account {user_values[1]}, now you can login !!!\n")
      

   def verify_acount(self):
          
      mail = input("\n Write please your mail in\n")
      psswrd = input("\n Now for login write your  password!\n")
      user_values = (mail,psswrd)
      sql = "SELECT * from users WHERE mail = ? AND psswrd = ?"
      result = self.connect_db.verify_user_login(sql,user_values,True)
      self.user_action_in_account(result)

   
   def user_action_in_account(self,logining_user):
          
      actions_for_notes = actions_notes.Action_notes(logining_user[0])
      
      while(True):
          
         print("""
         Hi, you can do:\n\n
         \t-create note (create)\n
         \t-read your notes (read)\n
         \t-delete note (delete)\n
         \t-exit of app (exit)\n
         """)
         actions_in_account = input("What want you to do??")
         if actions_in_account == "create":
            print("Create your note!")
            actions_for_notes.create_note()
            
         
         elif actions_in_account == "read":
            print("Here are your notes!")
            actions_for_notes.read_the_notes()
            
            
         elif actions_in_account == "delete":
            print("Delete your note!")
            actions_for_notes.delete_note()
           
         elif actions_in_account == "exit":
            actions_for_notes.close_the_db()
            print("Thanks for using the app, Good bye!")
            exit()
         else:
            print("I dont understand, please try it again")
            
            