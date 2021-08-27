day = 7
total = 0
list =[]

for _ in range(day):
    t = int(input())
    total += t
    list.append(t)
rainy = (total*30)/100
day = 0
for _ in list:
    if(_ <= rainy or _ <= 30):
        day += 1
print(day)