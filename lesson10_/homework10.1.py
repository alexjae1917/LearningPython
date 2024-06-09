
def valid(lst: list, n):
    for i in lst[n:]:
        if i % n == 0:
            lst.remove(i)


def prime_generator(end):
    lst = []
    for i in range(2,end+1):
        lst.append(i)
    for j in range(2,int(end**0.5)+1):
        valid(lst,j)
    for i in lst:
        yield i

#prime_generator(29)
from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], list(prime_generator(29))
