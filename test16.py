word = input()
 # word変数にRRRWWを代入
num = int(input())
 # num変数に3を代入
point = int(word.count("R"))
 # point変数にRの個数を代入

if point >= num:
    print("Yes")
else:
    print("No")


# 入力例1
# RRRWW
# 3
# 出力例1
# Yes
# 入力例2
# RRWRW
# 4
# 出力例2
# No