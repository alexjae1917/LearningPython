def refactor(number):
    for i in range(len(number)):
        number[i] = int(number[i])
    return number


def add_one(some_list: list) -> list:
    n = ''
    for i in some_list: n += str(i)
    n = int(n) + 1
    some_list = refactor(list(str(n)))
    return some_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'