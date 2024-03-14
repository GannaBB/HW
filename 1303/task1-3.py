#""" DESCRIPTION:
#   Develop a simple temperature converter program that converts temperatures from Fahrenheit to Celsius and vice versa based on user choice. Make a user-friendly interface as given in EXPECTED OUTPUT:.
#
#   Temperature conversions use the following formulas:
#  Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
# Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
#"""

### Your code here

### EXPECTED OUTPUT:
# **********Fahrenheit/Celsius Converter ***********
# # 1 => Convert to Fahrenheit                     #
# # 2 => Convert to Celsius                        #
# **************************************************
# Enter your choice [1/2]: 1
# Enter temperature in C: 20
# 20.0C = 68.0F

try:

    print(f"{' Fahrenheit/Celcius Converter ' :*^50}")
    print('1 => Convert Celcius to Fahrenheit')
    print('2 => Convert Fahrenheit to Celcius ')
    print('*'*50)

    choice = int(input('Enter your choice [1/2]: '))

    if not choice==1 and not choice==2:
        print('Input should be 1 or 2')
        exit()
    
    if choice==1:
        temp = float(input('Enter temperatur in Celcius: '))
        convert_temp = temp*9/5+32
        print(temp,'\N{DEGREE SIGN}C =', convert_temp,'\N{DEGREE SIGN}F')
    else:
        temp = float(input('Enter temperatur in Fahrenheit: '))
        convert_temp = (temp-32)*5/9
        print(temp,'\N{DEGREE SIGN}F =', convert_temp,'\N{DEGREE SIGN}C')



except:
    print('Enter a valid data')

