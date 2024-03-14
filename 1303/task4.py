#Да се състави програма, която да изчислява периметър и площ на
#правоъгълник по въведени дължини на прилежащи страни - естествени числа от интервала [5 ..100].
# Изведете съобщение, ако страните формират квадрат. Използвайте проверка на логическо условие - оператор if.
#Пример: 4,4 Изход: квадрат лице 16, периметър 16


try:
    a = int(input('Enter rectangular length: '))
    b = int(input('Enter rectangular hight: '))

    if a>100 or b>100:
        print('Length should be less than 100')
        exit()
    
    area = a*b
    perimeter = 2*(a+b)

    if a==b:
        print('This is a square with area of', area, 'and perimeter of ', perimeter)
    else:
        print('Rectangular with area of', area, 'and perimeter of ', perimeter)

except:
    print('Only integer value less than 100 is allowed')