x=5
y=10
print('initial x =',x)
print('initial y =',y)
tmp=x
x=y
y=tmp
print('x after swap =',x)
print('y after swap =',y)

x, y = y, x
print(x,y)