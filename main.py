from tools import *
import poplib

# string to import
d = data.loadAccounts()

email = account()
email.importAccount("lboutestanfei198612@rambler.ru:4sH98svjLoK:pop.rambler.ru:True:26:Fri, 07 Apr 2023 07:44:28 +0300")

print(email.getAllSubjects(1, 3))