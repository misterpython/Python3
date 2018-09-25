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

lastname - фамилия, name - имя, patronymic - отчество.

class Schoolchild:

    def __init__(self,lastname, name, patronymic):
        self.lastname = lastname
        self.name = name
        self.patronymic = patronymic
        self.lessons = set()
        
    def participate(self, lessons):
        self.lessons.add(lessons)

    def display_information(self):
        print('name:', self.lastname, self.name, self.patronymic)
        print('lessons:', sorted(self.lessons)
        print('parents:', self.mother, self.father)

class Teacher:
    def __init__(self, lastname, name ):
        self.lastname = lastname
        self.name = name
        self.lessons = set()

    def take(self, lesson):
        self.lessons.add(lesson)

    def display_information(self):
        print('name:', self.lastname, self.name)
        print('lessons:', sorted(self.lessons))

class Lesson:
    def __init__(self)          
         self.name = None
         self.hours = 0

    def display_information(self):
         print('Lesson')
         print('name:', self.name)
         print('hours:', self.hours)

class Parents:
    def __init__(self, lastname, name, patronymic, kinder)              
        self.lastname
        self.name
        self.patronymic
        self.kinder      

class Mother(Parents):
    def __init__(self)
        super().__init__(lastname, name, patronymic, kinder) 
              
    def display_information(self):
        print('lastname:', self.lastname)
        print('name:', self.name)      
        print('patronymic:', self.patronymic)
        print('kinder:', self.kinder)      

class Father(Parents):
    def __init__(self)
        super().__init__(lastname, name, patronymic, kinder) 
              
    def display_information(self):
        print('lastname:', self.lastname)
        print('name:', self.name)      
        print('patronymic:', self.patronymic)
        print('kinder:', self.kinder)      

class School_class:
    def __init__(self, name, list_sch_childs, list_teachers, list_sch_class)              
        self.name = name
        self.list_sch_class = list_sch_class      
        self.list_sch_childs = list_sch_childs
        self.list_teachers = list_teachers 
              
    def display_information(self):
        print('list schoolchild:', self.list_sch_childs)
        print('name:', self.name)
        print('list teachers:', self.list_teachers)      
        print('list School class:', self.list_sch_class)









              
