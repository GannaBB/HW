#Задача 20. Да се напише програма, която да намира най-близкото число палиндром дo
#въведено цяло число от клавиатурата.
#Вход: 887 Вход: 100 Вход: 888 Вход: 27
#Изход: 888 Изход: 99 Изход: 888 Изход: 22


try:
    x = int(input('Enter your number: '))
except:
    print('It should be integer')


#check if number istself if palindrom

str_x = str(x)
str_x_reverse = ''
for l in str_x:
    str_x_reverse = l + str_x_reverse

if str_x==str_x_reverse:
    print("Number itself is palindrom")
    exit()


#evaluation of the closest numbers
control = 1
x_plus = x + 1
x_minus = x - 1

while control==1:
    
    str_plus = str(x_plus)
    str_minus = str(x_minus)

    str_plus_reverse = ''
    str_minus_reverse = ''

    for l in str_plus:
        str_plus_reverse = l + str_plus_reverse

    for l in str_minus:
        str_minus_reverse = l + str_minus_reverse

    if str_plus==str_plus_reverse:
        print('The nearest palindrom: ', str_plus)
        control = 2

    elif str_minus==str_minus_reverse:
        print('The nearest palindrom: ', str_minus)
        control = 2

    else:
        x_plus = x_plus + 1
        x_minus = x_minus - 1



    


    



    