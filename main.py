import requests, colorama, time, random, os, subprocess, threading
from colorama import Fore, init

init()

request_url = "https://canary.discordapp.com/api/v6/users/@me"
hwid = subprocess.check_output('wmic csproduct get uuid').decode('UTF-8').strip().split('\n')[1]

def doIntro():
    os.system("cls")

    intro = [
        '████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ ',
        '╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗',
        '   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝',
        '   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗',
        '   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║',
        '   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝'
    ]

    spaces = center(len(intro[0]))

    for line in intro:
        print(Fore.RED + spaces + line + Fore.WHITE)

    spaces = center(len("Made by FliIGQ"))

    print(Fore.RED + spaces + "Made by FliiGQ")

    HorizontalLine()

def center(length):
    spaces = ""
    for i in range(int((120/2-length/2))):
        spaces += " "

    return spaces

def HorizontalLine():
    line = ""
    for i in range(120):
        line += "="

    print(Fore.GREEN + line + Fore.WHITE)

def println(text):
    print(f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {text}")

def printlnr(text):
    return f"{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {text}"

def main():
    doIntro()

    tokenFileName = input(printlnr("What is the name of the file with the tokens in? (Example: tokens): "))

    doIntro()

    if not os.path.exists(tokenFileName + ".txt"):
        println("Token file does not exist!")
        println("Press any key to continue...")
        input()
        exit()
    
    try:
        for item in open(tokenFileName + ".txt", "r").readlines():
            CheckToken(item.strip())

        println("All Tokens Checked!")
        println("Press any key to continue...")
        input()
        exit()

    except Exception as e:
        print(e)
        println("An error occurred!")
        println("Press any key to continue...")
        input()
        exit()

def CheckToken(token):
    req = requests.get(request_url, headers={'authorization': token})
    if req.status_code == 401:
        println(f"Invalid: {token}")
    elif req.status_code == 200:
        println(f"Valid: {token}")
        with open("valid.txt", "a") as f:
            f.write(token + "\n")
    else:
        println("An error occurred!")
        println("Press any key to continue...")
        input()
        exit()

main()
