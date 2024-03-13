VIP_price = 499.99
NORMAL_price=249.99

budget = int(input("Enter your budget: "))
category=str(input('Enter preferred ticket class: VIP or NORMAL: '))
number_people=int(input('Enter number of people:'))

if 1<=number_people<5:
    transportation=budget*0.75
    left_budget=budget*0.25
    if category=='VIP':
        tickets=VIP_price*number_people
    else:
        tickets=NORMAL_price*number_people
    total= transportation+tickets
    delta=budget-total
    if total>budget:
        print('Not enough money. You need',f'{-delta:.2f}', 'Lv' )
    else:
        print('Yes, you have', f'{delta:.2f}', 'Lv left')
elif 4<number_people<10:
    transportation=budget*0.60
    left_budget=budget*0.40
    if category=='VIP':
        tickets=VIP_price*number_people
    else:
        tickets=NORMAL_price*number_people
    total= transportation+tickets
    delta=budget-total
    if total>budget:
        print('Not enough money. You need',f'{-delta:.2f}', 'Lv' )
    else:
        print('Yes, you have', f'{delta:.2f}', 'Lv left')
elif 9<number_people<25:
    transportation=budget*0.5
    left_budget=budget*0.5
    if category=='VIP':
        tickets=VIP_price*number_people
    else:
        tickets=NORMAL_price*number_people
    total= transportation+tickets
    delta=budget-total
    if total>budget:
        print('Not enough money. You need',f'{-delta:.2f}', 'Lv' )
    else:
        print('Yes, you have', f'{delta:.2f}', 'Lv left')
elif 24<number_people<50:
    transportation=budget*0.4
    left_budget=budget*0.6
    if category=='VIP':
        tickets=VIP_price*number_people
    else:
        tickets=NORMAL_price*number_people
    total= transportation+tickets
    delta=budget-total
    if total>budget:
        print('Not enough money. You need',f'{-delta:.2f}', 'Lv' )
    else:
        print('Yes, you have', f'{delta:.2f}', 'Lv left')
else:
    transportation=budget*0.25
    left_budget=budget*0.275
    if category=='VIP':
        tickets=VIP_price*number_people
    else:
        tickets=NORMAL_price*number_people
    total= transportation+tickets
    delta=budget-total
    if total>budget:
        print('Not enough money. You need',f'{-delta:.2f}', 'Lv' )
    else:
        print('Yes, you have', f'{delta:.2f}', 'Lv left')
