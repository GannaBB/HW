# Да се създаде програма, която да въвежда текст от клавиатурата и да
# премахва повтарящите се букви в текста.
# Вход: aaabbbccc
# Изход: abc


try:
    text = str(input('Enter your text: '))
except:
    print('Invalid input')

old_str = text

# option 1
for l in text:
    
    num = text.count(l)
    index = text.index(l)


    if num > 1:
        text1 = text.replace(l,'')
        text = text1[:index] + l + text1[index:]


print('Cleaned text:', text)



# option 2
new_str = ''
for i in old_str:
    if i not in new_str:
        new_str = new_str + i

print('Cleaned text:', new_str)
