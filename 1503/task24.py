# Напишете програма, която пресмята N!*K!/(N-K)! за дадени N и K (1<K<N).
# Без да се ползват вградени функции.
# Вход: N = 4, K = 3 Вход: N = 3, K = 4 Вход: N = 0, K = 0
# Изход: 144 Изход: K трябва да е по-малко от N Изход: Невалиден вход


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

if k==0 or n==0:
    print('Invalid input')
    exit()

n_factorial = 1
k_factorial = 1
diff_factorial = 1

for i in range(n):
    n_factorial = n_factorial*(i+1)

for i in range(k):
    k_factorial = k_factorial*(i+1)

for i in range(n-k):
    diff_factorial = diff_factorial*(i+1)

result = n_factorial * k_factorial / diff_factorial

print('N!/K!=', result)
