#Напишете програма, която за дадено цяло число n, пресмята сумата
# S=1 + 1!/x+2!/x^2+   + n!/x^n


try:
    n = int(input('Enter integer n: '))
except:
    print('n must be integer')

try:
    x = float(input('Enter x: '))
except:
    print('Invalid input')


sum = 1

for i in range(n):
    
    term =1
    
    for j in range(i+1):
        term = term*(j+1)/x
    
    sum = sum + term

print('Result: ', sum)
        
