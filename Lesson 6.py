class Student:
    def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
      self.courses_attached = {}
    def grade_lecturer(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
        if course in lecturer.grades:
          lecturer.grades[course] += [grade]
        else:
          lecturer.grades[course] = [grade]
      else:
        print('Error')

class Mentor:
    def __init__(self, name, surname):
      self.name = name
      self.surname = surname

class Lecturer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.courses_attached = []
      self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
      super().__init__(name, surname)
      self.courses_attached = []
    def rate_homework(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]
      else:
        print('Error')
# first_exercise
best_student = Student('Ruoy', 'Eman', 'boy')
best_student.courses_in_progress += ['Python']
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_homework(best_student, 'Python', 9.9)
cool_reviewer.rate_homework(best_student, 'Git', 9.9)
print(best_student.grades)
# second_exercise
second_student = Student('Bob', 'Grenn', 'girl')
second_student.courses_in_progress += ['Geology']
# third_exercise
cool_lecturer = Lecturer('Sam', 'Smith')
cool_lecturer.courses_attached += ['Geology']
second_student.grade_lecturer(cool_lecturer, 'Geology', 9)
print(f"Name: {cool_lecturer.name}")
print(f"Surname: {cool_lecturer.surname}")
print(f"Courses in progress: {cool_lecturer.courses_attached}")
print(f"Grades: {cool_lecturer.grades}")