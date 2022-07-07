#first menu of app
from datetime import datetime

now= datetime.now().strftime("%d/%m/%Y")
print(f"\nWelcome in notes app, today is {now} \n\n -you can create an acount (create)\n -or login in your existing acount (login)\n")