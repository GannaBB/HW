# . Да се напише програма, която да намира сечението на два списъка
# използвайки lambda.


list1 = [2,5,'g',7,4,'d',8,5,4]
list2 = [1,5,3,'f', 6, 'a','g']


list_intersection = list(filter(lambda x: x in list1, list2))



print(list_intersection)