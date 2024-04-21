# size_of_triangle = int(input("Enter size of triangle: "))
# symbol_of_triangle = "*"
#
# for i in range(size_of_triangle + 1):
#     print(symbol_of_triangle * i)



size_of_triangle = int(input("Enter size of triangle: "))
symbol_of_triangle = "*"

for i in range(1, size_of_triangle + 1):
    spaces = " " * (size_of_triangle - i)
    stars = symbol_of_triangle * i
    print(spaces + stars)

