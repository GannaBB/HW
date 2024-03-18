# Напишете програма, която пресмята N!/K! за дадени N и K (1<K<N). Без да се
# ползват вградени функции.
# Вход: N = 4, K = 3 Вход: N = 3, K = 4 Вход: N = 0, K = 0
# Изход: 4 Изход: K трябва да е по-малко от N Изход: Невалиден вход

try:
    n = int(input('Enter N: '))

except:
    print('N must be integer')

try:
    k = int(input('Enter K<N: '))

    if k>=n:
        print('K must be less than N')
        exit()
except:
    print('K must be integer')

result = 1

if k==0 or n==0:
    print('Invalid input')
    exit()

for i in range(k+1,n+1):
    result = result*i

print('N!/K!=', result)

