def custom_map(function, *iterables):

    result = []

    if not function.__module__ == 'builtins':
        if len(iterables) == 1:
            iterables = iterables[0]
            for args in zip(*iterables):
                result.append(function(*args))
        else:
            for args in zip(*iterables):
                result.append(function(*args))
    else:
        if len(iterables) == 1:
            for item in iterables:
                for element in item:
                    result.append(function(element))
        else:
            for i in iterables:
                result.append(function(i))

    return result


print(custom_map(lambda x, y: x + y, [[1, 2, 3], [3, 5, 0]]))  # [4, 7, 3]
print(custom_map(lambda x, y: x + y, [1, 2, 3], [3, 5, 0]))  # [4, 7, 3])
print(custom_map(sum, [[1, 2, 3], [3, 5, 0, 5]]))  # [6, 13]
print(custom_map(sum, [1, 2, 3], [3, 5, 0, 5]))  # [6, 13]
print(custom_map(len, [[], [2, 4], [1, 3, 5, 7]]))  # [0, 2, 4]
print(custom_map(len, [], [2, 4], [1, 3, 5, 7]))  # [0, 2, 4]
print(custom_map(lambda x, y: x + y, [1, 2], [3, 5, 0]))  # [4, 7]
