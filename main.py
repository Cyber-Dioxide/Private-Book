import os, pyfiglet
import sys

from colorama import Fore
import random

black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'
blue = '\033[34m'
purple = '\033[35m'
cyan = '\033[36m'
lightgrey = '\033[37m'
darkgrey = '\033[90m'
lightred = '\033[91m'
lightgreen = '\033[92m'
yellow = '\033[93m'
lightblue = '\033[94m'
pink = '\033[95m'
lightcyan = '\033[96m'
all_col = [red, green, orange, cyan, lightred, lightgreen, yellow, lightcyan,lightblue,pink]
ran = random.choice(all_col)


def banner():
        os.system("clear")
        en = pyfiglet.figlet_format("Private\nBook\n")
        print(ran, en)
        print(ran + "\n\t\tV_1.0\t\n\n")

        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)


banner()


def exit():
    sys.exit()


my_dict = {}

def add_cont():
    name = input(ran + "\nType name for the number: ")
    num = input(ran + "\nType Phone number: ")
    comf = input(ran + "\nDo you want to add more info? [y/n]:")
    if comf == "y":
        email = input(ran + "\nEnter email address: ")
        nickname = input(ran +"\nType nickname for the contact: ")
        company = input(ran +"\nEnter company name: ")
        accounts = input(ran + "\nType other Social Media accounts: ")
        file = open("contacts.txt", "a+")
        file.write("\nName: " + name + f"\nPhone Number: {num} "+"\nEmail: "+email+"\nCompany: "+company + "\nAccounts: "+accounts+"\nNickname: "+nickname)
        file.write("\n" + "- " * 10)
        print(ran + "\n\n\tAdded Successfully!\n")
        print(cyan + "\nExit the tool! Type 'nano contacts.txt' to see saved contacts! :-)")


    else:
        file = open("contacts.txt", "a+")
        file.write("\nName: " + name + f"\nPhone Number: {num} ")
        file.write("\n" + "- " * 10)
        print(ran + "\n\n\tAdded Successfully!\n")
        print(cyan + "\nExit the tool! Type 'nano contacts.txt' to see saved contacts! :-)")
        l = {name: num}
        my_dict.update(l)
        pass


def del_cont():
    name = input(ran + "\nType name of the number: ")
    with open("contacts.txt") as file:
        all_contacts =file.readlines()
        for contacts in all_contacts:
            if name in contacts:
                all_contacts.remove(contacts)

    print(ran+"\nDeleted Successfully!\n")

cont =" "
while cont != "n" and "no":
    print(ran + "\n\t\t[1] Add Contact\n\t\t[2] Delete Contact\n\t\t[3] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        add_cont()
    elif choice == "2":
        del_cont()
    elif choice == "3":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
        print(Fore.CYAN, "- " * 4, " [+] Follow me on Instagram @saadkhan041 ", "- " * 4)
        print(Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @coding_memz ", "- " * 4)
        print(Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Saadkhan041/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()





