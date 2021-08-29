time = list(map(int,input().split(":")))

sun = time[0] - 8

 # 入力例2を行うために、if文が必要
 # 数値が「-」になった時の定義
if sun < 0:
    sun = 24 + sun

print(str(sun) + ":" + str(time[1]))


# 入力例1
# 5:25
# 出力例1
# 21:25
# 入力例2
# 12:59
# 出力例2
# 4:59