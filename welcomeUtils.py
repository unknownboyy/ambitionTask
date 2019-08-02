def welcomeScreen():
    print("**  WELCOME **")
    print("1. LOGIN")
    print("2. SIGNUP")
    inp = input("ENTER YOUR CHOICE (Press RETURN to exit):")
    if len(inp)==0:
        return None
    else:
        try:
            return int(inp)
        except:
            return -1

def wrongChoice():
    print("Wrong Choice !!\nShutting Down...")

def wrongChoiceEnterAgain():
    print("Wrong Choice !!\nEnter Your Choice Again...")

def invalidUser():
    print("Wrong E-mail ID or Password !!!")