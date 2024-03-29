# Дадено е стандартно класиране на конкуренцията (известно също като „1224“
# класиране) от някакво спортно състезание. Даден е речник, съдържащ имената и
# оценките на 5 състезатели, както и име на състезател, трябва да се напише програма,
# която да връща ранга на въведеният състезател. Рангът се изчислява като на найвисоката позиция в класирането се задава ранг 1, всеки следващ състезател получава
# предходният ранг увеличен с 1. Това може да се види на следващите примери.
# Няма съвпадащи стойности:
# Scores = [99, 98, 97, 96, 95]
# Rank = 1, 2, 3, 4, 5
# Със съвпадащи стойности:
# Scores = [99, 98, 98, 96, 95]
# Rank = 1, 2, 2, 4, 5
# Точките на втора и трета позиция в списъка са равни и затова изпускаме ранг 3.
# Вход:
# competitors = {
#  "George": 96,
#  "Emily": 95,
#  "Susan": 93,
#  "Jane": 89,
#  "Brett": 82
#  }
# competitor_name = “Jane”
# Изход:
# 4
# Вход:
# competitors = {
#  "Kate": 92,
#  "Carol": 92,
#  "Jess": 87,
#  "Bruce": 87,
#  "Scott": 84
#  }
# competitor_name = “Bruce”
# Изход:
# 3

#input of competitors scores

competitors = {}

name='Tom'
# initiating dictionary
while name != '':
    name = input('Enter competitor name: ')
    if name == '':
        break 
    else:
        try:
            scores = int(input('Enter competitor score: '))
            competitors[name] = scores
        except:
            print('Invalid data')

print(competitors)


try:
    competitor_name = input('Enter competitor name to get place: ')
    if competitor_name not in competitors:
        print('This competitor is not in the list')

except:
    print('Invalid data')

#sorting the scores
competitors_new = {}
scores_list=[]

for x in competitors:
    scores_list.append(competitors[x])

scores_list.sort(reverse = True)

#new dictionary with place 

for x in competitors:
    for i in range(len(scores_list)):
        if competitors[x] == scores_list[i]:
            if scores_list[i]==scores_list[i-1]:
                competitors_new[x] = i
            else:
                competitors_new[x] = i+1

print(competitor_name, ' takes: ', competitors_new[competitor_name], 'place')



