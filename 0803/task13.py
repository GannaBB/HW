x = 5463

a = x//1000
b = x%1000//100
c = 5463%100//10
d = 5463%10

y = a + b*10 + c*100 + d*1000

print('Input:', x)
print('Output:', y)