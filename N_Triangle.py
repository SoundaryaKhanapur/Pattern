# Enter N value: 5
# 1
# 12
# 123
# 1234
# 12345

n = int(input('Enter N value: '))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end='')
    print("\r") # ending line after each row
