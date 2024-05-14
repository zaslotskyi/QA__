def list_item_generator(lst, iter_num=None):
    if iter_num is None:
        index = 0
        length = len(lst)
        while True:
            yield lst[index]
            index = (index + 1) % length
    else:
        index = 0
        length = len(lst)
        while iter_num > 0:
            yield lst[index]
            index = (index + 1) % length
            if index == 0:
                iter_num -= 1

lst1 = ['a', 'b', 'c']
for i in list_item_generator(lst1, iter_num=2):
    print(i)

