
def geometric_progression(a1,n,d):
    i = 1
    an_list = []
    while i <= n:
        an = a1 * (d ** (i-1))
        an_list.append(an)
        i += 1
    
    yield an_list