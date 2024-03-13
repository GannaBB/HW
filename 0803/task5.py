a =1
b =2
c =1
print('Quadratic equation ', a,'*x^2+',b,'x+',c)
D = b**2-4*a*c
print(D)
if D<0:
    print('no real solutions')
elif D==0:
    x = -b/(2*a)
    print('one solution =', x)
else:
    x1 = (-b+D**(0.5))/(2*a)
    x2 = (-b-D**(0.5))/(2*a)
    print('solutions are', x1, 'and', x2)
