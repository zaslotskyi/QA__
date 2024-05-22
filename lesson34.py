def custom_zip(*sequences, full=False, default=None):
    new_list = []

    if not full:
        for i in (zip(*sequences)):
            new_list.append(i)
    else:
        max_lst = max(sequences, key=len)
        min_lst = min(sequences, key=len)
        min_lst_copy = min_lst[:]
        my_lst = [default] * (len(max_lst) - len(min_lst_copy))
        min_lst_copy.extend(my_lst)
        for i in zip(max_lst, min_lst_copy):
            new_list.append(i)

    return new_list


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

print(custom_zip(seq1, seq2))  # [(1, 9), (2, 8), (3, 7)]
print(custom_zip(seq1, seq2, full=True, default="Q"))  # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
print(custom_zip(seq1, seq2, full=True))
