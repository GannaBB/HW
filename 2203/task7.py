# Да се напише програма, която да симулира 1000 завъртания на два зара (от 6
# числа). Програмата да съдържа два речника, единият да е с очакваните вероятности, а
# другият ще пази броят на числата, които са се паднали.


import random

# define expected %
res_expected = {2:2.68, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}

#simulated values
simulation= {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
for i in range(1000):
    dice = random.randint(1,6) + random.randint(1,6)
    simulation[dice] += 1

res_simulated = {}
for a in simulation:
    res_simulated[a] = simulation[a]/10

print(f"{'Total':^10}{'Simulated %':^20}{'Expected %':^20}")

for a in simulation:
    print(f"{a:^10}{res_simulated[a]:^20}{res_expected[a]:^20}")




