# Ако имате въведени три точки (x1, y1), (x2, y2), (x3, y3) и те не са колинеарни,
# тогава намерете вида на триъгълника, образуван от тях (равностранен, равнобедрен или
# разностранен). Правилото за определяне дали се образува триъгълник е като му се
# намерят страните и се направят следните проверки c < a + b, b+ c < a, a+ c < b.
# Вход: (3, -5), (-3, 3), (-1, -2)
# Изход: разностранен

# input data
y = 1

while y == 1:
    x = 1
    while x == 1:
        try:
            point1 = list(input('Enter coordinates(x, y) of 1st point, separated by coma: ').split(','))
            if True:
                float(point1[0])
                float(point1[1])
                x = 0
        except:
            print('Your input must be a numbers. try again')

    x = 1
    while x == 1:
        try:
            point2 = list(input('Enter coordinates(x, y) of 2nd point, separated by coma: ').split(','))
            if True:
                float(point2[0])
                float(point2[1])
                x = 0
        except:
            print('Your input must be a numbers. try again')

    x = 1
    while x == 1:
        try:
            point3 = list(input('Enter coordinates(x, y) of 3d point, separated by coma: ').split(','))
            if True:
                float(point3[0])
                float(point3[1])
                x = 0
        except:
            print('Your input must be a numbers. try again')

    if (point1[0] == point2[0] and point2[0] == point3[0]) or (point1[1] == point2[1] and point2[1] == point3[1]):
        print('Your points should not be collinear. Try again')
        
    else:
        y = 5


x1 = float(point1[0])
y1 = float(point1[1])

x2 = float(point2[0])
y2 = float(point2[1])

x3 = float(point3[0])
y3 = float(point3[1])


a = abs(((x1-x2) ** 2 + (y1-y2) ** 2) ** (1/2))
b = abs(((x1-x3) ** 2 + (y1-y3) ** 2) ** (1/2))
c = abs(((x3-x2) ** 2 + (y3-y2) ** 2) ** (1/2))

print(a, b, c)
if a != b and b != c and c!=a:
    print('Разностранен')
elif a == b and b == c:
    print('Равностранен')
else:
    print('Равнобедрен'
          )
