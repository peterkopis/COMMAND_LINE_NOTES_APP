#for first the connection to the sqlite!
import sqlite3

class Connection:
    def __init__(self):
        self.connection = sqlite3.connect('note_project.sqlite') 
        self.cursor = self.connection.cursor()

    def write_account_in(self,sql,values):
        try:
            self.cursor.execute(sql,values)
            self.connection.commit()
            
            
            
        except:
            print("Sorry anything is wrong, try it again")
            

    def verify_user_login(self,sql,values,user_login):
        try:
            self.cursor.execute(sql,values)
            if user_login:
                result =self.cursor.fetchone()
                print(f"\n Welcome {result[2]}, your login is succesfully !!\n")
            else:
                result = self.cursor.fetchall()
                for every_result in result:
                    print(f"""****************\nyour Note: {every_result[2]} created at: {every_result[1]}\nthe content of app:\n {every_result[3]}""")
            #self.connection.close()
            
            return result
        except:
            print("Sorry login is incorrect , try it again")
