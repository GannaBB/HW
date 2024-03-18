# Да се напише програма, която подканва потребителя да въведе число и
# програмата да провери дали то е просто или не.
# Вход:
# Please enter a number
# >>> 12
# Изход:
# The number is not prime.


try:
    x = int(input('Enter a number: '))
except:
    print('Number must be integer')
    exit()


for i in range(2,x):
   
    if x%i==0:
        print('The number is not prime')
        exit()

print('The number is prime')