


def add_one(some_list: list) -> list:
    n = ''
    for i in some_list:
        n += str(i)
    n = int(n) + 1
    res = list(map(int, str(n)))

    return res


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'