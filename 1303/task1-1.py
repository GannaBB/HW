#""" DESCRIPTION:
#    Write a program that takes a number as input and checks if it is positive, negative, or zero.
#"""

### Your code here

### EXPECTED OUTPUT:
# "Enter a number: -2.45"
# "Number -2.45 is negative."


try:

    x = float(input('Enter a number: '))

    if x==0:
        print(x,'is zero')
    elif x>0:
        print(x, 'is positive')
    else:
        print(x, 'is negative')

except:
    print('Enter valid number')