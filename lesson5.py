a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))

list_of_nums = [a, b, c]
max_value = list_of_nums[0]
for num in list_of_nums[1:]:
    if num> max_value:
        max_value = num
print(f"Max value is {max_value}")