import os
import json
from encryptionUtils import encrypt, decrypt
from caseConstants import LOGIN_FILE, ENCRYPTION_KEY, JOURNAL_FILE

def readFile(file_name):
    file_data = open(file_name,"r")
    data = decrypt( file_data.read(), ENCRYPTION_KEY )
    file_data.close()
    return json.loads(data)

def writeFile(file_name,data):
    data = json.dumps(data)
    data = encrypt(data,ENCRYPTION_KEY)
    file = open(file_name,"w")
    file.write(data)
    file.close()

def getEmptyUserFileData():
    users = dict()
    return users

def ensureUsersFile():
    if not os.path.isfile(LOGIN_FILE):
        file = open(LOGIN_FILE,"w")
        file.write(encrypt(json.dumps(getEmptyUserFileData()),ENCRYPTION_KEY))
        file.close()

def getEmptyJournalFileData():
    journals = dict()
    return journals

def ensureJournalsFile():
    if not os.path.isfile(JOURNAL_FILE):
        file = open(JOURNAL_FILE,"w")
        file.write(encrypt(json.dumps(getEmptyJournalFileData()),ENCRYPTION_KEY))
        file.close()


def getUser(email,password):
    ensureUsersFile()
    users = readFile(LOGIN_FILE)
    if email in users and users[email] == password:
        return email
    else:
        return None

def setUser(email,password):
    ensureUsersFile()
    users = readFile(LOGIN_FILE)
    users[email] = password
    writeFile(LOGIN_FILE,users)

def getJournals(user):
    ensureJournalsFile()
    journals = readFile(JOURNAL_FILE)
    user_journals = journals.get(user,[])
    return user_journals

def saveNewJournal(user,journal):
    ensureJournalsFile()
    journals = readFile(JOURNAL_FILE)
    user_journals = journals.get(user,[])
    user_journals.append({"TITLE":journal[0],"LOGS":journal[1]})
    if len(user_journals)>50:
        user_journals.pop(0)
    journals[user] = user_journals
    writeFile(JOURNAL_FILE,journals)

def reachedUserLimit():
    ensureUsersFile()
    users = readFile(LOGIN_FILE)
    return len(users)<10