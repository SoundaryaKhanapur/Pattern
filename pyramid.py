# Enter N: 5
#     1
#    123
#   12345
#  1234567
# 123456789

n = int(input('Enter N: '))
num = 0
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(end=' ')
    while num != (2*i-1):
        print(num+1,end='')
        num += 1
    num = 0
    print('\r')