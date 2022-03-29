import os, pyfiglet
import sys

from colorama import Fore , Style
import random

all_col= [Style.BRIGHT+Fore.RED,Style.BRIGHT+Fore.CYAN,Style.BRIGHT+Fore.LIGHTCYAN_EX, Style.BRIGHT+Fore.LIGHTBLUE_EX, Style.BRIGHT+Fore.LIGHTCYAN_EX,Style.BRIGHT+Fore.LIGHTMAGENTA_EX,Style.BRIGHT+Fore.LIGHTYELLOW_EX]

ran = random.choice(all_col)


def banner():
    os.system("clear")

    print(ran, pyfiglet.figlet_format("\tPrivate\n\tBook"))


    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3)


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
        print(Fore.CYAN + "\nExit the tool! Type 'nano contacts.txt' to see saved contacts! :-)")


    else:
        file = open("contacts.txt", "a+")
        file.write("\nName: " + name + f"\nPhone Number: {num} ")
        file.write("\n" + "- " * 10)
        print(ran + "\n\n\tAdded Successfully!\n")
        print(Fore.LIGHTMAGENTA_EX + "\nExit the tool! Type 'nano contacts.txt' to see saved contacts! :-)")
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

def view():
    file = open("contacts.txt" , "r")
    read = file.read()

    print(ran + "\n\t\tThis is what i found: \n")

    print(ran + read)

cont =" "
while cont != "n" and "no":
    print(ran + "\n\t\t[1] Add Contact\n\t\t[2] Delete Contact\n\t\t[3] View Contatct\n\t\t[4] Exit\n ")

    choice = input(ran + "Enter your choice: ")
    if choice == "1":
        add_cont()
    elif choice == "2":
        del_cont()

    elif choice == "3":
        view()

    elif choice == "4":
        print(ran + "\n\tDont Forget to do following tasks :-)\t\n")
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX, "\n", "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4)
    print(Style.BRIGHT + Fore.LIGHTRED_EX, "\n", "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3)
        exit()

    else:
        print(ran + "\nInvalid option")
        exit()
    cont = input(ran + "\nDo you want to continue? [y/n]:")

    if cont == "y":
        os.system("clear")
        banner()





