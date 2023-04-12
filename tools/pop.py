'''
This file manages the email accounts and gives them specific functions.
'''
class account:
    def __init__(self, email = None, password = None, server = None, check = True):
        self.email = email # Email address
        self.password = password # Password
        self.server = server # Pop server

        if email == None and password == None and server == None:
            self.active = False
            self.messageCount = 0
            self.lastMessageDate = None
            return

        if check:
            self.active = self.checkAccount()
            if self.active:
                self.messageCount = self.getMessageCount() # Number of messages in the inbox
                self.lastMessageDate = self.getMessageDate(self.messageCount) # Date of the last message in the inbox
            else:
                self.messageCount = 0
                self.lastMessageDate = None
        else:
            self.active = True
            self.messageCount = 0
            self.lastMessageDate = None
    
    def exportAccount(self):
        '''Returns a string with the account information.'''
        return self.email + ":" + self.password + ":" + self.server + ":" + str(self.active) + ":" + str(self.messageCount) + ":" + self.lastMessageDate

    def importAccount(self, account):
        '''Imports an account from a string.'''
        account = account.split(":")
        self.email = account[0]
        self.password = account[1]
        self.server = account[2]
        self.active = bool(account[3])
        self.messageCount = int(account[4])
        self.lastMessageDate = account[5]
        return self

    def checkAccount(self):
        '''Checks if the account is valid by trying to connect to the server and log in.
            IF the account is valid, it will return True, otherwise it will return False.
            it also sets the messagecount variable to the number of messages in the inbox.
        '''
        import poplib
        try:
            pop = poplib.POP3(self.server)
            pop.user(self.email)
            pop.pass_(self.password)

            self.messagecount = pop.stat()[0]

            pop.quit()
            return True
        except:
            return False
        
    def getMessageCount(self):
        '''Returns the number of messages in the inbox.'''
        import poplib
        pop = poplib.POP3(self.server)
        pop.user(self.email)
        pop.pass_(self.password)

        messageCount = pop.stat()[0]
        pop.quit()
        return messageCount
    
    def getWelcomeMessage(self):
        '''Returns the welcome message from the server.'''
        import poplib
        pop = poplib.POP3(self.server)
        pop.user(self.email)
        pop.pass_(self.password)

        welcomeMessage = pop.getwelcome()
        pop.quit()
        return welcomeMessage
    
    def getMessageDate(self, messageNumber):
        '''Returns the date of a specific message.
            messageNumber is the number of the message in the inbox.
        '''
        import poplib
        pop = poplib.POP3(self.server)
        pop.user(self.email)
        pop.pass_(self.password)

        message = pop.retr(messageNumber)
        message = str(message)
        message = message[0:600]
        message = message.split(";")
        for part in message:
            if " Mon" in part or " Tue" in part or " Wed" in part or " Thu" in part or " Fri" in part or " Sat" in part or " Sun" in part:
                message = part
                break
        message = message[0:32]
        message = message[1:]
        return message
    
    def getMessageSubject(self, messageNumber):
        '''Returns the subject of a specific message.
            messageNumber is the number of the message in the inbox.
        '''
        import poplib
        pop = poplib.POP3(self.server)
        pop.user(self.email)
        pop.pass_(self.password)

        message = pop.top(messageNumber, 1)
        message = message[1]
        for part in message:
            if b'Subject: ' in part:
                message = part
                break
        message = str(message)
        message = message[2:-1]
        message = message[9:]
        return message

    def getAllSubjects(self, rangemin = None, rangemax = None):
        '''Returns a list of all the subjects in the inbox.'''
        if rangemin == None:
            rangemin = 0
        if rangemin <= 0:
            rangemin = 0

        if rangemax == None:
            rangemax = self.messageCount
        if rangemax > self.messageCount:
            rangemax = self.messageCount
        

        subjects = []
        for i in range(rangemin, rangemax + 1):
            subjects.append(self.getMessageSubject(i))
        return subjects

