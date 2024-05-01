my_list = [['a', 'c', 'e'],
           ['f', 'b', 'a'],
           ['a', 'n', 'k'],
           ['e', 'l', 'i']]



new_list = [sorted([i[0] for i in my_list]),
              sorted([i[1] for i in my_list]),
              sorted([i[2] for i in my_list])]


sorted_list = [[i[0] for i in new_list],
               [i[1] for i in new_list],
               [i[2] for i in new_list],
               [i[3] for i in new_list]]


print(sorted_list)







