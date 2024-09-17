# product of even numbers with in given range
n = int(input('enter value: '))
m = int(input('enter value: '))
product = 1
if n%2 != 0:
    print(f'{n} is invalisd')
else:
    for i in range(n,m,2):
        print(i,end=' ')
        product *= i
    print('--->{} is product values in range {},{}'.format(product,n,m))

