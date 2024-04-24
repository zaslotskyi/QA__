min_width = int(input("Enter minimal width: "))
max_width = int(input("Enter maximal width: "))
difference = max_width - min_width

if min_width > max_width:
    print("Minimal width can't be greater than maximal")
elif (max_width - min_width) % 2 != 0:
    print("The difference between maximal and minimal width is not a multiple of 2")
else:
    for i in range(1, (difference // 2) + 2):
        if i == 1:
            spaces = ' ' * (difference // 2)
            stars = '*' * min_width
            print(spaces + stars)
        else:
            spaces_before = ' ' * ((difference - (i - 1) * 2) // 2)
            spaces_inside = ' ' * (min_width * (i - 1))
            stars = '*' + spaces_inside + '*'
            print(spaces_before + stars)
    for j in range((difference // 2), 0, -1):
        if j == 1:
            spaces = ' ' * (difference // 2)
            stars = '*' * min_width
            print(spaces + stars)
        else:
            spaces_before = ' ' * ((difference - (j - 1) * 2) // 2)
            spaces_inside = ' ' * (min_width * (j - 1))
            stars = '*' + spaces_inside + '*'
            print(spaces_before + stars)
