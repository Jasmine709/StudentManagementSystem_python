import json

class Database():
    
    def __init__(self):
        # load all data 
        with open('students.data') as json_file:
            self.data = json.load(json_file)

    def get(self, target, keyword):
        for user in self.data:
            if user[target] == keyword:
                return user
        return None
    
    def save(self):
        with open('students.data', mode='w') as f:
            f.write(json.dumps(self.data, indent=2))
            
    def addNew(self, studentID,username, password, fullname, lastname):
        new_user= {
            "studentID" : str(studentID),
            "fullname": fullname,
            "lastname": lastname,
            "username": username,
            "password": password,
            "subjects" : [],
        }
        self.data.append(new_user)
        self.save()

    def update(self, target, keyword, update_target, new_data):
        for user in self.data:
            if user[target] == keyword:
                user[update_target] = new_data
                self.save()
                return True
        return False
    
    def remove(self,studentID):
        for user in self.data:
            if user['studentID'] == studentID:
                self.data.remove(user)
                self.save()
                return True
        return False

    def removeAll(self):
        removes = []
        for user in self.data:
            removes.append(user)

        for target in removes:
            self.data.remove(target)
        self.save()
