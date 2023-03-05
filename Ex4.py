class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {self.grades_avg()}\n' \
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                 f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Эти объекты нельзя сравнивать"
        return self.grades_avg() < other.grades_avg()

    def __le__(self, other):
        if not isinstance(other, Student):
            return "Эти объекты нельзя сравнивать"
        return self.grades_avg() <= other.grades_avg()


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (set(lecturer.courses_attached) & set(self.courses_in_progress)):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grades_avg(self):
        result = []
        for grades in self.grades.values():
            result.extend(grades)
        return sum(result) / len(result)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.grades_avg()}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Эти объекты нельзя сравнивать"
        return self.grades_avg() < other.grades_avg()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return "Эти объекты нельзя сравнивать"
        return self.grades_avg() <= other.grades_avg()

    def grades_avg(self):
        result = []
        for grades in self.grades.values():
            result.extend(grades)
        return sum(result) / len(result)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса)
def avg_grade_students_by_course(students, course):
    result = []
    for student in students:
        # Если элемент списка не является объектом класса Student или course не содержится в списке
        # student.grades, то пропускаю этот элемент
        if isinstance(student, Student) and course in student.grades:
            result.extend(student.grades[course])
    if result:
        return sum(result) / len(result)
    else:
        return 'По заданным условиям отсутствуют оценки у студентов'


# подсчет средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).
def avg_grade_lecturers_by_course(lecturers, course):
    result = []
    for lecturer in lecturers:
        # Если элемент списка не является объектом класса Lecturer или course не содержится в списке
        # lecturer.grades, то пропускаю этот элемент
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            result.extend(lecturer.grades[course])
    if result:
        return sum(result) / len(result)
    else:
        return 'По заданным условиям отсутствуют оценки у лекторов'



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Vasya', 'Pupkin', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')

cool_reviewer = Reviewer('Reviewer', 'One')

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 20)
cool_reviewer.rate_hw(best_student, 'Git', 30)

cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Git', 40)
cool_reviewer.rate_hw(best_student2, 'Python', 50)

cool_lecturer = Lecturer('Lecturer', 'One')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

cool_lecturer2 = Lecturer('Lecturer2', 'Two')
cool_lecturer2.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Git']

best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Python', 8)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'Git', 5)

best_student2.rate_lecture(cool_lecturer2, 'Python', 20)
best_student2.rate_lecture(cool_lecturer2, 'Git', 8)
best_student2.rate_lecture(cool_lecturer2, 'Python', 9)
best_student2.rate_lecture(cool_lecturer2, 'Git', 35)

print(best_student.name, best_student.surname, best_student.grades)
print('---')
print(best_student2.name, best_student2.surname, best_student2.grades)
print('---')
print(cool_lecturer.name, cool_lecturer.surname, cool_lecturer.grades)
print('---')
print(cool_lecturer2.name, cool_lecturer2.surname, cool_lecturer2.grades)
print('---')
print(cool_reviewer)
print('---')
print(cool_lecturer)
print('---')
print(cool_lecturer2)
print('---')
print(best_student)
print('---')
print(best_student2)
print()


print(best_student < best_student2)
print('---')
print(cool_lecturer > cool_lecturer2)
print('---')
print(best_student >= best_student2)
print('---')
print(cool_lecturer <= cool_lecturer2)
print()


print(avg_grade_students_by_course([best_student, best_student2], 'Python'))
print('---')
print(avg_grade_students_by_course([best_student], 'Python'))
print('---')
print(avg_grade_students_by_course([best_student2], 'Git'))
print()
print(avg_grade_lecturers_by_course([cool_lecturer, cool_lecturer2], 'Python'))
print('---')
print(avg_grade_lecturers_by_course([cool_lecturer, cool_lecturer2], 'Git'))
print('---')
print(avg_grade_lecturers_by_course([cool_lecturer], 'Python'))
