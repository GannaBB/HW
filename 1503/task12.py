#Да се състави програма, която извежда числов триъгълник изобразяващ
#следната последователност:
#1
#1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

x = 9

for i in range(x+1):
    for j in range(i):
        print(j+1, end=' ')
    print()


