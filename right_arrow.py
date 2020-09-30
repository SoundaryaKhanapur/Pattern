# Enter N value:5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n = int(input('Enter N value:'))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,'',end='')
    print('\r')

for i in reversed(range(n)):
    for j in range(1,i+1):
        print(j, '', end='')
    print('\r')
