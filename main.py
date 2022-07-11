#first menu of app

from datetime import datetime
from users import actions


now= datetime.now().strftime("%d/%m/%Y")

while(True):
    while(True):
        print(f"\nWelcome in notes app, today is {now} \n\n -you can create an acount (create)\n -or login in your existing acount (login)\n")
        first_action =input().lower()
        if (first_action == "create" or first_action == "login"):
            break
        print("Sorry, try it again !!")
    #Instance of class for actions, like create account or login in account
    do_it = actions.Actions()

    if first_action == "create":
            do_it.create_acount()
    