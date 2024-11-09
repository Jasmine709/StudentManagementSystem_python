from colorama import Fore, init
import re
import random

from database import Database
from subject import Subject

class Student():
    def __init__(self,studentID = None, username = None, password = None, fullname = None, lastname = None, subjects = [],sumMark = None):
        self.studentID = studentID
        self.username = username
        self.password = password
        self.fullname = fullname
        self.lastname = lastname
        self.subjects = subjects
        self.sumMark = sumMark

    def __str__(self):
        return (f"\t{self.fullname} {self.lastname} :: {self.studentID} --> Email: {self.username}")

    def getEmailPassword(self):
        while True:
            #get info from user
            email = str(input('\tEmail : ')).strip()
            password = str(input('\tPassword:')).strip()

            # validate email and password
            email_format = r"^[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+@university\.com$"
            password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"

            if re.match(password_format, password) and re.match(email_format, email):
                print(Fore.YELLOW + "\temail and password formats acceptable")
                return email, password
            else:
                print(Fore.RED + "\tIncorrect email or password format")
        
    def register(self):
        email, password = self.getEmailPassword()

        database = Database()

        student_data = database.get('username', email)
        if student_data is not None:
            print(Fore.RED + f"\tStudent {student_data['fullname']} {student_data['lastname']} already exists")
        else:
            while True:
                studentID = self.generateStudentID()
                studentID_data = database.get('studentID',studentID)
                if studentID_data is None:
                    break
            fullname, lastname = email.split('@')[0].split('.')
            fullname=fullname.capitalize()
            lastname=lastname.capitalize()

            database.addNew(studentID, email, password, fullname, lastname)

            print(f"\tName: {fullname} {lastname}")
            print(Fore.YELLOW + f"\tEnrolling Student {fullname} {lastname}")

    def generateStudentID(self):
        student_id = random.randint(1,999999)
        return str(student_id).zfill(6)

    
    def login(self):
        email, password = self.getEmailPassword()

        database = Database()
        student_data = database.get('username', email)

        if student_data is None:
            print(Fore.RED + f"\tStudent does not exists")
            return False
        elif student_data['username'] != email or student_data['password']!=password:
            print(Fore.RED + f"\tStudent does not exists")
            return False
        else:
            self.studentID = student_data['studentID']
            self.username = student_data['username']
            self.password = student_data['password']
            self.fullname = student_data['fullname']
            self.lastname = student_data['lastname']
            self.subjects = student_data['subjects']
            return True

    def showCourse(self):
        print(Fore.YELLOW+ f"\t\tShowing {len(self.subjects)} subjects")
        if len(self.subjects) != 0:
            for subject in self.subjects:
                this_subject=Subject(subject['subjectID'],subject['mark'])
                print(this_subject)

    def updateSubject(self):
        student_data = Database()
        student_data.update(
            target='username',
            keyword=self.username,
            update_target='subjects',
            new_data=self.subjects
        )

    def enrollCourse(self):
        subject = Subject()
        subject.subjectID = subject.generateSubjectID()
        subject.mark = subject.generateMark()
        new_subject = {
            "subjectID": subject.subjectID,
            "mark": subject.mark
        }

        if len(self.subjects) < 4:
            self.subjects.append(new_subject)

            self.updateSubject()
            
            print(Fore.YELLOW+ f"\t\tEnrolling in subject-{subject.subjectID}")
            self.getNumberOfSubject()
        else:
            print(Fore.RED+"\t\tStudents are allowed to enrol in 4 subjects only")

    def getNumberOfSubject(self):
        print(Fore.YELLOW+ f"\t\tYou are now enrolled in {len(self.subjects)} out of 4 subjects")

    def removeCourse(self):
        while True:
            remove_subject = str(input(f"\t\tRemove Subject by ID or 'x' to exit: "))
            if remove_subject == 'x':
                break
            else:
                get_subject=[subject for subject in self.subjects if subject.get('subjectID')==remove_subject]
                if len(get_subject) != 0:  
                    get_subject=get_subject[0]
                    self.subjects.remove(get_subject)
                    print(Fore.YELLOW+f"\t\tDroping Subject-{remove_subject}")
                    self.getNumberOfSubject()
                    self.updateSubject()
                else:
                    print(Fore.RED+f"\t\tThere is no subject-{remove_subject}")
                break

    def changePassword(self):  
        print(Fore.YELLOW + "\t\tUpdating Password ('x' to exit)")
        while True:
            new_password = input("\t\tNew Password: ")
            
            password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"
            if new_password == 'x':   
                break
            elif not re.match(password_format, new_password):
                print(Fore.RED + "\t\tIncorrect password format")
            else:
                while True:
                    confirm_password = input("\t\tConfirm Password: ")
                    if new_password != confirm_password:
                        print(Fore.RED + "\t\tPassword does not match - try again")
                    else:
                        student_data = Database()
                        student_data.update('username', self.username, 'password', new_password)
                        break
                break
                
        
    def SumMark(self):
        sum = 0
        for subject in self.subjects:
            sum = sum + int(subject['mark'])
        mean = sum/len(self.subjects)
        self.sumMark = mean
        return mean