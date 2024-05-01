my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


divisible_by_3 = []
divisible_by_5 = []
divisible_by_3_and_5 = []


for i in my_list:
    if i % 3 == 0 and i % 5 != 0:
        divisible_by_3.append(i)
    elif i % 5 == 0 and i % 3 != 0:
        divisible_by_5.append(i)
    elif i % 3 == 0 and i % 5 == 0:
        divisible_by_3_and_5.append(i)


# divisible_by_3 = [i for i in my_list if i % 3 == 0 and i % 5 != 0]
# divisible_by_5 = [i for i in my_list if i % 5 == 0 and i % 3 != 0]
# divisible_by_3_and_5 = [i for i in my_list if i % 3 == 0 and i % 5 == 0]




assert divisible_by_3 == [3, 6, 9, 12], 'Test1'
assert divisible_by_5 == [5, 10], 'Test2'
assert divisible_by_3_and_5 == [0, 15], 'Test3'
print("Passed")


