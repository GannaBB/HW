# Използвайте задача 11 и подредете точки по реда на техните x координати в
# низходящ ред.
# Вход: (-1, 4), (5, 6), (-2,2), (2,2)
# Изход: (5, 6), (2, 2) (-2, 2), (-1, 4)

points = {}
x_list = []
for i in range(4): 
    x = 1
    while x == 1:
        try:
            coordinates1 = list(input('Enter coordinates(x, y) of the point, separated by coma: ').split(','))
            if True:
                float(coordinates1[0])
                float(coordinates1[1])
                x = 0
            
        except:
            print('Your input must be a numbers. try again')

    points[i] = coordinates1
    x_list.append(float(coordinates1[0]))


x_sorted = sorted(x_list, reverse=True)

for a in points:
    x1 = float(points[a][0])
    y1 = float(points[a][1])
    points[a] = (x1,y1)


for a in x_sorted:
    for b in x_list:
        if a == b:
            x = x_list.index(b)
            print(points[x], end=',')

