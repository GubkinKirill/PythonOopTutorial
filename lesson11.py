#Пример испоьзования объектов property
#Пример разработки класса Person
#{ФИО, Возраст (целое число от 14 до 120), серия и номер паспорта в формате хххх хххххх, вес в кг)
from string import ascii_letters

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise ValueError('ФИО должно быть строкой')
        
        f = fio.split()
        if len(f) != 3:
            raise ValueError('ФИО должно состоять из трех слов')
        
        lettess = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 1:
                raise ValueError('Каждое слово ФИО должно содержать хотя бы одну букву')
            if len(s.strip(lettess)) > 0:
                raise ValueError('ФИО должно содержать только буквы')
    
    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise ValueError('Возраст должен быть целым числом от 14 до 120')

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise ValueError('Вес должен быть числом больше 20')
    
    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise ValueError('Серия и номер паспорта должны быть строкой')
        
        s = ps.split()

        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise ValueError('Серия и номер паспорта должны быть в формате xxxx xxxxxx')
        
        for p in s:
            if not p.isdigit():
                raise ValueError('Серия и номер паспорта должны содержать только цифры')

    @property
    def fio(self):
        return self.__fio
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

p = Person('Иванов Иван Иванович', 30, '1234 123456', 80.5)
print(p.fio)
print(p.old)
print(p.ps)
print(p.weight)
