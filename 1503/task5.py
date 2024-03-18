#Да се напише програма, която да намира броят на четните и нечетните числа
#от списък от цели числа.
#Вход:
#numbers = [1,2,3,4,5,6,7,8,9]
#Изход:
#Number of even numbers: 4


try:

    x = int(input('How many numbers will you enter: '))

    print('Enter your numbers: ')

    odd = 0
    even = 0

    for i in range(x):
        y = int(input())

        if y%2:
            odd += 1
        else:
            even += 1


except:
    print('Numbers must be integer')

print('Odd:', odd)
print('Even:', even)
