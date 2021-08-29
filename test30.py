# coding: utf-8
# Your code here!
m = input().split(" ")
 # 「11 1」が代入
M = m[0] + m[1]
 # 文字列として「11 + 1」 = 111

if len(M) == M.count(m[0][0]):
 # len(M) = 「111」なので長さは「3」
 # M.count(m[0][0]) = 「111」の「1」を指定 = 1が「3個」
     print("Yes")
else:
     print("No")


# 入力例1
# 11 1
# 出力例1
# Yes
# 入力例2
# 12 11
# 出力例2
# No