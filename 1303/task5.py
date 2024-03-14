#Преди доста години имаше услуга - изпращане на луксозна телеграма.
#Поводи най-различни: рожден, имен ден, сватба и т.н. Цената се формираше по следния начин:
#цена за бланка (А) + цена за текст до 20 думи (B) + цена за всяка дума, след първите 20 думи (C)
#Стойностите на A, B, C са реални числа от интервала [0.02..0.89]. 
#Да се състави програма, чрез която по въведени брой думи, стойности за A, B и C се изчислява крайна цена на луксозна телеграма.
#Пример: A=0.2, B=0.5, 45 думи, C=0.05 Изход: 1.95



try:

    a = float(input('Enter price for a form (0.20-0.89Lv): '))

    if a<0.2 or a>0.89:
        print('Enter valid price')
        exit()

    
    b = float(input('Enter price for a 1st 20 words (0.20-0.89Lv): '))

    if b<0.2 or b>0.89:
        print('Enter valid price')
        exit()


    c = float(input('Enter price for a word >20 (0.20-0.89Lv): '))

    if c<0.2 or c>0.89:
        print('Enter valid price')
        exit()


    text = input('Enter text of your telegramm: ')

    space = len(text.split())-1
    coma = len(text.split(','))-1
    coma_space= len(text.split(', '))-1
    space_coma= len(text.split(' ,'))-1

    if coma==0:
        word_number = space+1
    elif coma_space==0 and space_coma==0:
        word_number = space+coma+1
    elif coma_space==0:
        word_number = space+coma-space_coma+1
    elif space_coma==0:
        word_number = space+coma-coma_space+1
    else:
        word_number = space+coma-coma_space-space_coma+1

    if word_number<=40:
        price = a+b
    else:
        price = a + b +(word_number-40)*c

    print('Total price: ', price, 'Lv')


except:
    print('Enter valid data')