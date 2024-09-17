# product of n natura numbers
n = int(input('enter value: '))

if n<=0:
    print('{} is invalid'.format(n))
else:
    product = 1
    for i in range(1,n+1):
        product *= i
    print('product of first n numbers is {}'.format(product))
