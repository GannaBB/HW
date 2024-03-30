# В задача номер 7 намерете ъглите на триъгълника.
# Вход: (3, -5), (-3, 3), (-1, -2)
# Изход: 33 градуса, 30 градуса, 114 градуса

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


a = abs(((x1-x2) ** 2 + (y1-y2) ** 2) **(1/2))
b = abs(((x1-x3) ** 2 + (y1-y3) ** 2) **(1/2))
c = abs(((x3-x2) ** 2 + (y3-y2) ** 2) ** (1/2))

import math

cosA = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
cosB = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
cosC = (b ** 2 + a ** 2 - c ** 2) / (2 * b * a)

A = math.acos(cosA)
B = math.acos(cosB)
C = math.acos(cosC)

degreeA = round(math.degrees(A))
degreeB = round(math.degrees(B))
degreeC = round(math.degrees(C))

print(f"Angles of your triangle are: {degreeA}\N{DEGREE SIGN}, {degreeB}\N{DEGREE SIGN}, {degreeC}\N{DEGREE SIGN}")