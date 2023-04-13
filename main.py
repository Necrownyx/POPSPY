from tools import *
import poplib
import colorama
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')

def preUI():
    global d, file, accounts
    # get the user to select a file to use as the data file
    print(colorama.Fore.GREEN + "Welcome to POPSPY!" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please select a data file to use or leave blank to use : 'data.json'" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "" + colorama.Fore.RESET)

    file = input("File: ")
    if file == "": file = "data.json"

    d = data(file)
    # load all the accoutns into accounts object
    accounts = d.loadAccounts()
    print(accounts)
    input("Press enter to continue")

    os.system('cls' if os.name == 'nt' else 'clear')
    printUI()


# UI
def printUI(error=False):
    colorama.init()
    if error == True: print(colorama.Fore.RED + "Invalid choice please try again" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Welcome to the POPSPY User Interface!" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please select an option from below to continue" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "1. Import Account/Accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "2. Save Data to json" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "3. View Loaded Accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "4. Scan email subjects" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "5. Scan email bodies (slow)" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "6. Exit" + colorama.Fore.RESET)

    choice = input("Choice: ")
    if choice == "1": importAccount()
    elif choice == "2": exportAccount()
    elif choice == "3": viewAccounts()
    elif choice == "4": scanSubjects()
    elif choice == "5": scanBodies()
    elif choice == "6": exit()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI(error=True)

# import an account
def importAccount():
    global d, file, accounts

    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    print(colorama.Fore.GREEN + "IMPORT ACCOUNTS" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please enter the account details in the below format or provide the name of a txt file with the below format separated with newlines" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "Format: email:password:server" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "Example: example@example.com:password:pop.example.com" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "" + colorama.Fore.RESET)

    acc = input("Input: ")
    check = input("do you want to check the accounts? (y/n): ")
    if check == "y": check = True
    else: check = False

    default_active = False
    if not check:
        default_active = input("Do you want to set the default state of the accounts to active? (y/n): ")
        if default_active == "y": default_active = True

    if acc.endswith(".txt"):
        with open(accounts, "r") as f:
            acc = f.read()
        
        acc = accounts.split("\n")
        for i in acc:
            if i == "": acc.remove(i)
            else: 
                i = i.split(":")
                acc = account(i[0], i[1], i[2], check, default_active)
                d.appendAccount(acc)
                accounts.append(acc)
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI()
    
    else:
        acc1 = acc.split(":")
        acc= account(acc1[0], acc1[1], acc1[2], check, default_active)
        d.appendAccount(acc)
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI()

def exportAccount():
    global d, file

    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    print(colorama.Fore.GREEN + "EXPORT ACCOUNTS" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please enter the name of the file you want to export the accounts to or the file: '" + file + "' will be used." + colorama.Fore.RESET)

    i = input("File: ")
    if i == "": i = file

    print(d.accounts)
    if d.saveData(file, [d.accounts, d.settings, d.messages]):
        print(colorama.Fore.GREEN + "Successfully saved data to: " + i + colorama.Fore.RESET)
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI()
    else:
        print(d.saveData(file, [d.accounts, d.settings, d.messages]))
        print(colorama.Fore.RED + "Failed to save data to: " + i + colorama.Fore.RESET)
        print(colorama.Fore.RED + "Please raise an issue on this projects github page" + i + colorama.Fore.RESET)

def viewAccounts():
    global d

    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    print(colorama.Fore.GREEN + "VIEW ACCOUNTS" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please select an option from below to continue" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "1. View all accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "2. View active accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "3. View inactive accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "4. Exit" + colorama.Fore.RESET)

    choice = input("Choice: ")
    if choice == "1": printAccounts(d.getAccounts())
    elif choice == "2": printAccounts(d.getActiveAccounts())
    elif choice == "3": printAccounts(d.getInactiveAccounts())
    elif choice == "4": 
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI()
    else: 
        os.system('cls' if os.name == 'nt' else 'clear')
        viewAccounts()

def printAccounts(accounts):
    for i in accounts:
        print(i[0])
    
    input("Press enter to continue")
    os.system('cls' if os.name == 'nt' else 'clear')
    viewAccounts()

def scanSubjects():
    global d, accounts

    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    print(colorama.Fore.GREEN + "SCAN SUBJECTS" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please enter the keywords you want to scan for separated by a comma and a space" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "Example: keyword1, keyword2, keyword3" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "" + colorama.Fore.RESET)

    keywords = input("Keywords: ")
    keywords = keywords.split(", ")
    
    
    # create a list of all active accounts that have more than 0 messages
    active_accounts = []
    for i in accounts:
        if i.messageCount > 0 and i.active:
            active_accounts.append(i)
    
    # if their is more accounts than active accounts
    if len(accounts) > len(active_accounts):
        print(colorama.Fore.RED + "There are " + str(len(accounts) - len(active_accounts)) + " accounts with no messages" + colorama.Fore.RESET)
        print(colorama.Fore.RED + "Do you want to scan them for messages or they will be skipped? (y/n)" + colorama.Fore.RESET)
        choice = input("Choice: ")
        if choice == "y":
            print('not implemented yet')
        else:
            pass
    
    # if their is no active accounts
    if len(active_accounts) == 0:
        print(colorama.Fore.RED + "There are no active accounts with messages" + colorama.Fore.RESET)
        print(colorama.Fore.RED + "Please add some accounts or make some accounts active" + colorama.Fore.RESET)
        input("Press enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        printUI()
    
    for acc in active_accounts:
        subjects = acc.getAllSubjects()

        for key in keywords:
            for sub in subjects:
                if key in sub:
                    print(acc[0] + " has a message with the subject: " + sub + " with the keyword: " + key + " in it")





# print the ui
preUI()
