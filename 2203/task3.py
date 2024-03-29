# Да се създаде речник, който да съдържа информацията за дадено меню на
# ресторант. Ключовете му трябва да са стрингове, а стойностите цените. Програмата ще
# по иска от потребителя да въведе следната информация:
# - Ако потребителят въведе името на дадено ястие от менюто, тогава програмата
# да принтира цената и колко е общата цена до момента. След това да пита
# отново дали потребителят не иска да въведе нещо друго.
# - Ако потребителят въведе име на ястие, което не е в менюто, тогава програмата
# да изведе подходящо съобщение. След което отново програмата да пита
# потребителя да избере нещо друго от менюто.
# - Ако потребителят въведе празен стринг, тогава програмата да спре да подканва
# потребителя да избира от менюто и да изведе на екрана общата крайна сума.
# Пример:
# Order: sandwich
# sandwich costs 10, total is 10
# Order: tea
# tea costs 7, total is 17
# Order: elephant
# Sorry, we are fresh out of elephant today. Order: <enter>
# Your total is 17

#menu creation
menu={'sandwich': 10}
menu['burger'] = 9
menu['pizza'] = 30
menu['taco'] = 8
menu['fries'] = 5
menu['cola'] = 2
menu['water'] = 1
menu['beer'] = 4

#order calculation
user_order='sandwich'
price = 0
while user_order != '':
    user_order='sandwich'
    while user_order in menu:
        user_order = input('Order: ')
        if user_order == '':
            break 
        elif not user_order in menu:
            print('Sorry, we dont have this')
            break
        else:
            price += menu[user_order]
            print(user_order, ' costs ', menu[user_order], ', total is ', price)
              
    
     
print('Your total price: ', price)