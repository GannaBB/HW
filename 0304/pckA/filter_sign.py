def filter_positive(n):

    l_positive = []

    for i in n:
        if i > 0:
            l_positive.append(i)
    
    yield l_positive

def filter_negativ(n):

    l_negative = []

    for i in n:
        if i < 0:
            l_negative.append(i)
    
    yield l_negative
