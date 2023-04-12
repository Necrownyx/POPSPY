class account:
    def __init__(self, email, password, server):
        self.email = email # Email address
        self.password = password # Password
        self.server = server # Pop server


        self.active = self.checkAccount()
        if self.active:
            self.messageCount = self.getMessageCount() # Number of messages in the inbox
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

        # use pop.top() to get the first 100 lines of the message
        message = pop.top(messageNumber, 10)
        return message[1][0]

