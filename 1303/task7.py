#Да се състави програма, която да отгатне колко е студено/топло по
#въведената температура в градус Целзий. Температурните интервали са: 
#t <=-20 ледено студено; 
#t <=0 && t>-20 студено; 
#t <=15 && t>0 хладно; 
#t <=25 && t>15 топло; 
#t >25 горещо
#Входни данни: t - цяло число от интервала [-100..100].
#Пример: 12 Изход: хладно


try:

    temperature = int(input('Enter temperature in the range [-100:100]: '))

    if temperature<-100 or temperature>100:
        print('Enter valid value')
        exit()

    if temperature<=-20:
        print('Icy cold')
    elif temperature<=0:
        print('Cold')
    elif temperature<=15:
        print('Chilly')
    elif temperature<=25:
        print('Warm')
    else: 
        print('Hot')

except:
    print('Enter valid integer value')


