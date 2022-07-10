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
      print(connect_db)
      #connect_db.execute(sql,created_user.reg_time,created_user.u_name,created_user.mail,created_user.psswrd)
      connect_db.write_in(sql,user_values)

      """
      

      conec =Conexion()
      conec.execute(sql, datetime.now(),User.u_name,User.mail,User.psswrd)
      """
