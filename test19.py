S = str(input())
 # 文字列を代入
H = int(input())
 # 数値型を代入
daruma = S[:H-1]+S[H:]
 # 「p」+「iza」で結果が出力される

print(daruma)


# 入力例1
# paiza
# 2
# 出力例1
# piza
# 入力例2
# water
# 5
# 出力例2
# wate