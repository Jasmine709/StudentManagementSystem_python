import student_course_system
from colorama import Fore, init
import re
import data

init(autoreset=True)

def student_menu():
    while True:
        choice = input(Fore.BLUE + "\tStudent System (l/r/x): ").lower()
        if choice == 'l':
            print(Fore.GREEN + "\tStudent Sign In")
            login()
        elif choice == 'r':
            print(Fore.GREEN + "\tStudent Sign Up")
            register()
        elif choice == 'x':
            break
        else:
            print(Fore.RED + "\tInvalid option. Please try again.")

'''
Students should be able to register. Email and password should be verified against pattern 
rules. Then the student should be checked if they exist. Only register students that do not 
exist in the Database file. On registration, student data should be stored in “students.data”. 
'''
def register():
    email = input(Fore.BLACK + "\tEmail: ")
    password = input(Fore.BLACK + "\tPassword: ")
    
    #format match
    email_format = r"^[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+@university\.com$"
    password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"
    if not re.match(password_format, password) or not re.match(email_format, email):
        print(Fore.RED + "\tIncorrect email or password format")
        register()
    else:
        print(Fore.YELLOW + "\temail and password formats acceptable")

    # check whether exist
    student_data = data.read_data()
    for student in student_data:
        if student["username"] == email:
            print(Fore.RED + f"\tStudent {student['fullname']} {student['lastname']}already exists")
            return
        
    # create a new student
    fullname, lastname = email.split('@')[0].split('.')
    student_id = str(len(student_data) + 1).zfill(6)  
    new_student = {
        "studentID": student_id,
        "fullname": fullname,
        "lastname": lastname,
        "username": email,
        "password": password,
        "subjects": []  
    }
    student_data.append(new_student)  
    data.write_data(student_data)
    print(Fore.YELLOW + f"\tEnrolling Student {fullname} {lastname}") 


'''
Students should be able to login. Then the student should be checked if they exist. Only a 
registered student should login. Upon login, students' data should be read from 
“students.data”. After login, a student goes to Student Course Menu.
'''
def login():
    email = input(Fore.BLACK + "\tEmail: ")
    password = input(Fore.BLACK + "\tPassword: ")

    #format match
    email_format = r"^[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+@university\.com$"
    password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"
    if not re.match(password_format, password) or not re.match(email_format, email):
        print(Fore.RED + "\tIncorrect email or password format")
        register()
    else:
        print(Fore.YELLOW + "\temail and password formats acceptable")

    # check whether exist and enter course system
    student_data = data.read_data()
    for student in student_data:
        if student["username"] == email and student["password"] == password:
            student_course_system.course_menu(student)
            return
        else: 
            print(Fore.RED + "\tStudent does not exist")
            return