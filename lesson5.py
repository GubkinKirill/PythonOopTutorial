# Магический метод __new__. Пример паттерна Singleton
# __new()__ - вызывается перед созданием объекта класса 

class Point:
    def __new__(cls, *args, **kwargs): # аргументы обязаетельны
        print('Вызов  __new__ для ' + str(cls))
        return super().__new__(cls)
# cls ссылается на класс
# self ссылается на экземпляр класса
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print('вызов __init__ для ', str(self))

pt = Point(1, 2)

# При запуске программы выводится: Вызов  __new__ для <class '__main__.Point'>

print(pt)


# Паттерн Singleton
# Singleton - порождающий паттерн проектирования, гарантирующий, что в однопроцессном приложении будет только один экземпляр класса с глобальной точкой доступа.

class Database:
    __instance = None # приватная переменная класса используется для хранения единственного экземпляра класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance # возвращает единственный экземпляр класса
    
    def __del__(self):
        Database.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print('Подключение к базе данных: ', self.user, self.password, self.port)
    
    def close(self):
        print('Отключение от базы данных')

    def read(self):
        print('Чтение данных')
    
    def write(self, data):
        print('Запись данных в базу ', data)



db = Database('user', 'password', 3306)
db1 = Database('user1', 'password1', 3307)

print(id(db), id(db1)) # id одинаковый для обоих экземпляров класса, db и db1 - один и тот же объект
db.connect()
db1.connect()