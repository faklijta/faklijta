class Teacher(object):

    def teach(self):
        Student.learn()
    def answer(self):
        pass


class Student(object):
    
    def learn(self):
        pass
    def question(self):
        Teacher.answer()

student = Student()
teacher1 = Teacher()
student.question(teacher1)
