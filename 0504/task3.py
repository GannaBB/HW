#  Да се напише програма, която да пита потребителя да въведе едно число от
# клавиатурата и да покаже съответното число от редицата на Фибoначи. Задачата да се
# реши с рекурсивна функция.
# Вход: Enter the number 5
# Изход: The 5th fib term is 5.

def fib(n):

    if n == 1 or n ==2:
        res = 1

    else:
        f1 = 1
        f2 = 1
        for i in range(2,n):
            k = f2
            f2 += f1
            f1 = k
        res = f2

    return(res)


try:
    n_max = int(input('Enter an integer: '))
except:
    print('Must be an integer')
    
print(f"The {n_max}th fib term is {fib(n_max)}")