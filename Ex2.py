class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        # Как лучше? Два раза проверить вхождение или один раз вхождение в пересечение множеств?
        # if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
        if isinstance(lecturer, Lecturer) and course in (set(lecturer.courses_attached) & set(self.courses_in_progress)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


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

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')

cool_reviewer = Reviewer('Reviewer', 'One')

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer.rate_hw(best_student, 'Python', 30)

cool_lecturer = Lecturer('Lecturer', 'One')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)

print(best_student.name, best_student.surname, best_student.grades)
print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.grades)
