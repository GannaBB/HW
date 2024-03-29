# Да се създаде програма, която чете думи като вход от клавиатурата, докато
# потребителят не въведе празен ред. След като потребителят въведе празен ред,
# програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
# Думите трябва да се показват в същия ред, в който са били въведени. Например, ако
# потребителят въведе:
# first
# second
# first
# third
# second
# тогава програмата трябва да принтира само:
# first
# second
# third

x = 1
i = 1
txt = []
while x==True:
    try:
        num = str(input('Your enter: '))
    except:
        print('Invalid input ')
        continue

    if num=='':
        break
    elif num not in txt:
        txt.append(num)
        i += 1
        

print(*txt, sep = '\n')