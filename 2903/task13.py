# Да се реализира декартово произведение на две множества, като се използва
# съкратен запис за създаването на списъкът с крайните елементи.


# for numbers:

# set1 = [1,2,3,4,5]
# set2 = [4,3,5,6]

# def set_product(x,y):
#     product = []
#     for i in x:
#         for j in y:
#             product.append(i*j)

#     yield product

# print(next(set_product(set1,set2)))

#general

set1 = [1,2,'A',4,5]
set2 = [4,3,5,6]

def set_product(x,y):
    product = []
    for i in x:
        for j in y:
            t = (i,j)
            product.append(t)

    yield product

print(next(set_product(set1,set2)))