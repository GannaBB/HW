# При анализиране на данни, събрани като част от научен експеримент, може
# да се наложи да се премахнат най-крайните (големите) стойности, преди да се
# извършват някакви други изчисления. Да се създаде списък от стойностите само с n на
# брой положителни числа. Трябва да се създаде ново копие на създаденият списък с
# премахнатите n най-големи елемента и n най-малките елементи. Редът на елементите
# във върнатия списък не трябва да съвпада с реда на елементите в първоначалния
# списък. Напишете програма, която да чете списък от числа въведени от потребителя и
# да премахва двете най-големи и двете най-малки стойности. Да се принтира новият
# списък, както и оригиналният. Програма трябва да генерира подходящо съобщение за
# грешка, ако потребителят въведе по-малко от 4 стойности.

#list initiation  

i = 0

while i == 0:

    try:
        user_list = list(map(int,input('Enter your list separated by space: ').split()))   
    except:
        print('Invalid value. Values must be integer separated by space')
        continue

    if len(user_list) < 4:
        print('Not enough numbers. Should be minimum 4 values.')
        continue
    else:
        i = 1

# 2 max, 2 min filter
new_list = user_list.copy()
i = 0
for i in range(2):
    new_list.remove(max(new_list))
    new_list.remove(min(new_list))
   
    i += 1

print('Old list: ', user_list)
print('New list: ', new_list)
