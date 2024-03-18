#Да се състави програма, която ще изчисли сумата на 5, въведени от
#клавиатурата, естествени числа от интервала [10 ..5555].
#Вход: 1,2,3,4,5
#Изход: 15

try:

    z = 0
    for x in range(5):
        y = int(input('Enter integer number in range [10:5555]: '))
    
        if y<10 or y>5555:
            print('Number must be in the range [10:5555]')
            exit()

        z += y

        
except():
    print('Follow instructions')

print('Sum:', z)

    


    

    
             