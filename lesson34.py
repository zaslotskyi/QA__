def custom_zip(*sequences, full=False, default=None):

    result = []

    if full:
        max_length = max(len(lst) for lst in sequences)
        for i in range(max_length):
            tuple_values = tuple(lst[i] if i < len(lst) else default for lst in sequences)
            result.append(tuple_values)
    else:
        min_length = min(len(lst) for lst in sequences)
        for i in range(min_length):
            tuple_values = tuple(lst[i] for lst in sequences)
            result.append(tuple_values)
    return result


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]


print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True, default="Q"))
print(custom_zip(seq1, seq2, full=True))
