s = list(map(int,input().split(" ")))
h = "ABCDEFGHIJ"

print(h[:s[0]])
 # 先頭からの範囲を指定
print(h[s[0]:(s[0] + s[1])])
 # 真ん中の範囲指定
print(h[(s[0] + s[1]):])
 # 最後から数値を範囲


# 入力例1
# 2 3 5
# 出力例1
# AB
# CDE
# FGHIJ
# 入力例2
# 1 1 8
# 出力例2
# A
# B
# CDEFGHIJ
# 入力例3
# 3 4 3
# 出力例3
# ABC
# DEFG