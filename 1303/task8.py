#Да се състави програма, която да провери дали е възможно един
#правоъгълник да се вмести изцяло в друг правоъгълник.
#Входни данни: X1, Y1, X2, Y2 - страните на 2-та правоъгълника - естествени числа от интервала [5-100].
#Пример: 5, 12; 18,7 Изход: вместват се


try:

    x1 = float(input('Enter length of 1st rectangle: '))

    if x1<5 or x1>100:
        print('Value should be in the range [5:100]')
        exit()

    y1 = float(input('Enter width of 1st rectangle: '))

    if y1<5 or y1>100:
        print('Value should be in the range [5:100]')
        exit()

    x2 = float(input('Enter length of 2nd rectangle: '))

    if x2<5 or x2>100:
        print('Value should be in the range [5:100]')
        exit()

    y2 = float(input('Enter width of 2nd rectangle: '))

    if y2<5 or y2>100:
        print('Value should be in the range [5:100]')
        exit()

    if x1>x2 and y1>y2:
        print('Fit')
    elif x1<x2 and y1<y2:
        print('Fit')
    elif x1>y2 and y1>x2:
        print('Fit')
    elif x1<y2 and y1<x2:
        print('Fit')
    else:
        print('Does not fit')

except:
    print('Enter valid data')
        

    
    