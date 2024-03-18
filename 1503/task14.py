# Да се напише програма, която да генерира число на случен принцип и да
# подкани потребителя да познае това число. Да извежда следните стойности too low, too
# high, или exactly right, в случай, че потребителя е познал, или не числото


import random
try:
    max_range = int(input('Enter maximum possible value: '))
except:
    print('It must be integer')
    exit()

random_number = random.randint(0,max_range)

#print(random_number)

user_number = -1
while user_number!=random_number:
    try:

        user_number = int(input('Guess number: '))
    except:
        print('It must be integer')

    if user_number>random_number:
        print('>>Too high')
    elif user_number<random_number:
        print('>>Too low')
    
print('>>Exactly right')

