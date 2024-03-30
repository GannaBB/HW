# Помолете потребителя да въведе 4 точки и да ги подреди в зависимост от
# разстоянията им от началото на координатната система.
# Вход: (-1, 4), (5,6), (-2, 2), (2, 2)
# Изход: (-1, 4), (-2, 2), (2, 2), (5,6)

points = {}
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




distances = []
distances_dict = {}

for a in points:
    x1 = float(points[a][0])
    y1 = float(points[a][1])
    distance1 = abs((x1 ** 2 + y1 ** 2) ** (1/2))
    distances.append(distance1)
    distances_dict[i] = distance1
    points[a] = (x1,y1)

distances_sorted = sorted(distances)

for a in distances_sorted:
    for b in distances:
        if a == b:
            x = distances.index(b)
            print(points[x], end=',')






