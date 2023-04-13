'''
This file manages the data for the program. It will load and save the data this is to minimize the amount of time it takes to load the data into the program.
The data is all stored in a single json file.
'''
class data:
    def __init__(self, location='data.json'):
        self.location = location
        self.data = self.loadData(location)

        if self.data != None:
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
            d = {'accounts': {}, 'settings': {}, 'messages': {}}

            try:
                json_file = open(location, 'w')
                json_file.write(json.dumps(d, indent=4))
                json_file.close()

                self.accounts = d['accounts']
                self.settings = d['settings']
                self.messages = d['messages']
                return [d['accounts'], d['settings'], d['messages']]
            except:
                return None
    
    def saveData(self, location='data.json', d=None):
        import json

        d = {'accounts': d[0], 'settings': d[1], 'messages': d[2]}

        # overwrite the json file and dump as indented json
        try:
            json_file = open(location, 'w')
            json_file.write(json.dumps(d, indent=4))
            json_file.close()
            return True
        except Exception as e:
            return e

    def appendAccount(self, account):
        self.accounts[len(self.accounts) + 1] = [account.email, account.password, account.server, account.active, account.messageCount, account.lastMessageDate]

        # save the data to the file
        self.saveData(self.location, [self.accounts, self.settings, self.messages])

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

    def loadAccounts(self):
        from tools.pop import account
        # load the account from the dictionary and create it into a account object
        accounts = []
        for i in self.accounts:
            temp = account()
            temp2 = temp.importAccountFromList(self.accounts[i])
            accounts.append(temp2)
        return accounts

    
        

