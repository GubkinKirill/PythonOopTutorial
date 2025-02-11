# Классы и объекты. Атрибуты классов и объектов
 
class Point:
    color = 'red' # Атрибут класса
    circle = 2

a = Point() # Экземпляр класса
b = Point() # Второй экземпляр класса
# a и b разные не зависимые объекты


print(Point.__dict__) # => {'__module__': '__main__', 'color': 'red', 'circle': 2, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, '__doc__': None}
print(a.__dict__) # => {}

a.color = 'green'
print(a.__dict__) # => {'color': 'green'} Появилось локальное свойство color со значением green


setattr(Point, 'prop', 1) # Задали новый атрибут со значание 1. Можно было Point.prop = 1

# Обращение к несуществующему атрибуту вызовет ошибку

print('Обращение к несуществующему атрибуту: ', getattr(Point, 'a', False)) # => False
print('Обращение к существующему атрибуту', getattr(Point, 'color', False)) # => 'red'
