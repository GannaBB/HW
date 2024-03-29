# Задача 8. Напишете програма, която намира максималната редица от последователни
# нарастващи елементи в списък.
# Пример: {3, 2, 3, 4, 2, 2, 4} -> {2, 3, 4}.

#initiating user list
try:
    user_list = list(map(int,input('Enter your list separated by space: ').split()))   
except:
    print('Invalid value. Values must be integer separated by space')


# #trick to take into account last element if two last are the same
if user_list[-1] > user_list[-2]:
    user_list.append(user_list[-1]-1)


# determine quantity of sequence of growing elements
num_sublists=[]

n = len(user_list)

k = 1

for i in range(n-1):

    if user_list[i] < user_list[i+1]:
        k += 1
    else:
        num_sublists.append(k)
        k = 1


# determine data to slice list    
index_max = num_sublists.index(max(num_sublists))

sum = 0
for i in range(index_max):
    sum += num_sublists[i]

new_list = user_list[sum:sum+num_sublists[index_max]]
print(new_list)

