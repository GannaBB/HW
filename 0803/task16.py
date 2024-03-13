Month = str( input('Enter a month : May, June, July, August, September or October.') )
days=int(input('Enter number of days: '))

if Month=='May' or 'October':
    studio_price=50*days
    appartment_price=65*days
    if 7<=days<14:
        price_studio=50*days*0.95
    if days>=14:
        price_studio=50*days*0.7
        appartment_price=65*days*0.9
elif Month=='June' or 'September':
    studio_price=75.2*days
    appartment_price=68.7*days
    if days>=14:
        studio_price=75.2*days*0.8
        appartment_price=68.7*days*0.9
else: 
    studio_price=76*days
    appartment_price=77*days
    if days>=14:
        appartment_price=68.7*days*0.9


print('Appartmet price:', f'{appartment_price:.2f}',"Lv")
print('Studio price:', f'{studio_price:.2f}',"Lv")