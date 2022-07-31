import time
import os
import pyautogui
import colorama
from colorama import Fore
os.system(f'cls & mode 85,20 & title JSpammer!')

def main():
    menu()


def menu():
    choice = input(Fore.CYAN + """

 ▄▄▄██▀▀▀██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
   ▒██ ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
   ░██ ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
▓██▄██▓  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
 ▓███▒ ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
 ▒▓▒▒░ ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░ ░ ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
 ░   ░       ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                         
     
Made By Jose#0001                             
[1] Text Spammer
[2] Text Spammer With A Txt
Enter Your Choice ↓
""")
    if choice == "1":
        spammer()
    elif choice == '2':
        txt()
    else:
        print("Enter Right Choice")
        time.sleep(3)
        menu()



def spammer():
    print(Fore.GREEN + 'This Is Just A Regular Text Spammer')
    message = input(Fore.CYAN + "Enter Your Message: ")
    spam = input(Fore.CYAN + "How Many Messages You Want To Spam: ")
    print(Fore.YELLOW + "Please Wait 5 Secs Before The Spam Starts")
    time.sleep(5)
    
    for i in range(0,int(spam)):
        pyautogui.typewrite(message + '\n')


def txt():
     print(Fore.GREEN + 'This Is A Text Spammer You Can Open A Txt File And Spam With It')
     file = input(Fore.CYAN + "Enter The Name Of The Txt File:")
     file = open(file, "r")
     print(Fore.YELLOW + "Please Wait 5 Secs Before The Spam Starts")
     time.sleep(5)
     for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")

main()
