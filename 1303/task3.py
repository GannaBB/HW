#Съставете програма, която по въведено трицифренo число проверява дали числото се дели на всяка своя цифра. 
#Във въведеното число да няма цифра 0. Използвайте проверка на логическо условие - оператор if.
#Пример: 121 Изход: 1:2:4 дели се


try:
    x = input('Enter 3-digit number (no 0 is accepted): ')

    x_control = int(x)
    if x_control<100 or x_control>1000:
        print('Number must be 3-digit')
        exit()

    x1 = int(x[0])
    x2 = int(x[1])
    x3 = int(x[2])

    if x1==0 or x2==0 or x3==0:
        print('Number can not contan zero')
        exit()
    
    if x_control%x1 and x_control%x2 and x_control%x3:
        print('Не дели се')
    else:
        print('Дели се')
        
    #print(x_control%x1, x_control%x2, x_control%x3)

except:
    print('Follow instrctions')