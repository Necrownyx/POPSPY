from tools import *
import poplib
import colorama
import os

os.system('cls' if os.name == 'nt' else 'clear')

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



# print the ui
printUI()
