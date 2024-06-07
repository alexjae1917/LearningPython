import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time() - start
        return end
    return wrapper


@ my_decorator
def test_func(n: int):
    cnt = 1
    while cnt < n:
        cnt += 1


print(test_func(100000000))
