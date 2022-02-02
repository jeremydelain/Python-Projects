#parent class
class User:
    name = ''
    email = ''
    password = ''

    def login(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if(email == self.email and password == self.password):
            print("Hello, {}.".format(name))
        else:
            print("Incorrect email or password")

#child class
class Teacher(User):
    subject = ''
    salary = 0
    facultyID = 0

    def login(self):
        name = input("Enter your name: ")
        id = input("Enter your Faculty ID: ")
        if(id == self.facultyID):
            print("Hello, {}.".format(self.name))
        else:
            print("Incorrect Faculty ID")

#child class
class Student(User):
    grade = 0
    gpa = 0
    studentID = 0

    def login(self):
        name = input("Enter your name: ")
        id = input("Enter your Student ID: ")
        if(id == self.facultyID):
            print("Hello, {}.".format(self.name))
        else:
            print("Incorrect Student ID")
    
