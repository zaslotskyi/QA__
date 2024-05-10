def lst2dict(lst):

    keys = []
    values = []

    for index, value in enumerate(lst):
        if index % 2 == 0:
            keys.append(value)
        else:
            values.append(value)

    my_dict = dict(zip(keys, values))

    return my_dict


lst = [0, 1, 2, 3]
lst2 = ['a', 'A', 'b', 'B', 'c']


assert lst2dict(lst) == {0: 1, 2: 3}, 'Test1'
assert lst2dict(lst2) == {'a': 'A', 'b': 'B'}, 'Test2'
print('Passed')


