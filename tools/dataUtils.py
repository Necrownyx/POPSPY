'''
This file manages the data for the program. It will load and save the data this is to minimize the amount of time it takes to load the data into the program.
The data is all stored in a single json file.
'''
class data:
    def __init__(self, location='data.json'):
        self.location = location
        self.data = self.loadData(location)

        self.accounts = self.data[0]
        self.settings = self.data[1]
        self.messages = self.data[2]
    

    def loadData(self, location='data.json'):
        # check if the file exists
        import os

        if os.path.exists(location):
            # load the data
            import json
            with open(location, 'r') as file:
                data = json.load(file)
            
            # accoutns, settings, messages are all different dictionaries that need to be combined into one dictionary
            self.accounts = data['accounts']
            self.settings = data['settings']
            self.messages = data['messages']

            return [self.accounts, self.settings, self.messages]
        else:
            # create the file
            import json
            data = [{}, {}, {}]

            # accoutns, settings, messages are all different dictionaries that need to be combined into one dictionary
            accounts = data[0]
            settings = data[1]
            messages = data[2]

            d = {'accounts': accounts, 'settings': settings, 'messages': messages}

            try:
                with open(location, 'w') as file:
                    json.dumps(d, file, indent=4)
                return data
            except:
                return None
    
    def saveData(self, location='data.json', d=None):
        import json

        if d == None:
            d = {'accounts': self.accounts, 'settings': self.settings, 'messages': self.messages}

        # overwrite the json file and dump as indented json
        try:
            with open(location, 'w') as file:
                json.dumps(d, file, indent=4)
            return True
        except Exception as e:
            return e

    def appendAccount(self, account):
        self.accounts[len(self.accounts) + 1] = [account.email, account.password, account.server, account.active, account.messageCount, account.lastMessageDate]

        # return the new data
        return [self.accounts, self.settings, self.messages]

    def removeAccount(self, index):
        # find the account in the dictionary
        for i in self.accounts:
            if i == index:
                # remove the account from the dictionary
                del self.accounts[i]
                break
                
        

        # return the new data
        return [self.accounts, self.settings, self.messages]

    def getAccounts(self):
        accounts = []
        for i in self.accounts:
            accounts.append(self.accounts[i])
        return accounts
    
    def getActiveAccounts(self):
        activeAccounts = []
        for i in self.accounts:
            if self.accounts[i][3]:
                activeAccounts.append(self.accounts[i])
        return activeAccounts
    
    def getInactiveAccounts(self):
        inactiveAccounts = []
        for i in self.accounts:
            if not self.accounts[i][3]:
                inactiveAccounts.append(self.accounts[i])
        return inactiveAccounts


