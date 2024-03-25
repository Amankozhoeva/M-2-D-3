""" 
1) 
"""

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def info(self):
#         print(f'Название: {self.title}\n',
#                f'Автор : {self.author}\n',
#                  f'Кол-во страниц: {self.pages}')
        
#     def size(self):
#         if self.pages > 300:
#             print('Книга большая')
#         else:
#             print('Книга маленькая')
        
# book1 = Book('Гракаем алгоритмы', 'Адитья Бхаргава', 290)
# book1.info()
# book1.size()

"""
2)
"""
# class Student:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.grade = None

#     def set_grade(self, grade):
#         self.grade = grade

#     def get_grade(self):
#         if self.grade is None:
#             print('У студента не проставлена оценка!')
#         else:
#             print(f'Оценка студента: {self.grade}')

# student1 = Student(name='Sam')
# student1.get_grade()
# student1.set_grade(83)
# student1.get_grade()
        
"""
3)
"""


# class Teacher:
    
#     def __init__(self, name, subject) -> None:
#         self.name = name
#         self.subject = subject

#     def info(self):
#         print(f'{self.name} предмет преподования {self.subject}')

# class TeacherMath(Teacher):
#     pass

# class TeacherLang(Teacher):
#     def info(self):
#         print('Я сперва унаследовал!!!')
#         print(f' {self.name} предмет преподавания {self.subject}')

# teacher_math = TeacherMath(name ='Фибоначи', subject='Математика')
# teacher_lang = TeacherLang(name = 'Гвидо Ван Рассум', subject='Python')

# teacher_math.info()
# teacher_lang.info()

"""
4)
"""
class Vehicle:
    def __init__(self, mark, model):
        self.mark =mark
        self.model = model

    def start_engine(self):
        print(f' {self.mark}-{self.model} заводись!')
    
car1 = Vehicle(mark='Tayota', model= 'Camry')
car1.start_engine()