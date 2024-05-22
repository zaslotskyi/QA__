from typing import Callable


def custom_map(function: Callable, *iterables):

    result = [function(*args) for args in zip(*iterables)]

    return result


print(custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]]))  # [6, 13]
print(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0]))  # [4, 7, 3]
print(custom_map(len, [[], (2, 4), [1, 3, 5, 7]]))  # [0, 2, 4]
print(custom_map(lambda x: x ** 2, [3, 5, 0, 5]))  # [9, 25, 0, 25]
