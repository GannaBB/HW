#  Да се напише програма, която създава речник, който да съдържа следните
# операции |, &, -, между две множества a и b. Множествата да се въвеждат от
# клавиатурата. Речникът да има за ключ конкретната операция, а за стойност полученият
# резултат от изпълнението на операцията.
# Вход: a ={1,2} b = {2, 3}
# Изход:
# {
#  "{1, 2} | {2, 3}": {1, 2, 3},
#  "{1, 2} & {2, 3}": {2},
#  "{1, 2} - {2, 3}": {1}
# } 

try:
    set1 = set(input('Enter 1st list separated by space: ').split())
    set2 = set(input('Enter 2nd list separated by space: ').split())

except:
    print('Something goes wrong')

AunionB = set1.union(set2)
AintB = set1.intersection(set2)
AminusB = set1.difference(set2)

a = str(set1) +' | ' + str(set2)
b = str(set1) +' & ' + str(set2)
c = str(set1) +' - ' + str(set2)

res = {a: AunionB, 
       b: AintB,
       c: AminusB }

print(f"{a}: {res[a]} \n{b}: {res[b]} \n{c}: {res[c]}")