my_list = [['a', 'c', 'e'],
           ['f', 'b', 'a'],
           ['a', 'n', 'k'],
           ['e', 'l', 'i']]

num_rows = len(my_list)
num_cols = len(my_list[0])

sorted_list = [[] for _ in range(num_rows)]


for j in range(num_cols):
    column = [my_list[i][j] for i in range(num_rows)]
    column.sort()
    for i in range(num_rows):
        sorted_list[i].append(column[i])

print(sorted_list)


