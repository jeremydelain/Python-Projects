#parent class
class User:
    name = ''
    email = ''
    password = ''
    id = 0

#child class
class Teacher(User):
    subject = ''
    salary = 0

#child class
class Student(User):
    grade = 0
    gpa = 0
    
