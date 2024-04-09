#  Да се напише програма, която да реализира итератор на четни числа.


value_max = 100

from itertools import count

even_numbers = count(0,2)

i = 0
while i <= value_max:
    print(next(even_numbers))
    i += 2

