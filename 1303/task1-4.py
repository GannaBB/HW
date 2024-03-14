#""" DESCRIPTION:
#    Write a Body mass index (BMI) calculator program, which asks the user for:
#    weight in kilograms
#    height in meters
#
#    Calculate the BMI = W / (H*H)
#    where:
#    W = weight in kilograms
#    H = height in meters
#
#    Display to the user the BMI and basic category, using next table:
#
#    | ------------------------------- | ----------- |
#   | category                        | BMI         |
#    | ------------------------------- | ----------- |
#    | Underweight (Severe thinness)   | < 16.0      |
#    | Underweight (Moderate thinness) | 16.0 - 16.9 |
#    | Underweight (Mild thinness)     | 17.0 - 18.4 |
#    | Normal range                    | 18.5 - 24.9 |
#    | Overweight (Pre-obese)          | 25.0 - 29.9 |
#    | Obese (Class I)                 | 30.0 - 34.9 |
#    | Obese (Class II)                | 35.0 - 39.9 |
#    | Obese (Class III)               | ≥ 40.0      |
#    | ------------------------------- | ----------- |
#"""

### Your code here

### EXPECTED OUTPUT:
# Enter weight in kilograms: 92
# Enter height in meters: 1.78
# Your BMI = 29.04, Category: Overweight (Pre-obese)

try:

    weight = float(input('Enter your weight in kg: '))

    if weight<0 or weight>400:
        print('Invalid weight')
        exit()

    height = float(input('Enter your height in m: '))

    if height<0 or height>3:
        print('Invalid height')
        exit()

    BMI = round(weight/(height*height),2)

    if BMI<16:
        cat = 'Underweight (Severe thinness)'
    elif BMI<=16:
        cat = 'Underweight (Moderate thinness)'
    elif BMI<=18.4:
        cat = 'Underweight (Mild thinness)'
    elif BMI<=24.9:
        cat =  'Normal range'
    elif BMI<=29.9:
        cat = 'Overweight (Pre-obese)'
    elif BMI<=34.9:
        cat = 'Obese (Class I)'
    elif BMI<=39.9:
        cat = 'Obese (Class II)'
    else: 
        cat = 'Obese (Class III)'

    print(' Your BMI =', BMI,'\n',cat)

except:
    print('Invalid input')
