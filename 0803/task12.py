age = 66
gender = 'm'
married = 'Y'
if gender=='f':
    print('can work only in the urban area')
else:
    if 20 < age < 40:
        print('can work anywhere')
    elif 40 <  age < 60:
        print('can  work only in the urban area')
    else:
        print('error')
