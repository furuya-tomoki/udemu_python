#  リストとは
# リストとは、まとまったデータを便利に扱うことができるデータ構造。
# インデックスと呼ばれる番号で、それぞれのデータを区別します。

# 他のプログラミング言語では「配列」と呼ばれる機能が、Pythonでは「リスト」という名前で提供されています。

#  リストの使いどころ
# 1.並び順管理が必要なデータ処理
# - 出席番号、座席順、パーティの並び順
# - トランプや将棋などのゲームデータ
# 2.Webフォームの選択肢
# - 年齢、都道府県など
# 3.エクセルのような複数行データ
# - CSVデータの処理

#  リストへの代入
# team = ["勇者", "魔法使い", 100, player_1]

# このチャプターで使用した関数
# リストの参照　要素の番号を指定する

# print(team[0]) 直接数値で指定する
# print(team[num]) 変数で指定する
# print(team[num + 1]) 計算式で指定する

# len関数　要素の数
# print(len(team))

# team = ["勇者", "魔法使い"]
# print(team)
# print(team[1])
# num = 0
# print(team[num + 1])
# print(len(team))

#  このチャプターで使用した関数
# append関数　リストの末尾に要素を追加
# team.append("戦士")

# リストの要素を上書き
# team[0] = "ドラゴン"

# リストの要素を削除
# team.pop(0)

# team = ["勇者", "魔法使い"]
# print(team)
# print(team[0])

# team.append("戦士")
# print(team)
# print(len(team))

# team[2] = "ドラゴン"
# print(team)
# print(len(team))

# team.pop(2)
# print(team)
# print(len(team))

#  ループでリストを扱う

# team = ["勇者", "戦士", "魔法使い", "盗賊"]
# for i in team:
# 	print(i)
	
# 	team = ["勇者", "戦士", "魔法使い"]

# print("<select name =''job'>")
# for job in team:
#     print("<option>" + job + "</option>")
# print("</select>")

#  このチャプターで使用した関数
# input関数 標準入力から1行読み込む


# line = input()



# rstrip関数 文字列の末尾の改行コードを取り除きます。

# line = input().rstrip()




# split関数 与えられたデータを指定の記号で分割し、リストとして戻す

# line = "勇者,戦士,魔法使い"
# print(line.split(","))

# 標準入力から読み込み
# input関数 標準入力から1行読み込む


# line = input()



# rstrip関数 文字列の末尾の改行コードを取り除きます。

# line = input().rstrip()


# sys.stdin.readlines関数 ファイルを全て読み込み、1行毎に処理

# import sys
# line = sys.stdin.readlines()



# import sys
#  複数行読み込むライブラリ
# array = []
# for line in sys.readlines():
#     array.append(line.rstrip())
    
# print(array)

# import sys
# for line in sys.stdin.readlines():
# 	# ここに、文字列を分割して、出力するコードを書く
# 	enemy = line.rstrip().split(",")
# 	print(enemy[0] + "が" + enemy[1] + "匹現れた")
# [スライム,30]の配列になっているので、[0],[1]としてすればOK


#  このチャプターで使用した関数
# randrange関数 ランダムな値を生成します。
# 引数を1つ指定した場合は、ゼロから引数以下の値をランダムに生成します


# import random
# line = input().rstrip().split(",")
# for enemy in line:
# 	print(enemy + "が現れた！")

# num = len(line)
# print("敵は" + str(num) + "匹")

# attack = random.randrange(num)

# print(line[attack] + "会心の一撃" + line[attack] + "倒した")

# # coding: utf-8
# # じゃんけんプログラム

# import random
# # 標準入力から1行取得
# line = input().rstrip()

# # カンマで分割して、リストに代入
# janken = line.rstrip().split(",")

# # リストの要素数を変数に代入
# num = len(janken)

# # リストの中身を出力
# print(janken)

# # ランダムに選んだリストの要素を出力
# print(janken[random.randrange(num)])


# import random
# line = input().rstrip()

# # 今回は自力で全部書いてみよう！

# # カンマで分割して、リストに代入
# omikuji = line.rstrip().split(",")
# # リストの要素数を変数に代入
# num = len(omikuji)
# # リストの中身を出力
# print(omikuji)
# # ランダムに選んだリストの要素を出力
# print(omikuji[random.randrange(num)])
