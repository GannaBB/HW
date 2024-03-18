# Да се напише програма, която да приема като вход текст и да намира
# количеството знаци в текста. Включват се интервалите и текста трябва да е с малки
# букви. Ако няма дубликати, да се принтира 0.
# Вход: Hello World! Вход: foobar Вход: birthday Вход: helicopter
# Изход: 3 Изход: 1 Изход: 0 Изход: 1

try:
    text = str(input('Enter your text: '))
except:
    print('Invalid input')


count1 = 1
text_lower = text.lower()

for l in text_lower:
    count = 0
    for x in text_lower:
        if x==l:
            count = count + 1
    
    if count>count1:
        count1=count
        count=0


if count1==1:
    count1 = 0

print(count1)
