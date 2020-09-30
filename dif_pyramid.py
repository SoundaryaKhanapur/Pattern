
n = int(input('Enter n value: '))

for i in range(1, n+1):
    print(' ')
    print((n-i) * " ",end="")

    for j in range(i, 2*i):
        print(j%10, end="")

    for j in range(2*(i-1), i-1, -1):
        print(j%10, end="")

print()
