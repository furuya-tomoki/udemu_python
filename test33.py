a, b, R = map(int,input().split(" "))

for i in range(int(input())):
    xi, yi = map(int,input().split(" "))
    
    if ((xi - a) ** 2) + ((yi - b) ** 2) >= (R ** 2):
        print("silent")
    else:
        print("noisy")



# 入力例1
# 20 10 10
# 3
# 25 10
# 20 15
# 70 70
# 出力例1
# noisy
# noisy
# silent
# 入力例2
# 50 50 100
# 4
# 0 0
# 0 100
# 100 0
# 100 100
# 出力例2
# noisy
# noisy
# noisy
# noisy