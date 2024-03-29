# Да се напише програма, която да реализира тълковен речник. Програмата да
# може да търси по въведена дума, като например, ако речникът е френско-английски, то
# речника да може да предостави по въведена английска дума, съответният й еквивалент
# на френски. Ако английската дума се среща в речникът няколко пъти, то резултатът да
# бъде записан в списък, който след това да бъде принтиран. Ако думата не съществува да
# се изведе празен списък.


# definition of dictionary
dictionary = {'син': 'blue', 'червен':'red', 'жълт':'yellow', 'розов':'pink','черен':'black', 'сив':'grey','зелен':'green', 'небесно':'blue'}


try:
    control = 0
    while control == 0:
        txt = input('Enter word ')
        if ' ' in txt:
            print('You can enter only one word. Try again')
            continue
        elif txt.isalpha() == False:
            print('You can enter only letters. Try again')
            continue
        else: control = 1
        
except:
    print('Invalid input')

res = []

for a in dictionary:
    if txt == dictionary[a]:
        res.append(a)

        
print(res)