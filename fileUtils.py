import os
import json
from encryptionUtils import encrypt, decrypt
from caseConstants import LOGIN_FILE, ENCRYPTION_KEY, JOURNAL_FILE


def getEmptyUserFileData():
    users = dict()
    return users

def ensureUsersFile():
    if not os.path.isfile(LOGIN_FILE):
        file = open(LOGIN_FILE,"w")
        json.dump(getEmptyUserFileData(),file)
        file.close()

def getEmptyJournalFileData():
    journals = dict()
    return journals

def ensureJournalsFile():
    if not os.path.isfile(JOURNAL_FILE):
        file = open(JOURNAL_FILE,"w")
        json.dump(getEmptyJournalFileData(),file)
        file.close()


def getUser(email,password):
    ensureUsersFile()
    file_data = open(LOGIN_FILE,"r")
    users = json.load(file_data)
    file_data.close()
    if email in users and users[email] == password:
        return email
    else:
        return None

def setUser(email,password):
    ensureUsersFile()
    file_data = open(LOGIN_FILE,"r")
    users = json.load(file_data)
    file_data.close()
    file_data = open(LOGIN_FILE,"w")
    users[email] = password
    json.dump(users,file_data)

def getJournals(user):
    ensureJournalsFile()
    file_data = open(JOURNAL_FILE,"r")
    journals = json.load(file_data)
    file_data.close()
    user_journals = journals.get(user,[])
    return user_journals

def saveNewJournal(user,journal):
    ensureJournalsFile()
    file_data = open(JOURNAL_FILE,"r")
    journals = json.load(file_data)
    file_data.close()
    file_data = open(JOURNAL_FILE,"w")
    user_journals = journals.get(user,[])
    user_journals.append({"TITLE":journal[0],"LOGS":journal[1]})
    if len(user_journals)>50:
        user_journals.pop(0)
    journals[user] = user_journals
    json.dump(journals,file_data)
    file_data.close()

def reachedUserLimit():
    ensureUsersFile()
    file_data = open(LOGIN_FILE,"r")
    users = json.load(file_data)
    file_data.close()
    return len(users)<10