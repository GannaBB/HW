# Да се промени задача 13 така, че да използва itertools.product.

import itertools




def result_prodcut(set1,set2):
    yield list(itertools.product(set1, set2))


    

set1 = [1,2,3,4,5]
set2 = [4,3,5,6]

print(next(result_prodcut(set1,set2)))