import math
d = int(input())
day = math.sqrt(d)
if day % 2 == 0:
    print("OK")
else:
    print("NG")


# 入力例1
# 256
# 出力例1
# OK
# 入力例2
# 255
# 出力例2
# NG