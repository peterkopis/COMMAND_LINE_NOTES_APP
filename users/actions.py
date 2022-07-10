from users import user
import Conexion
from datetime import datetime

class Actions:
   
   
   def create_acount(self):
      
      u_name = input("\nWrite please your Name\n")
      mail = input("\n your mail\n")
      psswrd = input("\nand your password!\n")
      
      
      """
      sql = "INSERT INTO users(reg_time,u_name,mail,psswrd) VALUES (%s,%s,%s,%s)"

      conec =Conexion()
      conec.execute(sql, datetime.now(),User.u_name,User.mail,User.psswrd)
      """
