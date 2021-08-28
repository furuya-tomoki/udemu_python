pas = input()

A = len(pas)
 # 要素の長さ
B = pas.count(pas[0])
 # 要素の先頭の文字

if A == B:
     # 長さと先頭の文字との比較
    print("NG")
else:
    print("OK")


# 入力例1
# AAAAAAAA
# 出力例1
# NG
# 入力例2
# Paiza
# 出力例2
# OK