import math


def sum_and_product(min, max, lst):

    new_list = [i for i in lst if i >= min and i <= max]

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


