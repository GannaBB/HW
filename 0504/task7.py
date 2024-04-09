# Да се напише програма, която да сортира списък от речници използвайки
# Lambda.

list = [
    {'name': 'Ada', 'age': 25, 'city': 'Paris'},
    {'name': 'Nick', 'age': 21, 'city': 'London'},
    {'name': 'Leo', 'age': 30, 'city': 'Berlin'},
    {'name': 'Kris', 'age': 20, 'city': 'Milano'},
    {'name': 'Pete', 'age': 41, 'city': 'Sofia'},
]

print(f'Original list: \n{list}')

new_list = sorted(list, key=lambda x: x['age'])
print(f'Ordered by age: \n{new_list}')

new_list = sorted(list, key=lambda x: x['city'])
print(f'Ordered by city: \n{new_list}')

new_list = sorted(list, key=lambda x: x['name'])
print(f'Ordered by name: \n{new_list}')
