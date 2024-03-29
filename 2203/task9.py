# Две думи са анаграми, ако всичките им букви са еднакви, но в различен ред.
# Например “evil” и “live” са анаграми. Създайте програма, която чете два низа от
# потребителя, дали са анаграми или не

#input
try:
    control = 0
    while control == 0:
        txt1 = input('Enter 1st word: ')
        if ' ' in txt1:
            print('You can enter only one word. Try again')
            continue
        elif txt1.isalpha() == False:
            print('You can enter only letters. Try again')
            continue
        else: control = 1
        
except:
    print('Invalid input')



try:
    control = 0
    while control == 0:
        txt2 = input('Enter 2nd word: ')
        if ' ' in txt2:
            print('You can enter only one word. Try again')
            continue
        elif txt1.isalpha() == False:
            print('You can enter only letters. Try again')
            continue
        else: control = 1

        if len(txt1) != len(txt2):
            print('Your words must have same length. Try again')
            continue
        
except:
    print('Invalid input')


txt1_dict = {}
for a in txt1:
    txt1_dict[a] = txt1.count(a)

txt2_dict = {}
for a in txt2:
    txt2_dict[a] = txt2.count(a)



if txt1_dict == txt2_dict:
    print(txt1, ' and ', txt2, ' are anagramms')
else:
    print(txt1, ' and ', txt2, ' are not anagramms')
