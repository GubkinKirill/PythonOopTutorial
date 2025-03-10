# Свойство property. Декоратор @property

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        self.__work = 'Programmer'
    @property    
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    @property
    def work(self):
        return self.__work
    @work.setter
    def work(self, work):
        self.__work = work
    @work.deleter
    def work(self):
        del self.__work

p = Person('Tom', 30)
print(p.old) # 30
p.old = 40
print(p.old) # 40
print(p.__dict__) # {'_Person__name': 'Tom', '_Person__old': 40}


