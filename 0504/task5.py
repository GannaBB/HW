# Да се създаде програма, която да реализира няколко функции: добавяне (Add),
# изтриване (Remove), изтриване на всичко (clear), показване (show), край на програмата
# (Quit). Програмата да реализира програмна логика за количка за пазаруване (като тези
# в онлайн магазините). Потребителят да въвежда от клавиатурата даден елемент, след
# което да има възможност да го добави, изтрие, да види какво е поръчал.


def add(res):
    x = input("Enter item to add: ")
    res = list
    res.append(x)
    return(res)

def remove(res):
    x = input("Enter item to remove: ")
    res.remove(x)
    return(res)

def clear(res):
    res = []

def show(res):
    if res == []:
        print('Your basket if empty')
    else:
        print(f"Your current basket: ")
        for i in res:
            print(i)

# start

list = []

k = 1
while k == 1:
    try:
        y = int(input(f'What would you like to do? \n  #1 Add item \n  #2 Remove item \n  #3 Clear your list \n  #4 Show your basket \n  #5 Quit \nChoose your option by entering a number: '))
    except:
        print('Must be an integer')
    if y == 1:
        add(list)
    elif y == 2:
        remove(list)
    elif y == 3:
        clear(list)
    elif y == 4:
        show(list)
    elif y == 5:
        exit()
    else: 
        print('Number should be between 1 and 5')

