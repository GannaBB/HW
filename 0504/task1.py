# . Да се напише функция, която да търси в списък. Като параметър да приема
# списък и да принтира ако елементът е в списъка неговата позиция, ако ли не да
# принтира, че не е намерен.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found



def list_find(l,x):
    i = 0
    out = []
    for k in l:
        if k == x:
            out.append(i)
        i += 1

    if out == []:
        print(f"Not found")
    else:
        for j in out:
            print(f"Position {j}")


try:
    list = input('Enter your list separated by space: ').split()
    N = input('Enter element to search: ')
except:
    print('Oops, smth wrong')

list_find(list, N)