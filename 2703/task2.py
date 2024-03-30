# Да се напише програма, която да създаде множество от множества, което да
# съдържа: А - B, B, B-A, A-B + B-A, A & B, A | B, където A и B са два списъка, чиито
# елементи се въвеждат от клавиатурата.


try:
    list1 = input('Enter 1st list separated by space: ').split()
    list2 = input('Enter 2nd list separated by space: ').split()

except:
    print('Something goes wrong')


list1 = set(list1)
list2 = set(list2)

print(f"Set A= {list1} \nSet B ={list2}")

AplusB = list1.union(list2)
AminusB = list1.difference(list2)
BminusA = list2.difference(list1)
AmBpBmA = AminusB.union(BminusA)
AintersectionB = list1.intersection(list2)


print(f"A-B = {AminusB}")
print(f"B = {list2}")
print(f"B-A = {BminusA}")
print(f"A-B + B-A = {AmBpBmA}")
print(f"A|B = {AplusB}")


