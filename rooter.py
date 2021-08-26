import math
# 数学的な計算をする標準モジュール
cnt = int(input())

point = 0
# ポイントカードの初期値を設定
for i in range(cnt):
     # cnt回数繰り返す
     # range 関数は引数に指定した数値を要素として持つ
    y, money = map(int,input().split())
     # y = 日付
     # money = 購入金額
     # 配列などの各要素に関数を順番に適用することができます。
     # 使い方は map(適用したい関数, 配列1, ) です。
     
    if y == 3 or y == 13 or y == 23 or y == 30 or y == 31:
        # 日付3のつく日なら下記の処理を行う
        point += math.floor(money * 0.03)
    elif y == 5 or y == 15 or y == 25:
        # 日付5のつく日なら下記の処理を行う
        #math.floor = 四捨五入
        point += math.floor(money * 0.05)
    else:
        # それ以外
        point += math.floor(money * 0.01)
        
print(point)


# 入力例1
# 3
# 1 1024
# 11 2048
# 21 4196
# 出力例1
# 71
# 入力例2
# 1
# 30 340
# 出力例2
# 10
# 入力例3
# 2
# 5 10000
# 12 10000
# 出力例3
# 600