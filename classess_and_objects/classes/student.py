class Student:

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return True

    def average_grade(self):
        if len(self.grades) == 0:
            return False
        else:
            return sum(self.grades) / len(self.grades)
