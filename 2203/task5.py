
# . Да се напише програма, която да намира разликата между два речника.
# Като резултат програмата да генерира нов речник, който да съдържа разликата
# между двата речника. Ако няма разлика между речниците да се принтира празен
# речник. За всяка двойка ключ-стойност, която се различава, да се запазят
# различаващите се стойности в списък, а списъкът да се запази в речник, като
# ключът да съвпада с текущият. Ако някой от речниците не съдържат даденият
# ключ, то в списъкът, той трябва да бъде записан като None.
# Вход: Вход: Вход:
# d1 = {'a':1, 'b':2, 'c':3} d3 = {'a':1, 'b':2, 'd':3} d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':1, 'b':2, 'c':4} d4 = {'a':1, 'b':2, 'c':4} d5 = {'a':1, 'b':2, 'd':4}
# Изход: Изход: Изход:
# {'c': [3, 4]} {'c': [None, 4], 'd': [3, None]} {'c': [3, None], 'd': [None, 4]}
# Вход: d1 = {'a':1, 'b':2, 'c':3} и d1 = {'a':1, 'b':2, 'c':3}
# Изход: {}

# initiatin 1st dictionary
d1 = {'a':1, 'b':2, 'c':3}
res_dict = {}
#initiaiting 2nd dicitonary
d2 = {'a':1, 'b':2, 'c':3}

for x in d1:

    if x not in d2:
        res_dict[x] = [d1[x], 'None']
        continue
    elif d1[x] == d2[x]:
        pass
    elif d1[x] != d2[x]:
        res_dict[x] = [d1[x], d2[x]]

for y in d2:
    if y not in d1:
        res_dict[y] = ['None', d2[y]]
        continue
    
        

print(res_dict)



