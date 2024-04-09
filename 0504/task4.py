# Да се напише програма, която да пита потребителя да въведе число от
# клавиатурата и да пресметне факториелът на това число. Да се използва рекурсия.
# Вход: Enter the number 5
# Изход: Factorial of 5 is 120


def factorial(x):
    m = 1
    i = 1
    for i in range(1,x+1):
        m = m* i
    
    return(m)


try:
    n = int(input('Enter the number: '))
except:
    print('Must be an integer')
    
print(f"Factorial of {n} is {factorial(n)}")