def linearize_list(lst):
    new_lst = []

    for i in lst:
        if isinstance(i, list):
            new_lst.extend(linearize_list(i))
        else:
            new_lst.append(i)

    return new_lst

lst = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
result = linearize_list(lst)
print(result)




