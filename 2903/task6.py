# Да се напише програма, която от даден списък да прехвърля положителните
# числа в един списък и отрицателните в друг. 



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



try:
    l =  list(map(float,input('Enter your list separated by space: ').split()))   
except:
    print('Wrong input')

print(next(filter_negativ(l)))
print(next(filter_positive(l)))

