# Enter N: 5
# *********
#  *******
#   *****
#    ***
#     *
n = int(input('Enter N: '))

for i in reversed(range(n)):
    print(' '*(n-i-1) +  '*' * (2*i+1))