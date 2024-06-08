from email_validator import *
import requests
from colorama import *


def emailInfo(email):
    try:
        mail = requests.get(f"https://emailrep.io/{email}")
        data = mail.json()
        print(f"""
{Fore.LIGHTMAGENTA_EX}EMAIL: {Fore.LIGHTCYAN_EX}{email}{Fore.RESET}
─── ･ ｡ﾟ⟡ ⛩️ ⟡ ˚｡ ･ ───
{Fore.LIGHTMAGENTA_EX}{data}{Fore.RESET}""")
    except Exception as a:
        print("Error: ",a)






