from inspect import isgenerator
from typing import Callable


def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func: Callable):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    d = begin
    for i in range(end):
        yield d
        d = func(d)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], f'{list(gen)}'
