# Да се напише програма, която да кара потребителят да въвежда стринг от
# клавиатурата и да поставя всички гласни в едни списък и всички съгласни в друг.

try:
    text = str(input("Enter your text: "))
except:
    print('Wrong input')

vowels = ('a', 'e', 'i', 'o', 'u', 'y')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

text = text.lower()

vowels_l = ''
consonants_l = ''
other_l = ''



for i in text:
    if i in vowels:
        vowels_l += i
    elif i in consonants:
        consonants_l += i
    else:
        other_l += i
    
print(f" Vowels: {vowels_l} \n Consonants: {consonants_l} \n Not letters: {other_l}")


