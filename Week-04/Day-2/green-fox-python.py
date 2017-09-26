class Person(object):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = str(age)
        self.gender = gender

    def introduce():
        print("Hi, I'm"self.name", a "self.age" year old gender.")

    def get_goal():
        print("My goal is: Live for the moment!")

class Student(Person):

    def __init__(self, previous_organization, skipped_days):
        self.previous_organization = previous_organization
        self.skipped_days = skipped_days

    def get_goal():
        print("Be a junior software developer.")
        
    def introduce():
        print("Hi, I'm "person.name", a "person.age"year old "student.gender" from "self.previous_organization" who \
        skipped "self.skipped_days" days from the course already.)

    def skip_days(number_of_days):
        self.skipped_days += number_of_days

class Mentor(Person):

    def __init__(self, level):
        self.level = level
    
    def get_goal():
        print("Educate brilliant junior software developers")

    def introduce():
        print("Hi, I'm "mentor.name", a "mentor.age" year old "mentor.gender" level mentor.)

class Sponsor(Person):

    def __init__(self, company, hired_students):
        self.company = company
        self.hired_students = str(hired_students)
    
    def introduce():
        print("Hi, I'm "sponsor.name", a "sponsor.age" year old "sponsor.gender" who represents\
         "self.company" and hired "self.hired_students" students so far.")
    
    def hire():
        self.hired_students += 1
    
    def get_goal():
        print(Hire brilliant junior software developers.")