# Да се промени горната задача така, че тя да връща стойност и след това да се
# принтира резултатът в зависимост от върната стойност от функцията. Да се напише и
# още една функция, която да принтира резултатът от търсенето.
# Вход: [1, 2, 5, 9, 10], 5 Вход: [1, 2, 5, 9, 10], 3
# Изход: Position 2 Изход: Not found



def list_find(l,x):
    i = 0
    out = []
    for k in l:
        if k == x:
            out.append(i)
        i += 1

    return out

def print_res(res):
    if res == []:
        print(f"Not found")
    else:
        for j in res:
            print(f"Position {j}")



try:
    list = input('Enter your list separated by space: ').split()
    N = input('Enter element to search: ')
except:
    print('Oops, smth wrong')

print_res(list_find(list, N))