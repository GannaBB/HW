# Помолете потребителя да въведе две точки (x и y координати) и да намери
# разстоянието между тях.
# Вход: (3, 4), (6,5) Вход: (-3, -4), (4,5)
# Изход: 3.1622776601683795 Изход: 11.40175425099138


x = 1
while x == 1:
    try:
        coordinates1 = list(input('Enter coordinates(x, y) of 1st point, separated by coma: ').split(','))
        if True:
            float(coordinates1[0])
            float(coordinates1[1])
            x = 0
            
    except:
        print('Your input must be a numbers. try again')


x = 1
while x == 1:
    try:
        coordinates2 = list(input('Enter coordinates(x, y) of 2nd point, separated by coma: ').split(','))
        if True:
            float(coordinates2[0])
            float(coordinates2[1])
            x = 0
            
    except:
        print('Your input must be a numbers. try again')

    
x1 = float(coordinates1[0])
y1 = float(coordinates1[1])
    
x2 = float(coordinates2[0])
y2 = float(coordinates2[1])

distance = abs(((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2))

print(f"Distance between your points is {distance}")