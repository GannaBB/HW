# Да се напише програма, която да брои четните и нечетните числа в даден
# списък от цели числа, използвайки lambda.

lst = [1,4,5,6,1,3,8,6,2,7,5,3]

even = len(list(filter(lambda x: x%2==0 if x!=0 else False, lst)))
odd = len(list(filter(lambda x: x%2!=0 if x!=0 else False, lst)))

print(f'Number of even numbers: {even}')
print(f'Number of odd numbers: {odd}')