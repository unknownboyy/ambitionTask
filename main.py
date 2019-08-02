from welcomeUtils import welcomeScreen, wrongChoice, invalidUser
from caseConstants import LOGIN, SIGNUP, EXIT
from loginUtils import login, signup
from menuUtils import menu

choice = None

choice = welcomeScreen()
if choice == LOGIN:
    user = login()
    if user == None:
        invalidUser()
    else:
        menu(user)

elif choice == SIGNUP:
    user = signup()
    menu(user)

elif choice == EXIT:
    print("See You Later...")

else:
    wrongChoice()