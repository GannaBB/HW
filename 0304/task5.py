# Да се принтира списък със всички функции от модула “re”, които съдържат
# думата “find”.

import re

text = 'find'
for x in dir(re):
    if text in x:
        print(x)

        