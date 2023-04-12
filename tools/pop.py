class account:
    def __init__(self, email, password, server):
        self.email = email # Email address
        self.password = password # Password
        self.server = server # Pop server

        self.messagecount = 0 # Number of messages in inbox
        self.lastMessageDate = 0 # Unix time of last message
        self.active = self.checkAccount()
    
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

            self.messagecount = len(pop.list()[1])
            self.lastMessageDate = pop.stat()[2]
            print(self.lastMessageDate)

            pop.quit()
            return True
        except:
            return False
    
