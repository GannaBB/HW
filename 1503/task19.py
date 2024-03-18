# . Да се напише програма, която приема като вход текст и обръща буквите от
# дясно наляво на само на думите, чиято дължина е нечетна, тези които са с четен брой
# си остават така като са.
# Вход: Bananas Вход: One two three four
# Изход: sananaB Изход: enO owt eerht four
# Вход: Make sure uoy only esrever sdrow of ddo length
# Изход: Make sure you only reverse words of odd length


try:
    text = str(input('Enter your text: '))
except:
    print('Invalid input')



text_split = text.split()

count_word = len(text_split)

text_out = ''

for i in range(count_word):
    if len(text_split[i])%2==0:
        text_interim = text_split[i]
    else:
        text_interim=''
        for l in text_split[i]:
            text_interim = l + text_interim
    
    text_out = text_out + ' ' + text_interim

print('New text:',text_out)
    




