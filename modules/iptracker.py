import requests
from colorama import *
from pystyle import *

def iptracker(ip):
    try:
        status = requests.get(f"http://ip-api.com/json/{ip}?fields=status")
        message = requests.get(f"http://ip-api.com/json/{ip}?fields=message")
        continent = requests.get(f"http://ip-api.com/json/{ip}?fields=continent")
        continentCode = requests.get(f"http://ip-api.com/json/{ip}?fields=continentCode")
        country = requests.get(f"http://ip-api.com/json/{ip}?fields=country")
        countryCode = requests.get(f"http://ip-api.com/json/{ip}?fields=countryCode")
        region = requests.get(f"http://ip-api.com/json/{ip}?fields=region")
        regionName = requests.get(f"http://ip-api.com/json/{ip}?fields=regionName")
        city = requests.get(f"http://ip-api.com/json/{ip}?fields=city")
        district = requests.get(f"http://ip-api.com/json/{ip}?fields=district")
        zip = requests.get(f"http://ip-api.com/json/{ip}?fields=zip")
        lat = requests.get(f"http://ip-api.com/json/{ip}?fields=lat")
        lon = requests.get(f"http://ip-api.com/json/{ip}?fields=lon")
        timezone = requests.get(f"http://ip-api.com/json/{ip}?fields=timezone")
        offset = requests.get(f"http://ip-api.com/json/{ip}?fields=offset")
        currency = requests.get(f"http://ip-api.com/json/{ip}?fields=currency")
        isp = requests.get(f"http://ip-api.com/json/{ip}?fields=isp")
        org = requests.get(f"http://ip-api.com/json/{ip}?fields=org")
        As = requests.get(f"http://ip-api.com/json/{ip}?fields=as")
        asname = requests.get(f"http://ip-api.com/json/{ip}?fields=asname")
        reverse = requests.get(f"http://ip-api.com/json/{ip}?fields=reverse")
        mobile = requests.get(f"http://ip-api.com/json/{ip}?fields=mobile")
        proxy = requests.get(f"http://ip-api.com/json/{ip}?fields=proxy")
        hosting = requests.get(f"http://ip-api.com/json/{ip}?fields=hosting")
        query = requests.get(f"http://ip-api.com/json/{ip}?fields=query")
        print(f"""
{Fore.LIGHTCYAN_EX}STATUS: {Fore.LIGHTMAGENTA_EX}{status.content}
{Fore.LIGHTMAGENTA_EX}MESSAGE: {Fore.LIGHTCYAN_EX}{message.content}
{Fore.LIGHTCYAN_EX}CONTINENT: {Fore.LIGHTMAGENTA_EX}{continent.content}
{Fore.LIGHTMAGENTA_EX}CONTINENT CODE: {Fore.LIGHTCYAN_EX}{continentCode.content}
{Fore.LIGHTCYAN_EX}COUNTRY: {Fore.LIGHTMAGENTA_EX}{country.content}
{Fore.LIGHTMAGENTA_EX}COUNTRY CODE: {Fore.LIGHTCYAN_EX}{countryCode.content}
{Fore.LIGHTCYAN_EX}REGION: {Fore.LIGHTMAGENTA_EX}{region.content}
{Fore.LIGHTMAGENTA_EX}REGION NAME: {Fore.LIGHTCYAN_EX}{regionName.content}
{Fore.LIGHTCYAN_EX}CITY: {Fore.LIGHTMAGENTA_EX}{city.content}
{Fore.LIGHTMAGENTA_EX}DISTRICT: {Fore.LIGHTCYAN_EX}{district.content}
{Fore.LIGHTCYAN_EX}ZIP: {Fore.LIGHTMAGENTA_EX}{zip.content}
{Fore.LIGHTMAGENTA_EX}LAT: {Fore.LIGHTCYAN_EX}{lat.content}
{Fore.LIGHTCYAN_EX}LON: {Fore.LIGHTMAGENTA_EX}{lon.content}
{Fore.LIGHTMAGENTA_EX}TIMEZONE: {Fore.LIGHTCYAN_EX}{timezone.content}
{Fore.LIGHTCYAN_EX}OFFSET: {Fore.LIGHTMAGENTA_EX}{offset.content}
{Fore.LIGHTMAGENTA_EX}CURRENCY: {Fore.LIGHTCYAN_EX}{currency.content}
{Fore.LIGHTCYAN_EX}ISP: {Fore.LIGHTMAGENTA_EX}{isp.content}
{Fore.LIGHTMAGENTA_EX}ORG: {Fore.LIGHTCYAN_EX}{org.content}
{Fore.LIGHTCYAN_EX}AS: {Fore.LIGHTMAGENTA_EX}{As.content}
{Fore.LIGHTMAGENTA_EX}ASNAME: {Fore.LIGHTCYAN_EX}{asname.content}
{Fore.LIGHTCYAN_EX}REVERSE: {Fore.LIGHTMAGENTA_EX}{reverse.content}
{Fore.LIGHTMAGENTA_EX}MOBILE: {Fore.LIGHTCYAN_EX}{mobile.content}
{Fore.LIGHTCYAN_EX}PROXY: {Fore.LIGHTMAGENTA_EX}{proxy.content}
{Fore.LIGHTMAGENTA_EX}HOSTING: {Fore.LIGHTCYAN_EX}{hosting.content}
{Fore.LIGHTCYAN_EX}QUERY: {Fore.LIGHTMAGENTA_EX}{query.content}""")
    except Exception as a:
        print("Impossible track ip")