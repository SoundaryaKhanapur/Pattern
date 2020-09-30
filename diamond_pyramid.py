n = int(input('Enter N: '))

for i in range(n):
    print(' '*(n-i-1) +  '*' * (2*i+1))

for i in reversed(range(n)):
    print(' '*(n-i-1) +  '*' * (2*i+1))