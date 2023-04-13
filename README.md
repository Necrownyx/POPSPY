# POPSPY

Program that uses the [poplib](https://docs.python.org/3/library/poplib.html) module to check for new emails in a POP3 server and check them for keywords.
- Can be used on compromised accounts to retrive password reset links and codes.
- Can be used to search recieved emails to find what services the user is subscribed to.

## Usage
The program has a simple ui that allows for use by non-technical users. However it has been created to be extremely modular allowing for custom scripts to be created to perform more advanced and specific tasks.

### Using the User Interface
The program can be run by executing the `main.py` file. The program will then ask for the name of the data file to use leave blank to use 'data.json'.
<br>
the user is then presented with a menu that allows them to select what they want to do.
the user interface is currently in development and is not yet complete so it does not have all the features that are possible.
<br>
The current features are:
- Add a new account
- View all accounts
- Search for a keyword in all accounts

### Creating a custom script
The program is designed to be modular allowing for custom scripts to be created to perform more advanced tasks.
<br>
To create a custom script create a python file in the main directory and include the below code to the top of the file.
```python
from tools import *
```
<br>
This will import all the functions from the tools file allowing you to use them in your script.
<br>
## Tools Documentation
The tools folder contains all the functions that are used by the program and can be used by custom scripts. 
