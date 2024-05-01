import math


def sum_and_product(min_value, max_value, lst):

    new_list = [i for i in lst if i >= min_value and i <= max_value]

    if len(new_list) > 0:
        sum_ = sum(new_list)
        product = math.prod(new_list)
    else:
        sum_ = None
        product = None

    return f"sum_ = {sum_}\nproduct = {product}"


assert sum_and_product(3, 6, [2, 4, 6, 2, 1, 1, 9, 4, 6]) == "sum_ = 20\nproduct = 576", 'Test1'
assert sum_and_product(0, 0, [2, 4, 6, 2, 1, 1, 9, 4, 6]) == "sum_ = None\nproduct = None", 'Test2'
print('Passed')


