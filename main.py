from student import Student
from database import Database

from colorama import Fore, init
init(autoreset=True)

def studentSystem():
    student=Student()
    while True:  
        print(Fore.CYAN + "\tStudent System (l/r/x):",end=" ")
        option = input()
        if option == "l":
            print(Fore.GREEN + "\tStudent Sign In")
            is_login = student.login()
            if is_login:
                while True:
                    print(Fore.CYAN + "\t\tStudent Course Menu (c/e/r/s/x):",end=" ")
                    option_course = input()
                    if option_course == 'c':
                        student.changePassword()
                    elif option_course == 'e':
                        student.enrollCourse()
                    elif option_course == 'r':
                        student.removeCourse()
                    elif option_course == 's':
                        student.showCourse()
                    elif option_course == 'x':
                        break
                    else:
                        print(Fore.RED + "\t\tInvalid option. Please try again.")
        elif option == "r":
            print(Fore.GREEN + "\tStudent Sign Up")
            student.register()
        elif option == "x":
            break
        else:
            print(Fore.RED + "\tInvalid option. Please try again.")

def AdminSystem():
    student_data=Database()
    students = updateList(student_data)

    while True:  
        print(Fore.CYAN + "\tAdmin System (c/g/p/r/s/x):",end=" ")
        option = input()
        if option == "c":
            print(Fore.YELLOW + "\tClearing students database")
            while True:
                print(Fore.RED + "\tAre you sure you want to clear the database (Y)ES/(N)O:",end=" ")
                is_clear=input()
                if is_clear == "Y":
                    student_data.removeAll()
                    print(Fore.YELLOW + "\tStudents data cleared")
                    students = updateList(student_data)
                    break
                elif is_clear =="N":
                    break

        elif option == "g":
            print(Fore.YELLOW + "\tGrade Grouping")
            if len(students) == 0:
                print("\t\t<Nothing to Display>")
            else:
                student_HD, student_D, student_C, student_P, student_Z = [],[],[],[],[]
                for student in students:
                    mean = student.SumMark()
                    if mean >= 85:
                        student_HD.append(student)
                    elif mean >= 75:
                        student_D.append(student)
                    elif mean >= 65:
                        student_C.append(student)
                    elif mean >= 50:
                        student_P.append(student)
                    else:
                        student_Z.append(student)
                
                showGrouping(student_HD,"HD")
                showGrouping(student_D,"D")
                showGrouping(student_C,"C")
                showGrouping(student_P,"P")
                showGrouping(student_Z,"Z")
            
        elif option == "p":
            print(Fore.YELLOW + "\tPASS/FAIL Partition")
            student_pass, student_fail = [],[]
            for student in students:
                mean = student.SumMark()
                if mean >= 50:
                    student_pass.append(student)
                else:
                    student_fail.append(student)

            showPartition(student_pass,"PASS")
            showPartition(student_fail,"FAIL")

        elif option == "r":
            removed_id = input("\tRemove by ID: ")
            if student_data.get('studentID', removed_id) is not None:
                student_data.remove(removed_id)
                students = updateList(student_data)
                print(Fore.YELLOW + f"\tRemoving Student {removed_id} Account")
            else:
                print(Fore.RED + f"\tStudent {removed_id} does not exist")

        elif option == "s":
            print(Fore.YELLOW + "\tStudent List")
            if len(students) == 0:
                print("\t\t<Nothing to Display>")
            else:
                for student in students:
                    print(f"\t{student.fullname} {student.lastname} :: {student.studentID} --> Email: {student.username}")

        elif option == "x":
            break
        
        else:
            print(Fore.RED + "\tInvalid option. Please try again.")

def updateList(student_data):
    students = []
    for student in student_data.data:
        student = Student(student['studentID'],student['username'],student['password'],student['fullname'],student['lastname'],student['subjects'])
        students.append(student)
    return students

def showGrouping(groups,grade):
    if len(groups) > 0:
        i = 1
        print(f"\t{grade} --> [",end="")
        for student in groups:
            print(f"{student.fullname} {student.lastname} :: {student.studentID} --> GRADE: {grade} - MARK: {student.sumMark}",end="")
            if i != len(groups):
                print(", ",end="")
            i+=1
        print("]")

def showPartition(groups,grade):
    i = 1
    print(f"\t{grade} --> [",end="")
    for student in groups:
        print(f"{student.fullname} {student.lastname} :: {student.studentID} --> GRADE: {grade} - MARK: {student.sumMark}",end="")
        if i != len(groups):
            print(", ",end="")
        i+=1
    print("]")

def main():
    while True:  
        print(Fore.CYAN + "University System: (A)dmin, (S)tudent, or (X):",end=" ")
        option = input()
        if option == "A":
            AdminSystem()
            #admin_system.admin_menu()
        elif option == "S":
            studentSystem()
        elif option == "X":
            print(Fore.YELLOW + "Thank You")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()