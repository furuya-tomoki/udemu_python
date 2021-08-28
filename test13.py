n = int(input())
words = input().split()
 # 文字列代入
rule = n>=1 and n<=100 and len(words) == n 

nword = "";

if(rule):
     # Trueを定義
    for _ in words:
        # ブロック変数に＿にwordsを代入
        nword += _[0]
         # nwordに_[文字列の一文字目]を＋
    print(nword)
    
    
# 入力例1
# 4
# as soon as possible
# 出力例1
# asap
# 入力例2
# 3
# best friend forever
# 出力例2
# bff