xc, yc, r1, r2 = map(int,input().split(" "))

for i in range(int(input())):
    x1, x2 = map(int,input().split(" "))
    if r1 ** 2 <= (x1 - xc) ** 2 + (x2 - yc) ** 2 and (x1 - xc) ** 2 + (x2 - yc) ** 2 <= r2 ** 2:
        print("yes")
    else:
        print("no")
        
        
# 入力例1
# 0 0 1 2
# 3
# 0 0
# 1 1
# 4 2
# 出力例1
# no
# yes
# no
# 入力例2
# 47 19 57 80
# 3
# 62 -52
# 35 -70
# -81 2
# 出力例2
# yes
# no
# no