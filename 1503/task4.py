#Да се напише програма, която да обръща буквите на дадена дума на обратно.
#Думата да бъде въведена от клавиатурата. Като за целта използвате цикъл.
#Вход:
#Input a word to reverse: Hello
#Изход:
#olleH

text = input('Enter word to reverse: ')

x = len(text)

for i in range(x):
    print(text[x-i-1],end='')

