'''
This file manages the data for the program. It will load and save the data this is to minimize the amount of time it takes to load the data into the program.
The data is all stored in a single json file.
'''

def loadAccounts(location='data.json'):
    '''loads the data from the data.json file in the local directory unless the user has specified a different location.'''
    # open the file and load the data
    import json

    try:
        with open(location, 'r') as file:
            data = json.load(file)
        # return the data
        return data
    except:
        return {}

def saveAccounts(data={}, location='data.json'):
    '''saves the data to the data.json file in the local directory unless the user has specified a different location.'''
    # open the file and save the data
    import json

    try:
        with open(location, 'w') as file:
            json.dump(data, file)
        return True
    except:
        return False

def loadSettings():
    pass

def saveSettings():
    pass

def loadMessages():
    pass

def saveMessages():
    pass


