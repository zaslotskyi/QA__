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
            stars_for_first_line = '*' * min_width
            print(spaces + stars_for_first_line)
        else:
            spaces_before = ' ' * ((difference - (i - 1) * 2) // 2)
            spaces_inside = ' ' * (min_width + 2 * (i - 2))
            upper_stars = '*' + spaces_inside + '*'
            print(spaces_before + upper_stars)
    for j in range((difference // 2), 0, -1):
        if j == 1:
            spaces = ' ' * (difference // 2)
            stars_for_last_line = '*' * min_width
            print(spaces + stars_for_last_line)
        else:
            spaces_before = ' ' * ((difference - (j - 1) * 2) // 2)
            spaces_inside = ' ' * (min_width + 2 * (j - 2))
            lower_stars = '*' + spaces_inside + '*'
            print(spaces_before + lower_stars)
