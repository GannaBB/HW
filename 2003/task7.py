# Напишете програма, която намира максимална редица от последователни
# еднакви елементи в списък.
# Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter

#initiating user list
try:
    user_list = list(map(int,input('Enter your list separated by space: ').split()))   
except:
    print('Invalid value. Values must be integer separated by space')

#trick to take into account last element if two last are the same
if user_list[-1] == user_list[-2]:
    user_list.append(user_list[-1]+1)


# determine quantity of sequence of equal elements
num_sublists=[]

n = len(user_list)
k = 1

for i in range(n-1):

    if user_list[i] == user_list[i+1]:
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
print(new_list[0], ' * ',len(new_list) )

    

