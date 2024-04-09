# Да се напише генератор, който да намира геометрична прогресия, като
# потребителят въвежда началото, стъпката и колко числа да покаже.

def geometric_progression(a1,n,d):
    i = 1
    an_list = []
    while i <= n:
        an = a1 * (d ** (i-1))
        an_list.append(an)
        i += 1
    
    yield an_list
    
        

try:
    first_el = float(input('Enter first element of geometric progression: '))
    step = float(input('Enter step: '))
    n_max = int(input('Enter number of elements to show: '))

except:
    print('Wrong input type')



print(f"Resulted progression: {next(geometric_progression(first_el,n_max,step))}")