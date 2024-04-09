# Да се организират всички функции, които реализират генератори (от
# предишната лекция) в един пакет и след това да се използват в скрипт под име
# main.py.


import pckA.even_numbers

test = pckA.even_numbers.even(10)

for i in test:
    print(i)