from tools import *
import poplib
import colorama
import os

os.system('cls' if os.name == 'nt' else 'clear')

def preUI():
    global d
    # get the user to select a file to use as the data file
    print(colorama.Fore.GREEN + "Welcome to POPSPY!" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please select a data file to use" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "" + colorama.Fore.RESET)

    file = input("File: ")
    d = data(file)


# UI
def printUI(error=False):
    colorama.init()
    if error == True: print(colorama.Fore.RED + "Invalid choice please try again" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Welcome to the POPSPY User Interface!" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please select an option from below to continue" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "1. Import Account/Accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "2. Export Account/Accounts" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "3. View/Edit Loaded Accounts" + colorama.Fore.RESET)
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
    global d

    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    print(colorama.Fore.GREEN + "IMPORT ACCOUNTS" + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + "Please enter the account details in the below format or provide the name of a txt file with the below format separated with newlines" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "Format: email:password:server" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "Example: example@example.com:password:pop.example.com" + colorama.Fore.RESET)
    print(colorama.Fore.RED + "" + colorama.Fore.RESET)

    accounts = input("Input: ")
    check = input("do you want to check the accounts? (y/n): ")
    if check == "y": check = True
    else: check = False

    if accounts.endswith(".txt"):
        with open(accounts, "r") as f:
            accounts = f.read()
        
        accounts = accounts.split("\n")
        for i in accounts:
            if i == "": accounts.remove(i)
            else: 
                i = i.split(":")
                acc = account(i[0], i[1], i[2], check)
                d.appendAccount(acc)
    
    else:
        accounts = accounts.split(":")
        acc = account(accounts[0], accounts[1], accounts[2], check)
        d.appendAccount(acc)





# print the ui
# printUI()
importAccount()
