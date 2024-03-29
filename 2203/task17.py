#  Даден е речник студенти и техните точки от тест. Имената на студентите са
# ключове на речника, а техните точки са запазени в списък. Да се напише програма, която
# да изчислява средните точки на всеки един от студентите и да извежда на екрана този,
# който има най-висок среден резултат.
# Вход:
# student_scores = {
#  "John": [100, 90, 80],
#  "Bob": [100, 70, 80]
# }
# Изход: John
# Вход:
# student_scores = {
#  "Susan": [67, 84, 75, 63],
#  "Mike": [87, 98, 64, 71],
#  "Jim": [90, 58, 73, 86]
# }
# Изход: Mike

data = {}

name='Tom'
# initiating dictionary
while name != '':
    name = input('Enter student name: ')
    if name == '':
        break 
    else:
        try:
            scores = list(map(int,input('Enter student scores separated by space: ').split()))   
            data[name] = scores
        except:
            print('Invalid data')


#to find average
scores_av = {}

for x in data:
    score_av = sum(data[x])/len(data[x])
    scores_av[x] = score_av

#to find the nest student
best_student = max(scores_av, key = scores_av.get)

#print(scores_av)
print(best_student)



