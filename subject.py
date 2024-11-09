import random

class Subject():
    def __init__(self, subjectID=None, mark=0):
        self.subjectID = subjectID
        self.mark = int(mark)

    def __str__(self):
        return (f"\t\t[ Subject::{self.subjectID} -- mark = {self.mark} -- grade = {self.grading()}]")
    
    def grading(self):
        if self.mark >= 85:
            return 'HD'
        elif self.mark >= 75:
            return 'D'
        elif self.mark >= 65:
            return 'C'
        elif self.mark >= 50:
            return 'P'
        else:
            return 'Z'
        
    def generateSubjectID(self):
        subject_id = random.randint(1,999)
        return str(subject_id).zfill(3)
    
    def generateMark(self):
        return str(random.randint(25, 100))
    