'''
This file manages the data for the program. It will load and save the data this is to minimize the amount of time it takes to load the data into the program.
The data is all stored in a single json file.
'''
def loadData(location='data.json'):
    # check if the file exists
    import os

    if os.path.exists(location):
        # load the data
        import json
        with open(location, 'r') as file:
            data = json.load(file)
        accounts = data['accounts']
        settings = data['settings']
        messages = data['messages']

        d = [accounts, settings, messages]
        return d
    else:
        # create the file and rerun the function
        saveData(None)
        return loadData(location)
    
def saveData(data, location='data.json'):
    import json

    # if the data is None then create a new data file
    if data == None:
        data = [{}, {}, {}]



    # accoutns, settings, messages are all different dictionaries that need to be combined into one dictionary
    accounts = data[0]
    settings = data[1]
    messages = data[2]

    d = {'accounts': accounts, 'settings': settings, 'messages': messages}

    try:
        # dump as indented json
        with open(location, 'w') as file:
            json.dump(d, file, indent=4)
        return True
    except:
        return False


