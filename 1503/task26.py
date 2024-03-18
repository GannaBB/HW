#Напишете програма, която чете от конзолата положително цяло число N (N <
#20) и отпечатва матрица с числа като на фигурата по-долу:

try:
    n = int(input('Enter N<20:'))

    if n>=20:
        print('N must be less then 20')
        exit()
except:
    print('N must be integer')

for i in range(n):
    for j in range(n):
        print(j+1+i, end=' ')

    print()



    
