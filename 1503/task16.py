# Да се създаде програма, която да въвежда текст от клавиатурата и да
# премахва повтарящите се букви в текста.
# Вход: aaabbbccc
# Изход: abc


try:
    text = str(input('Enter your text: '))
except:
    print('Invalid input')


for l in text:
    
    num = text.count(l)
    index = text.index(l)


    if num > 1:
        text1 = text.replace(l,'')
        text = text1[:index] + l + text1[index:]


print('Cleaned text:', text)


    

