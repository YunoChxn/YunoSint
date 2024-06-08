import phonenumbers
from colorama import *
from phonenumbers import carrier, geocoder 

def TrackNumber(number):
    try:
        phone = phonenumbers.parse(number)
        valid_number = phonenumbers.is_valid_number(phone)
        possible = phonenumbers.is_possible_number(phone)
        Carrier = carrier.name_for_number(phone, lang=("it","en"))
        Region = geocoder.description_for_number(phone, lang=("it","en"))
        print(f"""
{Fore.LIGHTMAGENTA_EX}NUMBER: {Fore.LIGHTCYAN_EX}{number}
{Fore.LIGHTMAGENTA_EX}VALID NUMBER: {Fore.LIGHTCYAN_EX}{valid_number}
{Fore.LIGHTMAGENTA_EX}POSSIBLE NUMBER: {Fore.LIGHTCYAN_EX}{possible}
{Fore.LIGHTMAGENTA_EX}CARRIER: {Fore.LIGHTCYAN_EX}{Carrier}
{Fore.LIGHTMAGENTA_EX}REGION: {Fore.LIGHTCYAN_EX}{Region}{Fore.RESET}""")
    except Exception as a:
        print("Error: ",a)