# Да се преработи следната задача, така че да използва речник. Да се напише
# програма, която да изчислява дневният калориен прием на даден потребител, като
# данните се въвеждат от клавиатурата. Необходимите данни са: възраст, пол (‘f’, ‘m’),
# височина (в сантиметри), тегло (в килограми), ниво на физическа активност (някоя от
# стойностите от 1 до 6 по-долу). Ниво на физическа активност се определя в следните
# няколко категории:
# 1 – базална метаболитна скорост
# 2 - заседнал – малка или никаква активност
# 3 - лека активност (1-3 пъти седмично) BMR * 1.2 BMR * 1.375
# 4 - средна активност(3-5 пъти седмично) BMR * 1.55
# 5 - висока активност (6-7 пъти седмично) BMR * 1.725
# 6-многовисокаактивност (6–7пъти седмично + тежка физическа работа). BMR*1.9
# Да се изчисли и какъв трябва да бъде дневният прием на калории ако:
# - за да запазите сегашното си тегло
# - за да сваляте по 0.5 кг на седмица
# - за да сваляте по 1 кг. на седмица
# - за да качвате по 0.5 кг. на седмица
# - за да качвате по 1 кг. на седмица
# Да се принтират данните на потребителя, както и калорийният прием спрямо горните
# няколко точки.
# Формула за изчисление на BMR при мъже:
# BMR = 66.47 + ( 13.75 × weight in kg ) + ( 5.003 × height in cm ) − ( 6.755 × age in years )
# Формула за изчисление на BMR при жени:
# BMR = 655.1 + ( 9.563 × weight in kg ) + ( 1.85 × height in cm ) − ( 4.676 × age in years )
# Пример:
# Входни данни:
# 29
# f
# 172
# 63.5
# 4
# Изход:
# Имате нужда от 2240 Калории на ден за да поддържате теглото си
# Имате нужда от 1740 Калории на ден за да сваляте по 0.5 кг на седмица
# Имате нужда от 1240 Калории на ден за да сваляте по 1 кг на седмица
# Имате нужда от 2740 Калории на ден за да качвате по 0.5 кг на седмица
# Имате нужда от 3740 Калории на ден за да качвате по 1 кг на седмица
# Пояснения:
# Години = 29
# Пол = “f”
# Ръст = 172
# Килограми = 63.5
# Ниво на активност = 4
# Изчисляваме BMR по формулата за жени:
# BMR = 655.1 + ( 9.563 * 63.5) + ( 1.85 * 172) − ( 4.676 * 29 ) = 1444.9465 калории
# Добавяме и активността на потребителя:
# Активността е 4 и гледаме по-нагоре каква е стойността за ниво 4. А тя е 1.55.
# BMR = BMR * 1.55 = 2239.6670750000003 = 2240 калории
# След това изчисляваме калориите какви трябва да са, ако искаме да сваляме килограми
# - при 0.5 кг седмица = BMR – 500 гр. = 1740 калории
# - при 1 кг на седмица = BMR – 1000 гр. = 1240 калории
# След това изчисляваме калориите какви трябва да са, ако искаме да качваме килограми
# - при 0.5 кг седмица = BMR + 500 гр. = 2740 калории
# - при 1 кг на седмица = BMR + 1000 гр. = 3240 калории

# input
try:
    
    age_input = 151
    while age_input > 150:
        age_input = int(input('Enter your age: '))
   
        if age_input > 150:
            print ('You cant be so old. Try again')
      
        continue
    
except:
    print('Invalid input')

try:
    gender_input = 'd'

    while gender_input != 'f' or gender_input != 'm':

        gender_input = str(input('Enter your gender m/f: '))
   
        if gender_input == 'f' or gender_input == 'm':
            break
        else:
            print ('You can choose only between "m" for male and "f" for female. Try again')
      
        continue
    
except:
    print('Invalid input')


try:
    
    height_input = 301
    while height_input > 300 or height_input < 50:
        height_input = int(input('Enter your height in cm: '))
   
        if height_input > 300:
            print ('You cant be so tall. Try again')
        if height_input < 50:
            print ('Are you new born? Try again')
      
        continue
except:
    print('Invalid input')   

try:
    
    weight_input = 501
    while weight_input > 500 or weight_input < 30:
        weight_input = float(input('Enter your weight in kg (not nesesarily to be rounded): '))
   
        if weight_input > 500:
            print ('Extreme overweight. Please, contact doctor or try again')
        if weight_input < 30:
            print ('Extreme low weight. Please, contact doctor or try again')
      
        continue
except:
    print('Invalid input')     

try:
    print('Choose your activity level acc. to the info below:')
    print('1 - basal metabolic speed')
    print('2 - low or no activity')
    print('3 - light activity (1-3 weekly)')
    print('4 - moderate activity (3-5 weekly)')
    print('5 - hight activity (6-7 weekly)')
    print('6 - very high activity (6-7 weekly + hard physical work)')

    activity_input = 8
    while activity_input > 6 :
        activity_input = int(input('Shoose your activity level 1 to 6: '))
   
        if activity_input > 6:
            print ('Out of range. Try again')
              
        continue
except:
    print('Invalid input')     


#dictionary initining
data = {'age': age_input, 'gender': gender_input, 'height':  height_input, 'weight': weight_input, 'activity_level': activity_input}

#calculation
if data['gender'] == 'm':
    BMR = 66.47 + (13.75 * data['weight']) + (5.003 * data['height']) - (6.755 * data['age'])

else:
    BMR = 655.1 + (9.563 * data['weight']) + (1.85 * data['height']) - (4.676 * data['age'])


if data['activity_level'] == 2:
    BMR = BMR*1.2
elif data['activity_level'] == 3:
    BMR = BMR * 1.375
elif data['activity_level'] == 4:
    BMR = BMR * 1.55
elif data['activity_level'] == 5:
    BMR = BMR * 1.725
elif data['activity_level'] == 6:
    BMR = BMR * 1.9

#output
print('You need ', round(BMR), ' to keep you weight as it is')
print('You need ', round(BMR) - 500, ' to loose 0.5 kr per week')
print('You need ', round(BMR) - 1000, ' to loose 1 kr per week')
print('You need ', round(BMR) + 500, ' to gain 0.5 kr per week')
print('You need ', round(BMR) + 1000, ' to gain 1 kr per week')

