n = int(input('enter value: '))
if n<0:
    print('{} is invalid'.format(n))
else:
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(f'sum of first n numbers is {sum}')