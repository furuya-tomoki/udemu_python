# 入力値
# 2000 #(残額) 5 #(乗車回数)
# 300 #以下(それぞれの区間運賃)
# 500
# 300
# 100
# 100

# 期待値
# 1700#(それぞれの区間で乗車した時のカード残額) 30　#（以下それぞれの区間を利用した時のポイント)
# 1200 80
# 900 110
# 900 10
# 800 20

money, n = map(int,input().split())
# money = 「2000（所持金）」 n = 「5（回数）」が代入されている
# map関数を使って1行目の値をそれぞれ変数に代入する
# int,input() = 数値型の標準入力
# split() = 文字列の分割

point = 0
# 予め所持ptを設定、デフォルト値は0


#for文でn(5回)回処理繰り返す
for i in range(n):
    #運賃を入力
    uc = int(input())
#以下の数値が代入(それぞれの区間運賃)
# 300 
# 500
# 300
# 100
# 100

    #もしも運賃よりも所持ptが大きかった場合にはptから運賃を差し引き
    #所持ptが運賃より不足している場合には所持金から運賃を差し引き、運賃の10%をptに加算
    if point >= uc:
        point -= uc
    # 110（所持ポイント）が100（運賃）より多いかったら、差し引く = 110-100=10 
    else:
        money = money - uc
        point += int(uc / 10)
    # 0（所持ポイント）が300（運賃）より少なかったら、2000（所持金）から300(運賃)を差し引き運賃の10%を加算
    print(money, point)
    
    
    num1, num2 = map(int,input().split())

if num1 >= 25 or num2 < 40:
    print("Yes")
else:
    print("No")
    
    
v = input().split()
N = int(v[0])
K = float(v[1])

total = 0
for _ in range(N):
    x = float(input())
    total += round(x * 10)

ans = int(total / round(K * 10))
if total % round(K * 10) != 0:
    ans += 1
print(ans)