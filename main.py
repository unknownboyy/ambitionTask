from welcomeUtils import welcomeScreen, wrongChoice, invalidUser, userLimitExceeded
from caseConstants import LOGIN, SIGNUP, EXIT
from loginUtils import login, signup, canCreateMoreUser
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
    if canCreateMoreUser():
        user = signup()
        menu(user)
    else:
        userLimitExceeded()

elif choice == EXIT:
    print("See You Later...")

else:
    wrongChoice()