#first menu of app
from datetime import datetime

now= datetime.now().strftime("%d/%m/%Y")

while(True):
    print(f"\nWelcome in notes app, today is {now} \n\n -you can create an acount (create)\n -or login in your existing acount (login)\n")
    first_action =input().lower()
    print(first_action)
    if (first_action == "create" or first_action == "login"):
        break
    #if first_action == create:

