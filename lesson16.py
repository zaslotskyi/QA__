def average_between_elements(lst):

    new_list = []

    for i in lst:
        new_list.append(i)
        if i != lst[-1]:
            new_list.append((i + lst[lst.index(i) + 1]) / 2)

    return new_list



assert average_between_elements([1, 2, 3, 4, 5]) == [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], 'Test1'
assert average_between_elements([0, 1, 2, 3, 4, 5, 6, 7]) == [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7], 'Test2'
assert average_between_elements([5.3, 7.2, 3, 6.4, 2, 9]) == [5.3, 6.25, 7.2, 5.1, 3, 4.7, 6.4, 4.2, 2, 5.5, 9], 'Test3'
assert average_between_elements([]) == [], 'Test4'
print('Passed')
