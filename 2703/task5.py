# Задача 5. Помолете потребителя да въведе координатите на дадена точка и да намери
# разстоянието на точката до началото (0, 0). За абсолютна стойност може да използвате
# вградената функция abs(). Формулата за намиране на разстояние
# !(�! − �")" + (�! − �")"
# Вход: (3, 4) Вход: (-3,




x = 1
while x == 1:
    try:
        coordinates = list(input('Enter coordinates(x, y), separated by coma: ').split(','))
        if True:
            float(coordinates[0])
            float(coordinates[1])
            x = 0
            
    except:
        print('Your input must be a numbers. try again')

x = float(coordinates[0])
y = float(coordinates[1])
distance = abs((x ** 2 + y ** 2) ** (1/2))

print(f"Distance to your point is {distance}")
