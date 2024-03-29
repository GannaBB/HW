# Карта Бинго се състои от 5 колони от 5 числа. Колоните са обозначени с
# буквите B, I, N, G и O. Има 15 числа, които могат да се появят под всяка буква. Поспециално, числата, които могат да се появят под B варират от 1 до 15, числата, които
# могат да се появят под I, варират от 16 до 30, числата, които могат да се появят под N
# диапазон от 31 до 45, и така нататък. Напишете програма, която създава произволна
# бинго карта и я съхранява в речник. Ключовете ще бъдат буквите B, I, N, G и O.
# Стойностите ще бъдат списъците на пет числа, които се появяват под всяка буква. Да се
# принтира картата Бинго заедно с колоните, обозначени по подходящ начин. 


import random

# create a list of winning numbers


bingo = ['B','I', 'N', 'G', 'O']
card = {}

for i in range(5):
    j = 0
    winning_numbers = []
    min_N = 15 * i +1
    max_N = min_N + 14
    while j < 5:
        random_number = random.randint(min_N, max_N)

        if random_number not in winning_numbers:
            winning_numbers.append(random_number)
            j += 1
    
    card[bingo[i]] = winning_numbers

#caed output
for i in range(5):
    print(f"{'|'}{bingo[i]:^5}", end='')
print()
print('-'*30)

for i in range(5):
    for j in range(5):
        print(f"{'|'}{card[bingo[j]][i]:^5}", end ='')
    print()
    print('-'*30)
     


    

