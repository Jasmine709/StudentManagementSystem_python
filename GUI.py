import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import Database
from student import Student
from subject import Subject

import re

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="Login Page", font=("Arial Bold",15))
        Label.place(x=200, y=50)

        #email
        L1 = tk.Label(self, text="Email", font=("Arial",10))
        L1.place(x=100, y=100)
        T1 = tk.Entry(self, width=30, bd=5)
        T1.place(x=200, y=100)

        #password
        L2 = tk.Label(self, text="Password", font=("Arial",10))
        L2.place(x=100, y=150)
        T2 = tk.Entry(self, width=30, show="*", bd=5)
        T2.place(x=200, y=150)

        def verity():
            email = T1.get()
            password = T2.get()

            # validate email and password
            email_format = r"^[a-zA-Z0-9._%+-]+\.[a-zA-Z0-9._%+-]+@university\.com$"
            password_format = r"^[A-Z][a-zA-Z]{5,}\d{3,}$"

            if re.match(password_format, password) and re.match(email_format, email):
                database = Database()
                student_data = database.get('username', email)

                if student_data is None:
                    messagebox.showerror("Error", "Student does not exists")
                elif student_data['username'] != email or student_data['password']!=password:
                    messagebox.showerror("Error", "Student does not exists
                else:
                    student.studentID = student_data['studentID']
                    student.username = student_data['username']
                    student.password = student_data['password']
                    student.fullname = student_data['fullname']
                    student.lastname = student_data['lastname']
                    student.subjects = student_data['subjects']

                    controller.show_frame(MainPage)
                    controller.frames[MainPage].get_name()
                    controller.frames[MainPage].get_enroll_list()
            else:
                messagebox.showerror("Error", "Incorrect email or password format")

        Button = tk.Button(self, text="Login", font=("Arial Bold",10), command=verity)
        Button.place(x=200, y=450)

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.Label = tk.Label(self, text="", font=("Arial Bold",15))
        self.Label.place(x=150, y=50)

        self.subjectsTitle = tk.Label(self, text="Enrolled Subject", font=("Arial Bold",15))
        self.subjectsTitle.place(x=150, y=80)

        self.subjectList = []
        position=200
        for i in range(0,4):
            label = tk.Label(self, text="", font=("Arial",15))
            label.place(x=50, y=position)
            self.subjectList.append(label)
            position += 50

        self.Button = tk.Button(self, text="Logout", command=lambda: controller.show_frame(LoginPage))
        self.Button.place(x=400, y=10)

        def enroll():
            subject = Subject()
            subject.subjectID = subject.generateSubjectID()
            subject.mark = subject.generateMark()
            new_subject = {
                "subjectID": subject.subjectID,
                "mark": subject.mark
            }

            if len(student.subjects) == 4:
                messagebox.showerror("Error", "Students are allowed to enrol in 4 subjects only")
            else:
                student.subjects.append(new_subject)
                student.updateSubject()
                messagebox.showinfo("Enroll", f"Enrolling in subject-{subject.subjectID}")
                self.get_enroll_list()

        Button = tk.Button(self, text="Enroll", font=("Arial Bold",10), command=enroll)
        Button.place(x=200, y=150)

    def get_name(self):
        student_name = student.fullname+" "+student.lastname
        greeting_text = "Hello, "+student_name
        self.Label.config(text=greeting_text)

    def get_enroll_list(self):
        i = 0
        for subject in student.subjects:
            this_subject=Subject(subject['subjectID'],subject['mark'])
            subject_text = f"Subject::{this_subject.subjectID} -- mark = {this_subject.mark} -- grade = {this_subject.grading()}" 
            self.subjectList[i].config(text=subject_text)
            i+=1


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=500)

        self.frames = {}
        for F in (LoginPage, MainPage):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
    
if __name__ == "__main__":
    student = Student()
    app = Application()
    app.mainloop()
