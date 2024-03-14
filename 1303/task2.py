#Да се състави програма, чрез която се въвеждат 2 естествени двуцифрени числа a,b. Програмата да изведе съобщение дали последната цифра от произведението 
#на двете числа е четна, както и самата цифра. 
#Входни данни: a,b - естествени числа от интервала [10..99].
#Използвайте проверка на логическо условие - оператор if.
#Пример: 15, 25 Изход: 375, 5 нечетна


try:
    x = int(input('Enter 1st 2-digit real number: '))

    if x<10 or x>99:
        print('Numbers should mst contain 2 digits')
        exit()

    y = int(input('Enter 2nd 2-digit real number: '))

    if y<10 or y>99:
        print('Numbers should mst contain 2 digits')
        exit()
    
    product=x*y
    last_digit=product%10


    
    if last_digit==0:
        print(product, last_digit)
    else:
        if product%2:
            print(product, last_digit, 'нечетна')
        else:
            print(product, last_digit, 'четна')

except:
    print('Follow instructions and enter 2-digit numbers')


