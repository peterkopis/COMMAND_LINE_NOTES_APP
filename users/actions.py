from users import user
from datetime import datetime
from conection_db import connection 


class Actions:
   
   
   def create_acount(self):
             
      u_name = input("\nWrite please your Name\n")
      mail = input("\n your mail\n")
      psswrd = input("\nand your password!\n")
      created_user = user.User(datetime.now(),u_name,mail,psswrd)
      user_values = (created_user.reg_time,created_user.u_name,created_user.mail,created_user.psswrd)
      connect_db = connection.Connection()
      sql = "INSERT INTO users(reg_time,u_name,mail,psswrd) VALUES (?,?,?,?)"
      #print(connect_db)
      #connect_db.execute(sql,created_user.reg_time,created_user.u_name,created_user.mail,created_user.psswrd)
      connect_db.write_account_in(sql,user_values)
      

   def verify_acount(self):
          
      mail = input("\n Write please your mail in\n")
      psswrd = input("\n Now for login write your  password!\n")
      user_values = (mail,psswrd)
      connect_db = connection.Connection()
      sql = "SELECT * from users WHERE mail = ? AND psswrd = ?"
      result = connect_db.verify_user_login(sql,user_values)
      #print(result)
      self.user_action_in_account(result)

   
   def user_action_in_account(self,logining_user):
      logining_user = logining_user
          
      print("""
      Hi, you can do:\n\n
      \t-create note (create)\n
      \t-read your notes (read)\n
      \t-delete note (delet)\n
      \t-exit of app (exit)\n
      """)
      actions_in_account = input("What want you to do??")
      if actions_in_account == "create":
         print("Create your note!")
         self.user_action_in_account(logining_user)
      elif actions_in_account == "read":
         print("Here are your notes!")
         self.user_action_in_account(logining_user)
      elif actions_in_account == "delete":
         print("Delete your note!")
         self.user_action_in_account(logining_user)
      elif actions_in_account == "exit":
         print("Thanks for using the app, Good bye!")
         exit()
      else:
         print("I dont understand, please try it again")
         
         