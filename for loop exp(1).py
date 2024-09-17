word = input('enter value: ')

for i in word:
    print(i)
print('-'*50)

# +ve index forword direction
for i in range(0,len(word)):
    print(word[i])
else:
    print('len of word: ',len(word))
    print('-'*50)

# +ve index backword direction
for i in range(len(word)-1,-1,-1):
    print(word[i])
else:
    print('len of word: ', len(word))
    print('-'*50)

# -ve index forword direction
for i in range(-(len(word)),0):
    print(word[i])
else:
    print('len of word: ', len(word))
    print('-' * 50)

# -ve index backword direction
for i in range(-1,-(len(word)+1),-1):
    print(word[i])
else:
    print('len of word: ', len(word))
    print('-' * 50)