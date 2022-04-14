# Practical AIM             :-  see below instructions for practical 9.
# Student-ID                :-  20CS052
# Student-Name              :-  KISHANKUMAR PATEL
# GitHub repository link    :-  https://github.com/20CS052/CE259_PYTHON.git


'''Consider an example of declaring the examination result.
Design three classes: Student, Exam, and Result. The Student class hasdatamemberssuch
as those representing rollNumber, Name, etc. Create the class Exambyinheriting
Student class. The Exam class adds fields representing the marks scoredinsixsubjects.
Derive Result from the Exam class, and it has its own fields such astotal_marks.Write an
interactive program to model this relationship.'''

class Student:
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name

    def display(self):
        print(f'Student Roll No: {self.rollNo}')
        print(f'Student Name: {self.name}')


class Exam(Student):
    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name)
        self.subject = subject

    def display(self):
        super().display()
        for i in range(len(self.subject)):
            print(f'Subject {i} Marks: {self.subject[i]}')

class Result(Exam):
    total_marks = 0

    def __init__(self, rollNo, name, subject):
        super().__init__(rollNo, name, subject)
        self.total_marks = sum(subject)

    def display(self):
        super().display()
        print(f'Total Marks: {self.total_marks}')


if (__name__ == "__main__"):
    student = Student(1, "Kp")
    student.display()
    print()

    exam = Exam(2, "Kishan", [90, 92, 93])
    exam.display()
    print()

    result = Result(3, "Kpp", [84, 85, 86])
    result.display()
    print()

    result = Result(4, "Kri", [70, 80, 90, 10])
    result.display()
    print()
