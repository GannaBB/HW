# Да се напише програма, която генерира всички подсписъци на даден списък.
# Например, списъците на [1, 2, 3] са [], [1], [2], [3], [1, 2], [2, 3], [1, 3] и [1, 2, 3]. 


user_list = [1, 2, 3, 4] 

l_list = len(user_list)

out_list = []

for x in range(l_list):
    for y in range(x+1, l_list+1):
        out_list.append(user_list[x:y])

res = sorted(out_list, key=len)
print(res)





    