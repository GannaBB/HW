# Задача 4. Да се напише програма, която да проследява валежите в редица градове.
# Потребителят да може да въвежда името на град; ако името на града е празно,
# програмата излиза и принтира отчет. Ако името на града не е празно, потребителят
# ще трябва да въведе информация за количеството дъжд за конкретният
# град(обикновено се измерва в милиметри). След въвеждане на количеството дъжд,
# потребителят има възможност да въвежда следващ град и количество дъжд и това
# ще го прави докато не натисне „Enter“, вместо да напише името на града.
# Пример:
# Boston
# 5
# New York
# 7
# Boston
# 5
# [Enter; blank line]
# Изход:
# Boston: 10
# New York: 7


# dictionaty initiation
rain_level = {'Boston': 5}
rain_level['New Yourk'] = 7
rain_level['London'] = 10
rain_level['Paris'] = 2
rain_level['Prague'] = 1
rain_level['Sofia'] = 0
rain_level['Athene'] = 11
rain_level['Berlin'] = 3
rain_level['Milano'] = 6
rain_level['Madrid'] = 7


# input
city='Boston'
output = []
i = 0
while city != '':
    city = 'Boston'

    while city in rain_level:
        city = input('City: ')
        if city == '':
            break 
        elif not city in rain_level:
            print('Sorry, we dont have this information. Try another city')
             
        else:
            txt = city + ': ' + str(rain_level[city])
            output.append(txt)
            i += 1
        
      

# removing duplicates
res =[]
for x in output:
    if x not in res:
        res.append(x)
            
#print out
n = len(res)      
print(n)     

for i in range(n):
    print(res[i])
     


