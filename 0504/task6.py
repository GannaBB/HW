# Да се напише програма, която да сортира списък от tuples използвайки
# Lambda.

data = [('a',5,3),('g',4),('d',6,1),('e',5),('b')]

data.sort(key=lambda i:i[0])

print(data)