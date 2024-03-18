#Да се състави програма, която изчислява сумата на произведенията от 1 до
#въведено едноцифрено число.
#Сумата се формира така:
#1*2 + 2*3*4 +..+n*(n+1)*(n+2)*..*2*n
#Вход: 4
#Изход: 7106

try:
    x = int(input('Enter maximum value: '))
except:
    print('Enter integer')

sum=0


for i in range(1,x+1):
    
    factor=1

    for j in range(i,2*i+1):
        factor=factor*j


    sum = sum+factor



print(sum)
