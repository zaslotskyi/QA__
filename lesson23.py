def second_largest_number(lst):
    max_value = float('-inf')
    second_max_value = float('-inf')

    if not lst or all(x == lst[0] for x in lst):
        return None

    for i in lst:
        if i > max_value:
            second_max_value = max_value
            max_value = i
        elif (i > second_max_value
              and i != max_value):
            second_max_value = i

    return second_max_value



assert second_largest_number([]) is None, 'Test1'
assert second_largest_number([1, 1]) is None, 'Test2'
assert second_largest_number([1, 2, 3, 4, 5]) == 4, 'Test3'
assert second_largest_number([1, 2, 3, 4, 4, 5]) == 4, 'Test4'
assert second_largest_number([1, 2, 3, 4, 5, 5]) == 4, 'Test5'
assert second_largest_number([-7, -5, -3, 0, -2]) == -2, 'Test6'
print('Passed')
