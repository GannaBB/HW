# Задача 13. Да се напише програма, която да групира думи по броят на главните букви в
# тях. Резултатът да се запази в речник, чиито ключове трябва да са броят на главните
# букви, а стойностите списък с думите. Думите не трябва да се повтарят в списъка.
# Вход: ["HaPPy", "mOOdy", "yummy", "mayBE"]
# Изход: {3: ['HaPPy'], 2: ['mayBE', 'mOOdy'], 0: ['yummy']}
# Вход: ["eeny", "meeny", "miny", "moe"]
# Изход: {0: ['eeny', 'meeny', 'miny', 'moe']}
# Вход: ["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]
# Изход: {2: ['bOR', 'MoR', 'tOR'], 3: ['FORe'], 0: ['lor'], 1: ['sOr']}


# input_list =  ["FORe", "MoR", "bOR", "tOR", "sOr", "lor"]
try:
    input_list = list(map(str,input('Enter your list separated by space: ').split()))   
except:
    print('Invalid value. Values must be integer separated by space')

print(input_list)

# count upper cases
l = len(input_list)
count = input_list.copy()
for i in range(l):
    count[i] = 0
    for a in input_list[i]:
        if a.isupper() == True:
           count[i] += 1

res = {}

#create an output
for i in range(l):
    txt = []
    for j in range(l):
        if count[i] == count [j]:
            txt.append(input_list[j])

    res[count[i]] = txt


print(res)
