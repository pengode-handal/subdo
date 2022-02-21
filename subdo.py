from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests, argparse

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
url = 'https://sonar.omnisint.io/subdomains/'

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls
    
parser = argparse.ArgumentParser()

parser.add_argument('-d', '--domain', metavar='DOMAIN', help='Target domain')
parser.add_argument('-ld', '--list', metavar='List Domain', help='List target')

arg = parser.parse_args()
def subdoscan(dom: str):
    target = dom.replace('http://','').replace('https://','').split('/')[0]
    res = requests.get(url + target).text
    if 'null' in res:
        print(f'\n\n{red}{target} Maybe Down')
    else:
        result = res.replace('"', '').replace('[','').replace(']','').replace(',','\n')
        garis = result.splitlines()
        print(c+result)
        print(f'\n{b}Total subdomain: {str(len(garis))}')
        



if arg.domain:
    subdoscan(arg.domain)
elif arg.list:
    target = getUrl(arg.list)
    for lis in target:
        print(w+'\n=======================================')
        subdoscan(lis)
else:
    print(red+'Usage: subdo.py [-h] [-d DOMAIN] [-ld List Domain]')
