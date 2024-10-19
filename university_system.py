import student_system
import admin_system
from colorama import Fore, init

init(autoreset=True)

def university_menu():
    while True:  # keep until input X
        option = input(Fore.BLUE + "University System: (A)dmin, (S)tudent, or (X): ").lower()
        if option == "a":
            admin_system.admin_menu()
        elif option == "s":
            student_system.student_menu()
        elif option == "x":
            print(Fore.YELLOW + "Thank You")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")
