from colorama import Fore, init

init(autoreset=True)

def admin_menu():
    while True:
        choice = input(Fore.BLUE + "\tAdmin System (c/g/p/r/s/x): ").lower()
        if choice == 'c':
            clear_database_file()
        elif choice == 'g':
            group_students()
        elif choice == 'p':
            partition_students()
        elif choice == 'r':
            remove_student()
        elif choice == 's':
            show()
        elif choice == 'x':
            break
        else:
            print(Fore.RED + "\tInvalid option. Please try again.")

# enables admin to clear the data file “students.data”
def clear_database_file():
    return 0

# shows the students organized with respect to the grade
def group_students():
    return 0        

# shows the pass/fail distribution
def partition_students():
    return 0

# enables admin to remove a student by ID
def remove_student():
    return 0     

# show the students from the data file
def show():
    return 0
     