from collections import Counter
 # リストの各要素の数え上げ
E = input().split("+")
 # 「+」区切りで出力
num = 0

for i in E:
     # for文でEの要素を取り出す
    c = dict(Counter(i))
     # dictで辞書へ変換
     # 単語の出現頻度をカウント
    num += c.get("<", 0) * 10 + c.get("/", 0)
     # getメソッドでキーから値を取得
     # 該当の値が無ければ第二引数を返す
print(num)

