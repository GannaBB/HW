# Да се промени 6та задача така, че да използва итератор



try:
    l =  list(map(float,input('Enter your list separated by space: ').split()))   
except:
    print('Wrong input')


l_iter = iter(l)

l_positive = []
l_negative = []

while True:
    try:
        x = next(l_iter)
        if x > 0:
            l_positive.append(x)
        elif x < 0:
            l_negative.append(x)
    except StopIteration as e:
        break


print(l_positive)
print(l_negative)


