# Scripts
This directory contains scripts that can be used to obtain the log in information for a user's email account.

## brute_force.py
this file uses the list of 10000 most common passwords and tries to log in to the user's email account. If the password is correct, the script will print the password to the console.

## webhook_generator.py
this file generates a encoded exec() string that imports requests and sends a POST request to a webhook. This string can be used in any python file to send a variable present in the file to a webhook.