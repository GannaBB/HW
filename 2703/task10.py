# Помолете потребителя да въведе две точки и да открие дали те са на равни
# разстояния от началото на координатната система.
# Вход: (-1, 4) (5,6)
# Изход: Не са на равни разстояния разположени. Втората точка е разположена на поголямо разстояние



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

distance1 = abs((x1 ** 2 + y1 ** 2) ** (1/2))
distance2 = abs((x2 ** 2 + y2 ** 2) ** (1/2))

if distance1 == distance2:
    print('Points are on the same distance from (0,0)')
elif distance1 > distance2:
    print('Points are on different distance from (0,0). Point 2 is closer to zero')
else:
    print('Points are on different distance from (0,0). Point 1 is closer to zero')

# print(distance1,distance2)