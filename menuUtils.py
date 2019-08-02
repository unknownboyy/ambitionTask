from caseConstants import MY_JOURNAL, NEW_JOURNAL, EXIT
from welcomeUtils import wrongChoiceEnterAgain
from fileUtils import getJournals, saveNewJournal

def printJournal(journal):
    print("-"*50)
    print("TITLE: ",journal["TITLE"])
    for log in journal["LOGS"]:
        print(log)
    print("-"*50)

def showOptions():
    print("1. My Journals")
    print("2. Add New Journal")
    print("Enter Your Choice (Press RETURN to exit):",end="")

def getChoice():
    inp = input()
    if len(inp)==0:
        return None
    else:
        try:
            return int(inp)
        except:
            return -1

def showMyJournals(user):
    journals = getJournals(user)
    if len(journals)==0:
        print("No Journals Found !!")
    else:
        for journal in journals:
            printJournal(journal)

def getJournalLogs():
    logs = []
    inp = input("Enter LOG (Press RETURN to Stop):")
    while len(inp)>0:
        logs.append(inp)
        inp = input("Enter LOG (Press RETURN to Stop):")
    return logs

def getNewJournal():
    journal_title = input("Enter Journal Title:")
    journal_logs = getJournalLogs()
    return (journal_title,journal_logs)


def storeNewJournal(user):
    journal = getNewJournal()
    saveNewJournal(user,journal)

def menu(user):
    showOptions()
    choice = getChoice()
    while choice != EXIT:
        if choice == MY_JOURNAL:
            showMyJournals(user)
        
        elif choice == NEW_JOURNAL:
            storeNewJournal(user)
        
        else:
            wrongChoiceEnterAgain()
        showOptions()
        choice = getChoice()