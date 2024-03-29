# В играта на Scrabble всяка буква има точно определени зададени точки.
# Общият резултат за една дума е сборът от точките за всяка една от нейните букви. Почесто срещаните букви имат по-малко точки, докато по-малките букви имат повече.
# Точките, свързани с всяка буква, са показани по-долу:
# Напишете програма, която изчислява и показва резултата от Scrabble за дадена дума.
# Създайте речник, който преобразува от букви в точки. След това използвайте речника,
# за да изчислите резултата.



# creation of dictionary:
res = {'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's': 1, 't':1, 'u':1,
       'd':2, 'g':2,
       'b':3, 'c':3, 'm':3, 'p':3,
       'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
       'k':5,
       'j':8, 'x':8,
       'q':10, 'z':10}


try:
    control = 0
    while control == 0:
        txt = input('Enter your word: ')
        if ' ' in txt:
            print('You can enter only one word. Try again')
            continue
        elif txt.isalpha() == False:
            print('You can enter only letters. Try again')
            continue
        else: control = 1
        
except:
    print('Invalid input')

    

txt = txt.lower()

# score calculation
sum = 0
for a in txt:
    sum += res[a]

print(sum)