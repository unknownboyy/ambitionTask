from getpass import getpass
from fileUtils import getUser, setUser

def getCredentials():
    email = input("Enter Your E-mail:")
    password = getpass(prompt="Enter Password:")
    return (email,password)

def login():
    email,password = getCredentials()
    return getUser(email,password)

def signup():
    email,password = getCredentials()
    setUser(email,password)
    return email