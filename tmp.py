weight = float(input('Enter your weight in kg: '))

if weight<0 or weight>400:
    print('Invalid input')
    exit()

height = float(input('Enter your height in m: '))

if height<0 or height>3:
    print('Invalid input')
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

print('Your BMI =', BMI,cat)