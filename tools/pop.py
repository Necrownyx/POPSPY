class account:
    def __init__(self, email, password, server):
        self.email = email # Email address
        self.password = password # Password
        self.server = server # Pop server

        self.messageCount = 0 # Number of messages in inbox
        self.active = self.checkAccount()
        self.lastMessageDate = self.getMessageDate(self.messageCount) # Date of the last message in the inbox
    
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

        message = pop.retr(messageNumber)[1]
        message = str(message)
        message = message.split("\\r\\n")
        print(message)
