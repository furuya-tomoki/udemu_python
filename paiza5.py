# このチャプターで作成したコード

# # coding: utf-8
# # Your code here!

# # リストのおさらい
# enemyArray = ["スライム", "モンスター", "ドラゴン"]
# print(enemyArray)
# print(enemyArray[0])

# # 辞書の具体例
# enemyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
# print(enemyDictionary)
# print(enemyDictionary["中ボス"])

# level = "ラスボス"
# print(enemyDictionary[level])
# # print(enemyDictionary["敵"])




# # 辞書の基本操作
# enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
# print(enemies)
# print(enemies["中ボス"])
# print(len(enemies))

# enemies["ザコ2"] = "メタルモンスター"
# print(enemies)
# print(len(enemies))

# enemies["中ボス"] = "レッドドラゴン"
# print(enemies)
# print(len(enemies))

# del enemies["ザコ"]
# print(enemies)
# print(len(enemies))

# # 辞書をループで処理する

# # 辞書のおさらい
# enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
# print(enemies)
# print(enemies["中ボス"])

# for rank in enemies:
# 	print(enemies[rank] + "が、あらわれた！")
# for (rank, enemy) in enemies.items():
# 	print(rank + "の" + enemy + "が、あらわれた！")
	
	
# 	# 辞書をループで処理する

# # 辞書のおさらい
# enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
# print(enemies)
# print(enemies["中ボス"])

# for rank in enemies:
# 	print(enemies[rank] + "が、あらわれた！")
# for (rank, enemy) in enemies.items():
#      itemsメソッドを使用
# 	print(rank + "の" + enemy + "が、あらわれた！")
	
	
# skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# # この下で、辞書の値をループで出力してみよう
# for rank in skills:
#     print(skills[rank])
    
# 配列の中身
# 配列内に要素があり、キーと値がある
# ["~":"~","~":"~"]

# skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# # この下で、ハッシュの値をループで出力してみよう
# for (rank, skiil) in skills.items():
#     print(rank + "は" + str(skiil) + "です")
    
# points = {"国語" : 70, "算数" : 35, "英語" : 52}
# sum = 0
# # この下で、辞書の値の合計をループで計算してみよう
# for num in points:
#     sum += points[num]
# print(sum)


# weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
# print(weapons)

# print(sorted(weapons))
# アイウエオ順で出力
# print(sorted(weapons, reverse=True))
#  アイウエオ順の逆で出力
# weapons2 = ["4.イージスソード", "1.ウィンドスピア", "3.アースブレイカー", "2.イナズマハンマー"]
# print(sorted(weapons2))
#  数字順で表示

# weapons3 = ["バーニングソード", "風神スピア", "大地ブレイカー", "稲妻ハンマー"]
# print(sorted(weapons3))
# pcが判断する順番


# weapons = {"イージスソード":40, "ウィンドスピア":12, "アースブレイカー":99}
# print(sorted(weapons))
# print(weapons)
# print(sorted(weapons.items()))



# # 画像用辞書
# item_images = {
#     "剣":"http://paiza.jp/learning/images/sword.png",
#     "盾":"http://paiza.jp/learning/images/shield.png",
#     "回復薬":"http://paiza.jp/learning/images/potion.png",
#     "クリスタル":"http://paiza.jp/learning/images/crystal.png"
# }

# # アイテムの並び順配列
# item_orders = ["クリスタル", "回復薬", "盾", "剣", "回復薬", "回復薬"]

# # print(item_images)
# # print(item_orders)

# # アイテム名を取り出す
# for item_name in item_orders:
# # 画像ファイル名を取り出す
#     print("<img src='" + item_images[item_name] + "'>")
#     print(item_name + "<br>")