def custom_zip(*lists, full=False, default=None):
    if full:
        max_length = max(len(lst) for lst in lists)
        result = []
        for i in range(max_length):
            tuple_values = tuple(lst[i] if i < len(lst) else default for lst in lists)
            result.append(tuple_values)
    else:
        min_length = min(len(lst) for lst in lists)
        result = list(zip(*lists))[:min_length]
    return result



seq1 = [10, 2, 3, 4, 5]
seq2 = [9, 8, 7]

print(custom_zip(seq1, seq2))  # [(1, 9), (2, 8), (3, 7)]
print(custom_zip(seq1, seq2, full=True, default="Q"))  # [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
print(custom_zip(seq1, seq2, full=True))
