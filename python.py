r = [1, 2, 3, 4, 5, 1, 2, 3]
# print(r.index(3))
# 3を検索
# 出力結果 2 = インデックス番号2に3がある
print(r.index(3, 3))
 # (3, 3) = インデックス番号3から3を探す

print(r.count(3))
# 3の個数確認

if 5 in r:
    print("exist")
# 5があったら「exist」と出力

r.sort()
print(r)
# r配列を小さい順に並び替え

r.sort()
r.sort(reverse = True)
print(r)
# r配列を大きい順に並び替え

r.reverse()
print(r)
# 配列を元に戻す

s = "My name is Mike."
to_split = s.split(" ")
print(to_split)
# 出力結果 = ['My', 'name', 'is', 'Mike.']
# splitで配列に分ける

x = " ".join(to_split)
print(x)
# 出力結果 = My name is Mike.
# joinメソッド = 文字列の連結

print(help(list))
# メソッド一覧の確認