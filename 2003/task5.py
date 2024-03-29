# За да спечели най-голямата награда в определена лотария, човек трябва да
# съпостави всичките 6 числа от билета си с 6-те числа между 1 и 49, които са изтеглени от
# организатора на лотарията. Напишете програма, която генерира произволен избор от 6
# числа за лотариен билет. Уверете се, че избраните 6 числа не се повтарят. Покажете
# числата във възходящ ред.


import random

# create a list of winning numbers
winning_numbers = []

i = 0
while i<6:
    random_number = random.randint(1, 49)

    if random_number not in winning_numbers:
        winning_numbers.append(random_number)
        i += 1

winning_numbers.sort()

print(winning_numbers)

# create user numbers
user_numbers = []
length = 0

while length != 6:
    try:
        user_numbers = list(map(int,input('Enter your 6 numbers from 1 to 49: ').split()))
        length = len(user_numbers)
 
        if length < 6:
            print('Missing number. Add', 6-length,' more: ')
            x = list(map(int,input().split()))
            for i in x:
                user_numbers.append(i)
            length = len(user_numbers)       
        
        elif length > 6:
            print('Too many numbers. Try again')

        for i in user_numbers:
                if i > 49:
                    print('One of number is out of range. Try again')
                    length = 0

    except:
        print('Invalid unput')

# compare user and winning numbers

                  
if winning_numbers==user_numbers:
    print('You win') 
else:
    print('No win')   




