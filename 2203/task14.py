# Даден е речник, съдържащ тримесечни стойности на продажбите за една
# година. Трябва да се напише програма, която да създава bar chart по зададеният речник.
# Ключовете на речника трябва да са: Q1, Q2, Q3, Q4. В графиката стойностите трябва да
# се показват в низходящ ред. Ако има стойности, които са равни те трябва да бъдат
# показани както са постъпи през годината.
# Вход: {"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0}
# Изход: Q1|###### 300
# Q4|##### 250
# Q2|### 150
# Q3|0
# Вход: {"Q4": 500, "Q3": 100, "Q2": 100, "Q1": 150}
# Изход: Q4|########## 500
# Q1|### 150
# Q2|## 100
# Q3|## 100



# data input

data = {}

for i in range(4):
    kkey = 'Q' + str (i+1)
    message = 'Enter sales for ' + kkey +': '
    try:
        num= int(input(message))
    except:
        print('Invalid input')
    data[kkey] = num

#sorting the sales

sales_list = []

for x in data:
    sales_list.append(data[x])

sales_list.sort(reverse = True)


for i in range(4):

    for x in data:
        if data[x] == sales_list[i]:
            n = sales_list[i]//50
            print(f"{x}{'|'}{'#'*n}{data[x]} ")
            data.pop(x)
            break
        

      

