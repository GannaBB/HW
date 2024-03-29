# Задача 9. Напишете програма, която създава следните квадратни матрици и ги
# извежда на конзолата във форматиран вид. Размерът на матриците се въвежда от
# конзолата. Пример за (4,4):

try:
    n = int(input('Enter matrix size: '))
except:
    print('Value must be integer')



length = n * n

# option 1
for i in range(n):
    for j in range(n):
        print(i+1+j*n,end=' ' )
    print()

print('-'*(n*2))
# option 2
for i in range(n):
    for j in range(n):
        if  j == 0 or not j%2:
            print(i+1+j*n,end=' ' )
        else:
            print(n-i+j*n,end=' ' )
    print()

    

    

