# Да се напише програма, която да създава tuple (a, b), представящ броят на
# уникалните елементи в дадено множество и b представящо броят на дублицираните
# елементи в множеството. Множеството да се въвежда от клавиатурата.

try:
    set1 = set(input('Enter 1st list separated by space: ').split())
    set2 = set(input('Enter 2nd list separated by space: ').split())

except:
    print('Something goes wrong')

unique_elements = set1.union(set2)
duplicates = set1.intersection(set2)

a = len(unique_elements)
b = len(duplicates)

res = (a, b)

print(res)