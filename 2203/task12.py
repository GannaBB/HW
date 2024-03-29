# Да се напише програма, която да създава речник от стринг. Ключовете на
# речника трябва да бъдат буквите от стринга, а стойностите броят на повторение на
# буквите в стринга.
# Вход: “Hello world”
# Изход: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# Вход: “Greeting 3>“
# Изход: {'g': 2, 'r': 1, 'e': 2, 't': 1, 'i': 1, 'n': 1, ' ': 1, '3': 1, '>': 1}”
# Вход: “ ”
# Изход: {}


try:
    input_txt = str(input('Enter your text: '))
except:
    print('Eror')

    
input_txt = input_txt.lower()
res = {}
for a in input_txt:
    res[a] = input_txt.count(a)

print(res)

