height = int(input("Enter height of rectangle: "))
width = int(input("Enter width of rectangle: "))
symbol_for_rectangle = input("Enter symbol to build rectangle with: ")

for i in range(height):
    for j in range(width):
        print(symbol_for_rectangle, end='')
    print()
