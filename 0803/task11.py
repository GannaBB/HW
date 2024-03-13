a = 17
b = 15
c = 20
if a<=b<=c:
    print('median from', a,',',b,',',c,'is', b)
elif b<=a<c:
    print('median from', a,',',b,',',c,'is', a)
else: 
    print('median from', a,',',b,',',c,'is', c)