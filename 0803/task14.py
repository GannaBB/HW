a = 68
b = 90
c = 30

if a>b:
    if a<c:
        print(c,a,b)
    elif b<c:
        print(a,c,b)
    else:
        print(a,b,c)
else:
    if b<c:
        print(c,b,a)
    elif a>c:
        print(b,a,c)
    else:
        print(b,c,a)


    
