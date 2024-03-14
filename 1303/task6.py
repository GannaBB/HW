#Високосни години са всички години кратни на 4 с изключения столетията, но без столетия кратни на 400, т.е. 1900 не е високосна, но 1600 и 2000 са високосни.
#Съставете програма, която по въведена година проверява дали тя е високосна
#Входни данни: число за година в инетервала [0-9999].
#Пример: 2024 Изход: 2024та е високосна


try:

    year=int(input('Enter year: '))

    if year<0 or year>9999:
        print('Enter valid year in rane[0:9999]')
        exit()

    if not year%4:
        if year%100:
            print(year, 'е високосна')
        else:
            if year%400:
                print(year, 'не е високосна')
            else:
                print(year, 'е високосна')
                


    else:
        print(year, 'не е високосна')
        

except:
    print('Enter valid year')