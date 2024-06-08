from modules.banner import *
from modules.menu import *
from modules.iptracker import *
from modules.whois import *
from modules.TrackNumber import *
from modules.emailInfo import *
from colorama import *
from pystyle import *

while True:
    banner()
    menu()
    try:
        choice = int(input(f"{Fore.LIGHTMAGENTA_EX}[Yuno]->{Fore.RESET} "))
        if choice == 1:
            ip = input(f"{Fore.LIGHTMAGENTA_EX}Insert IP:{Fore.RESET} ")
            iptracker(ip)

        elif choice == 2:
            domain = input(f"{Fore.LIGHTMAGENTA_EX}Insert Domain:{Fore.RESET} ")
            Whois(domain)

        elif choice == 3:
            number = input(f"{Fore.LIGHTMAGENTA_EX}Insert Phone Number: {Fore.RESET} ")
            TrackNumber(number)

        elif choice == 4:
            mail = input(f"{Fore.LIGHTMAGENTA_EX}Insert Email: {Fore.RESET} ")
            emailInfo(mail)

        elif choice == 5:
            break
    except Exception as a:
        print("impossible to make this choice: ",a)