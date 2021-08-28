A = input()
B = input()


# 「0」で先頭の文字
# 「-1」で最後の文字

if A[-1] == B[0] and B[-1] != "n" :
    print("OK")
else:
    print("NG")
    
# A の最後の 1 文字が B の最初の 1 文字と一致している。
# B の最後の 1 文字が "n" ではない。


# 入力例1
# paiza
# application
# 出力例1
# NG
# 入力例2
# apple
# elephant
# 出力例2
# OK