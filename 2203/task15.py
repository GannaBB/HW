# Google стартира мрежа от автономни дронове за доставка на пица и иска да
# създадете гъвкава система за награди (Pizza Points ™), която може да бъде настроена в
# бъдеще. Правилата са прости: ако клиент е направил поне N поръчки на най-малко Y
# цена, той получава БЕЗПЛАТНА пица!
# Създайте програма, която приема речник от клиенти, минимален брой поръчки и
# минимална цена на поръчката. Върнете списък с клиенти, които отговарят на условията
# за безплатна пица.
# Вход:
# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
# min_price = 20
# min_orders = 5
# Изход: ["Spider-Man"]
# Вход:
# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
# min_price = 10
# min_orders = 3
# Изход: ["Batman", "Spider-Man"]
# Вход:
# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
# min_price = 100
# min_orders = 5
# Изход: []


# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
# min_price = 20
# min_orders = 5

customers = {
 "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
 "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
}
min_price = 100
min_orders = 5

# customers = {
#  "Batman": [22, 30, 11, 17, 15, 52, 27, 12],
#  "Spider-Man": [5, 17, 30, 33, 40, 22, 26, 10, 11, 45]
# }
# min_price = 10
# min_orders = 3

winners = []

for x in customers:
    new_list = []
    for y in customers[x]:
        if y >= min_price:
            new_list.append(y)
    if len(new_list) >= min_orders:
        winners.append(x)

print(winners)

