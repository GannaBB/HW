# Напишете генератор, който да намира аритметична прогресия, като
# потребителят въвежда началото, стъпката на прогресия и колко числа да покаже от
# редицата.

def arithmetic_progression(a1,n,d):
    i = 1
    an_list = []
    while i <= n:
        an = a1 + (i-1) * d
        an_list.append(an)
        i += 1
    
    yield an_list
    
        

try:
    first_el = float(input('Enter first element of arythmetic progression: '))
    step = float(input('Enter step: '))
    n_max = int(input('Enter number of elements to show: '))

except:
    print('Wrong input type')



print(f"Resulted progression: {next(arithmetic_progression(first_el,n_max,step))}")