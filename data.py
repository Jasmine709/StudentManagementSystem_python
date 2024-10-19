import json

filename='students.data'

def read_data():
    with open(filename, 'r') as file:
        data = json.load(file)  
    return data

def write_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4) 

def get_grade(mark):
    if mark >= 85:
        return "HD"
    elif mark >= 75:
        return "D"
    elif mark >= 65:
        return "C"
    elif mark >= 50:
        return "P"
    else:
        return "N"