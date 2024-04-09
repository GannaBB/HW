# Да се промени задача 8 така, че да използва итератор.

try:
    text = str(input("Enter your text: "))
except:
    print('Wrong input')

vowels = ('a', 'e', 'i', 'o', 'u', 'y')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z')

text = text.lower()
text_it = iter(text)
vowels_l = ''
consonants_l = ''
other_l = ''


while True:
 
    try:
        x = next(text_it)
        if x in vowels:
            vowels_l += x
        elif x in consonants:
            consonants_l += x
        else:
            other_l += x
    except StopIteration:
        break
    
print(f" Vowels: {vowels_l} \n Consonants: {consonants_l} \n Not letters: {other_l}")


