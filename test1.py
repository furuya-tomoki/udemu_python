# 1. 通常は購入金額の 1 ％（小数点以下切り捨て）とする
# 2. ただし、3 のつく日は購入金額の 3 ％（小数点以下切り捨て）とする
# 3. ただし、5 のつく日は購入金額の 5 ％（小数点以下切り捨て）とする


import math
cnt = int(input())

point = 0
for i in range(cnt):
    y, money = map(int,input().split())
    if y == 3 or y == 13 or y == 23 or y == 30 or y == 31:
        point += math.floor(money * 0.03)
    elif y == 5 or y == 15 or y == 25:
        point += math.floor(money * 0.05)
    else:
        point += math.floor(money * 0.01)
print(point)

# 絶対値の求め方
x = int(input())
y = abs(x)
print(y)