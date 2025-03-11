# Магический метод __call__. Функторы и классы-декораторы

# Функторы
# Функтор - это объект, который можно вызывать как функцию.
# Для этого в классе должен быть определен метод __call__.  Этот метод вызывается при вызове объекта как функции.
# Функторы используются для создания объектов, которые могут хранить состояние и реализовывать какую-то логику.
import math
class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('Вызван метод __call__')
        self.__counter += 1
        return self.__counter

c = Counter()
print(c())
print(c())
print(c())
print(c())


class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError('Аргумент должен быть строкой')
        return args[0].strip(self.__chars)

s1 = StripChars('!@#$%^&*()_+')
s2 = StripChars('1234567890')
print(s1('!@#$%^&*()_+hello!@#$%^&*()_+'))
print(s2('1234567890hello1234567890'))


class Derivate:
    def __init__(self, func):
        self.__fn = func
    def __call__(self, x=0, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate   
def df_sin(x):
    return math.sin(x)

print(df_sin(math.pi / 3))

#df_sin = Derivate(df_sin)
