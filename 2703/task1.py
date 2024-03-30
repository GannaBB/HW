# Да се напише програма, която сортира в нарастващ ред списък, чиито елементи
# са tuples. При сортирането да се взема предвид последният елемент във всеки tuple. В
# списъкът не трябва да се съдържат празни tuples.
# Вход: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Изход: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# list_input = [(2,5),(1,2),(4,4),(2,3),(2,1)]

list_input =[]

x = 1
while x != '':
    try:
        x = input('Enter numbers for your tuple: ')
    except:
        print('Oops, something goes wrong')
    if x == '':
        break    
    inp_tuple = tuple(map(int,x.split(' ')))
    list_input.append(inp_tuple)
   

print(f"Initial list: {list_input}")



new_list = sorted(list_input, key=lambda a: a[-1])

print(f"Sorted list: {new_list}")
