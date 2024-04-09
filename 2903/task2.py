# Да се напише програма, която да реализира генератор на нечетни числа.




def generator_odd(n):
    
    i = 1
    while i <= n:
            yield i
            i += 2


max_value = 101
for i in generator_odd(max_value):
      print(i)


