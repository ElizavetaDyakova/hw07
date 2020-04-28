# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, teachers, student, studentpar):
        self._teachers = teachers
        self._students = student
        self._studentpar = studentpar
#получаем все классы в школе
    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    #ученики в классе
    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    #учителя в классе
    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    #Родители, предметы, учителя и полное имя ученика
    def find_student(self, student_full_name):
        for person in self._studentpar:
            if student_full_name == person.get_full_name:
                parents = person.get_parents
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                return {
                    'full_name': student_full_name,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                }

class People:
    def __init__(self, surname, name, lastname):
        self._surname = surname
        self._name = name
        self._lastname = lastname

    #полное имя
    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._surname,
                                    self._name,
                                    self._lastname)

    #сокращенное имя
    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._surname,
                                     self._name[:1],
                                     self._lastname[:1])


class Student(People):
    def __init__(self, surname, name, lastname,
                 class_room, mom, dad):
        People.__init__(self, surname, name, lastname)
        self._class_room = class_room
        self._parents = {
            'mom': mom,
            'dad': dad
            }

    #классы в шк
    @property
    def get_class_room(self):
        return self._class_room

    #родители
    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, surname, name, lastname,
                 courses, classes):
        People.__init__(self, surname, name, lastname)
        self._courses = courses
        self._classes = classes

    #предметы которые ведет учитель
    @property
    def get_courses(self):
        return self._courses

    #классы в которых он преподает
    @property
    def get_classes(self):
        return self._classes

#уителя
teachers = [
    Teacher('Попов', 'Арсений', 'Сергеевич', 'Физика', ['11А', '11Б']),
    Teacher('Иванов', 'Сергей', 'Андреевич', 'Биология', ['11А'])]

#ученики
student = [
    Student('Петров', 'Максим', 'Даниилович', '11А', 'Петрова Е.О.', 'Петров Д.А.'),
    Student('Ястребова', 'Лидия', 'Тимуровна', '11А', 'Ястребова Т.В.', 'Ястребов А.В.'),
    Student('Крутин', 'Дмитрий', 'Евгеньевич', '11Б', 'Крутина А.E.', 'Крутин С.А.'),
    Student('Кириченко', 'Ева', 'Андреевна', '11Б', 'Кириченко В.А.', 'Кириченко А.Т')]
#ученики в р.п.
studentpar = [
    Student('Петрова', 'Максима', 'Данииловича', '11А', 'Петрова Е.О.', 'Петров Д.А.'),
    Student('Ястребовой', 'Лидии', 'Тимуровны', '11А', 'Ястребова Т.В.', 'Ястребов А.В.'),
    Student('Крутина', 'Дмитрия', 'Евгеньевича', '11Б', 'Крутина А.E.', 'Крутин С.А.'),
    Student('Кириченко', 'Евы', 'Андреевны', '11Б', 'Кириченко В.А.', 'Кириченко А.Т')]




school = School(teachers, student, studentpar)
clases = school.get_all_classes()
print('Список классов в школе: ')
print(', '.join(clases))

print('\nСписок 11А класса:')
print('\n'.join(school.get_students('11А')))
print('\nСписок 11Б класса:')
print('\n'.join(school.get_students('11Б')))

print('\nПреподаватели 11А класса:\n''{0}'.format(', '.join(school.get_teachers('11А'))))
print('\nПреподаватели 11Б класса:\n''{0}'.format(', '.join(school.get_teachers('11Б'))))


st1 = school.find_student('Кириченко Евы Андреевны')
print('\nРодители {0}: \n''Мама:{1},\nПапа:{2}\nПредметы: {3}'.format(st1['full_name'], st1['parents']['mom'], st1['parents']['dad'], ', '.join(st1['lessons'])))
st2 = school.find_student('Ястребовой Лидии Тимуровны')
print('\nРодители {0}: \n''Мама:{1},\nПапа:{2}\nПредметы: {3}'.format(st2['full_name'], st2['parents']['mom'], st2['parents']['dad'], ', '.join(st2['lessons'])))
st3 = school.find_student('Крутина Дмитрия Евгеньевича')
print('\nРодители {0}: \n''Мама:{1},\nПапа:{2}\nПредметы: {3}'.format(st3['full_name'], st3['parents']['mom'], st3['parents']['dad'],', '.join(st3['lessons'])))
st4 = school.find_student('Ястребовой Лидии Тимуровны')
print('\nРодители {0}: \n''Мама:{1},\nПапа:{2}\nПредметы: {3}'.format(st4['full_name'], st4['parents']['mom'], st4['parents']['dad'], ', '.join(st4['lessons'])))



