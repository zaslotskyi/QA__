n = int(input("Enter n: "))

for i in range(n):
    num = 1
    for j in range(n - i - 1):
        print(' ', end=' ')
    for j in range(i):
        print(num, end=' ')
        num += 1
    for j in range(i+1):
        print(num, end='')
        num-=1
        if j != i:
            print('', end=' ')
    print()
