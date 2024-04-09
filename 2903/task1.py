# Да се напише програма, която да реализира генератор на четни числа.




def generator_even(n):
    
    i = 0
    while i <= n:
            yield i
            i += 2


max_value = 100
for i in generator_even(max_value):
      print(i)
