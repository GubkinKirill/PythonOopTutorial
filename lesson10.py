# Свойство property. Декоратор @property

class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
        self.__work = 'Programmer'  # Инициализация атрибута work

    @property
    def old(self):
        """Геттер для атрибута old"""
        return self.__old

    @old.setter
    def old(self, old):
        """Сеттер для атрибута old"""
        self.__old = old

    @old.deleter
    def old(self):
        """Делитер для атрибута old"""
        del self.__old

    @property
    def work(self):
        """Геттер для атрибута work"""
        return self.__work

    @work.setter
    def work(self, work):
        """Сеттер для атрибута work"""
        self.__work = work

    @work.deleter
    def work(self):
        """Делитер для атрибута work"""
        del self.__work

# Создание экземпляра класса Person
p = Person('Tom', 30)

# Использование геттера для получения значения old
print(p.old)  # 30

# Использование сеттера для изменения значения old
p.old = 40
print(p.old)  # 40

# Вывод всех атрибутов экземпляра
print(p.__dict__)  # {'_Person__name': 'Tom', '_Person__old': 40, '_Person__work': 'Programmer'}