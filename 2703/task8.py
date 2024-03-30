# Използвайте задача 7 и проверете дали триъгълникът е с прав ъгъл.
# Използвайте sin теорема: sin(от даден ъгъл) = срещулежаща страна / хипотенузата.
# Използвайте функция math.asin да превърнете в радиани, и след това math.degrees за да
# превърнете в градуси. Като sin(90) = 1, sin(30) = ½ и т.н. Ако сборът на два от ъглите е
# 90 градуса, то автоматично третият е равен на 90 градуса.
# Вход: (3, -5), (-3, 3), (-1, -2)
# Изход: Нито един от ъглите не 90 градуса.

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


a = (x1-x2) ** 2 + (y1-y2) ** 2
b = (x1-x3) ** 2 + (y1-y3) ** 2
c = (x3-x2) ** 2 + (y3-y2) ** 2



if ((a + b) == c ) or ((a + c) == b) or ((b + c) == a):
    print('Правоъгълен триъгълник')
else: 
    print('Няма прав ъгъл')

    print(a,b,c)




