# Създаване на калкулатор, който да може да пресмята събиране,
# умножение, деление и изваждане. Да се създаде модул calculator, който да съдържа
# функциите add, subtract, multiplication, division. Да се създаде и друг модул, в който
# да се извикат тези функции, модулът да се казва task2_calculation.py. Да се накара
# потребителят да въведе двете числа. Модулът calculator.py да има и функция за
# принтиране на резултата. 

try:
    number1 = float(input('Enter first number: '))
    number2 = float(input('Enter second number: '))
except:
    print('Invalid data')


import calculator

try:
    k = int(input(f'Choose your action: \n 0 to add \n 1 to substract \n 2 to multiply \n 3 to divide: '))
    if k < 0 or k > 3:
        print('Must be between 0 and 3')
        exit()
        
except:
    print('Must be integer')

if k == 0:
    calculator.print_res(calculator.add(number1,number2)) 
elif k ==1:
    calculator.print_res(calculator.substract(number1,number2))
elif k ==2:
    calculator.print_res(calculator.multiplication(number1,number2)) 
elif k ==3:
    calculator.print_res(calculator.division(number1,number2)) 

    
