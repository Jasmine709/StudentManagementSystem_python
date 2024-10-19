from colorama import Fore, init
import data
import re

init(autoreset=True)

def course_menu(student):
    while True:
        choice = input(Fore.BLUE + "\t\tStudent Course Menu (c/e/r/s/x): ").lower()
        if choice == 'c':
            print(Fore.YELLOW + "\t\tUpdating Password")
            change(student)
        elif choice == 'e':
            enrol(student)
        elif choice == 'r':
            remove(student)
        elif choice == 's':
            show(student)
        elif choice == 'x':
            break
        else:
            print(Fore.RED + "\t\tInvalid option. Please try again.")

# enables a student to change their password
def change(student):
    new_password = input(Fore.BLACK + "\t\tNew Password: ")

    #format match
    password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"
    if not re.match(password_format, new_password):
        print(Fore.RED + "\t\tIncorrect password format")
        change(student)
        return
    confirm_password = input(Fore.BLACK + "\t\tConfirm Password: ")

    if new_password != confirm_password:
        print(Fore.RED + "\t\tPassword does not match - try again")
        change(student)
    else:
        student["password"] = new_password
        student_data = data.read_data()
        for s in student_data:
            if s["studentID"] == student["studentID"]:
                s["password"] = new_password
        data.write_data(student_data)

# Student enrols in a subject. A student can enrol in maximum 4 subjects.
def enrol(student):
    return 0      
  
# Student can remove a subject from the subjects’ enrolment list
def remove(student):
    return 0

# Shows the enrolled subjects and the marks and grades for each subject
def show(student):
    return 0     