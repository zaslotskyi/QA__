import math


def result_cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):

        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = func(*args, **kwargs)
            cache[key] = result
            return result

    return wrapper


@result_cache_decorator
def custom_sqrt(x):
    return math.sqrt(x)


print(custom_sqrt(144))
print(custom_sqrt(144))
