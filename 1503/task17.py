# Да се напише програма, която да приема от клавиатурата цяло число n и като
# резултат да принтира всички числа до въведеното.
# Вход: n = 4 Вход: n = 11
# Изход: 1-2-3-4 Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1
# Вход: n = 15
# Изход: 1-2-3-4-5-6-7-8-9-1-0-1-1-1-2-1-3-1-4-1-5


try:
    x = int(input('Enter a number: '))
except:
    print('It must be an integer')

for n in range(1,x+1):
    
    n_str=str(n)
    for l in n_str:
        print(l, end='-')
