import whois
from colorama import *




def Whois(domain):
    try:
        w = whois.whois(domain)
        print(Fore.LIGHTMAGENTA_EX, w, Fore.RESET) 
    except Exception as a:
        print("Error: ",a)
    