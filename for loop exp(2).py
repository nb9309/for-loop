n = int(input('enter value: '))

if n < 0:
    print('{} is invalid'.format(n))
else:
    for i in range(1,11):
        print('{} x {} = {}'.format(i,n,i*n))