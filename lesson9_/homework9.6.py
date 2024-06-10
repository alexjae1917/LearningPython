from typing import Callable


def my_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        name = func.__name__
        result = func(*args, **kwargs)
        print(f'Function name {name}, with position arguments {args}, named arguments {kwargs}, and result {result}')
        return result

    return wrapper


@my_decorator
def test_func(n: int, cnt=5):
    while cnt < n:
        cnt *= cnt

    return cnt

print(test_func(100, cnt=10))
