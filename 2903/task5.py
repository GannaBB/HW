#  Да се напише програма, която да реализира итератор на нечетни числа.


value_max = 100

from itertools import count

odd_numbers = count(1,2)

i = 0
while i < value_max:
    print(next(odd_numbers))
    i += 2