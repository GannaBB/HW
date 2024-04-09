def simple(n):

    i = 1

    while i <= n:
        k = 1
        for y in range(2,i):
            if i%y==0:
                k = 0
                break
        
        if k == 1:
            yield i
        
        i += 1

