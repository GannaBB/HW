n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
operator = str(input('Enter operator (събиране (+), изваждане (-), умножение (*), деление (/) и модулно деление (%).): '))

if operator !='/' and operator != '%':
    if 2:
        if operator =='+':
            result = n1+n2
        elif operator == '-':
            result = n1-n2
        elif operator == '*':
            result = n1*n2
    if result % 2:
        print(n1,operator,n2,'=', result, ' нечетное')
    else:
        print(n1,operator,n2,'=', result, ' четное')
elif operator =='/' and n2!=0:
    result1 = n1/n2
    print(n1,operator,n2,'=', result1)
elif operator=='%' and n2!=0:
    result = n1%n2
    print(n1,operator,n2,'=', result)
else:
    print('You can not divide by 0')
