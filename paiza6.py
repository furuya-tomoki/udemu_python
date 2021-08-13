# 2次元リストとは
# 2次元リストとは、2つのインデックスで要素を指定するリストのこと。
# リストにリストを組み合わせて作成し、インデックスを2つ指定してデータを参照する。

# 多次元リストの用途
# - RPGのマップ
# - 写真・イラストなどのイメージ
# - 3D-CGの空間座標
# - ゲームの盤面
# - 表形式データ

# team_c = ["勇者", "戦士", "魔法使い"]
# team_d = ["盗賊", "忍者", "商人"]
# team_e = ["スライム", "ドラゴン", "魔王"]

# teams = [team_c, team_d, team_e]
# print(teams)

# print(teams[0])
# print(teams[0][0])
# print(teams[0][1])
# print(teams[0][2])


# # 2次元リストを作成する

# player = "忍者"
# team_a = [player, "戦士", "魔法使い"]
# print(team_a)
# print(team_a[1])

# team_b = [team_a[0], team_a[1], team_a[2]]
# print(team_b)
# print(team_b[0])

# team_c = ["勇者", "戦士", "魔法使い"]
# team_d = ["盗賊", "忍者", "商人"]
# team_e = ["スライム", "ドラゴン", "魔王"]

# teams = [team_c, team_d, team_e]
# print(teams)
# print(teams[1])
# print(teams[2][0])
# print(teams[2][1])
# print(teams[2][2])


# teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
# print(teams)
# print(teams[0])
# print(teams[0][0])
# print(teams[0][1])

# teams[0][1] = "魔導士"
# print(teams)
# print(len(teams))
# print(len(teams[0]))

# teams.append(["メタルモンスター", "シルバーモンスター", "ブラックモンスター"])
# teams[0].append("レッドドラゴン")

# del teams[1]
# del teams[0][1]



# teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
# print(teams)

# teams.append(["メタルモンスター", "シルバーモンスター", "ブラックモンスター"])
# print(teams)
# print(len(teams))

# teams[0].append("レッドドラゴン")
# print(teams)
# print(len(teams))
# print(len(teams[0]))

# del teams[1]
# print(teams)
# print(len(teams))

# del teams[0][1]
# print(teams)
# print(len(teams))
# print(len(teams[0]))


# team = ["勇者", "戦士", "魔法使い"]
# print(team)
# print(team[0])

# for (i, person) in enumerate(team):
#     print(str(i + 1) + "番目の" + person + "が、スライムと戦った")
    
    
#     numbers = [3, 1, 4, 1, 5]
# results = []
# for item in numbers:
#     results.append(item * 10)

# print(results)


# # ループでリストを処理する

# team = ["勇者", "戦士", "魔法使い"]
# print(team)
# print(team[0])

# for (i, person) in enumerate(team):
#     print(str(i + 1) + "番目の" + person + "が、スライムと戦った")

# numbers = [3, 1, 4, 1, 5]
# results = []
# for item in numbers:
#     results.append(item * 10)

# print(results)

# enemies = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"]
# # ここに、要素をループで表示するコードを記述する
# for (i, enemy) in enumerate(enemies):
#     print(str(i + 1) + "番目の" + enemy + "が現れた")


# # 各要素を3倍にして新しいリストを作成する

# numbers = [12, 34, 56, 78, 90]

# # ここに、各要素を3倍にして新しいリストを作成するコードを記述する
# numbers2 = []
# for num in numbers:
#     numbers2.append(num * 3)

# print(numbers2)



#  配列をforで作成
# numbers = [i * 2 for i in range(10)]
# print(numbers)



#  2次元配列をforで作成する
# numbers2 = [[1 for i in range(3)] for j in range(4)]
# print(numbers2)


# # 2次元リストをmapで作成する

# numbers = [i * 2 for i in range(10)]
# print(numbers)
# print(len(numbers))

# numbers2 = [[1 for i in range(3)] for j in range(4)]
# numbers2[0][1] = 2
# print(numbers2)


# ans = ["paiza" for i in range(5)]
# print(ans)



# num = [[7 for i in range(4)] for j in range(5)]
# print(num)


# # ドット絵を表示する

# enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#              [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
#              [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
#              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#              [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
#              [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]

# for line in enemy_img:
#     for dot in line:
#         if dot == 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
    
    
    
# letter_A = [[0,0,1,1,0,0],
#             [0,1,0,0,1,0],
#             [1,0,0,0,0,1],
#             [1,1,1,1,1,1],
#             [1,0,0,0,0,1],
#             [1,0,0,0,0,1]]

# # ここに、ドットを表示するコードを記述する
# for line in letter_A:
#     for dot in line:
#         if dot == 1:
#             print("@", end="")
#         else:
#             print(" ", end="")
            
#     print("")
#      forの位置にインデントを揃える
     
     
# 3次元配列
# カギかっこを3重にすると、3次元配列になる。


# enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
#               [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
#               [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],
#              [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
#               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]],
#              [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
#               [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]]]
              

#  3次元配列で、3つのドット絵を表示するループ

# for img in enemy_img:
#     for line in img:
#         for dot in line:
#             if dot == 1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
        
        

# # 3次元リストでドット絵を表示する

# enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
#               [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
#               [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],
#              [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
#               [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]],
#              [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
#               [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]],
#              [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
#               [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
#               [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
#               [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
#               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
#               [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
#               [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]]]

# for img in enemy_img:
#     # 配列を取り出す
#     for line in img
#      # 1行ずつ取り出す
#         for dot in line:
#             # 各行から1行ずつ取り出す
#             if dot == 1:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
        
        

# letters = [[[0,0,1,1,0,0],
#              [0,1,0,0,1,0],
#              [1,0,0,0,0,1],
#              [1,1,1,1,1,1],
#              [1,0,0,0,0,1],
#              [1,0,0,0,0,1]],
#             [[1,1,1,1,1,0],
#              [1,0,0,0,0,1],
#              [1,1,1,1,1,0],
#              [1,0,0,0,0,1],
#              [1,0,0,0,0,1],
#              [1,1,1,1,1,0]],
#             [[0,1,1,1,1,0],
#              [1,0,0,0,0,1],
#              [1,0,0,0,0,0],
#              [1,0,0,0,0,0],
#              [1,0,0,0,0,1],
#              [0,1,1,1,1,0]]]

# # ここに、ドットを表示するコードを記述する
# for img in letters:
#   for line in img:
#     for dot in line:
#         if dot == 1:
#             print("@", end="")
#         else:
#             print(" ", end="")
#     print()
#   print()
  
  
#   2次元配列で地図を作成・表示する

# landmap = [["森" for i in range(20)] for j in range(10)]
# for line in landmap:
#     for area in line:
#         print(area, end="")
#     print()
    
#  行番号を表示する

# for i,line in enumerate(landmap):
#     print(str(i) + ":", end="")
#     for area in line:
#         print(area, end="")
#     print()
    
# # coding: utf-8
# # Your code here!

# # 2次元リストで地図を表示する

# landmap = [["森" for i in range(20)] for j in range(10)]
# landmap[0][0] = "城"
# landmap[0][19] = "町"
# landmap[9][19] = "町"
# for i,line in enumerate(landmap):
#     print(str(i) + ":", end="")
#     for area in line:
#         print(area, end="")
#     print()
    
# text = ["吾輩は猫である",
#         "名前はまだ無い",
#         "どこで生まれたか",
#         "とんと見当がつかぬ"]

# #ここに、行番号を表示するコードを記述する
# for i,line in  enumerate(text):
#     print(str(i + 1) + ":" + line)


#  AND(論理積)について
# ANDは、両方の条件が成立した場合、全体の条件が成立します。
# 全てが不成立、どれか1つでも不成立の場合には、不成立となります。
# Pythonでは、「and」と記述します。


# 条件Ａ	条件Ｂ	全体
# 不成立	不成立	不成立
# 成立	不成立	不成立
# 不成立	成立	不成立
# 成立	成立	成立



#  OR(論理和)について
# ORは、どれか１つの条件が成立した場合、全体の条件が成立します。
# 全てが不成立の場合には、不成立となります。
# Pythonでは、「or」と記述します。


# 条件Ａ	条件Ｂ	全体
# 不成立	不成立	不成立
# 成立	不成立	成立
# 不成立	成立	成立
# 成立	成立	成立


#  2次元配列で地図を表示する

# landmap = [["森" for i in range(20)] for j in range(10)]
# for line in landmap:
#     for area in line:
#         print(area, end="")
#     print()
    
    
# 城と町を配置して、道でつなぐ
# 道は、行が2で割り切れるか、列が3で割り切れる場合で、そこが「森」の時に配置する。


# landmap = [["森" for i in range(20)] for j in range(10)]
# landmap[0][0] = "城"
# landmap[0][19] = "町"
# landmap[9][19] = "町"
# for i,line in enumerate(landmap):
#     print(str(i) + ":", end="")
#     for j,area in enumerate(line):
#         if (i % 2 == 0 or j % 3 == 0) and area == "森":
#             print("＋", end="")
#         else:
#             print(area, end="")
#     print()
    
    
# このチャプターで作成したコード

# # coding: utf-8
# # Your code here!

# # 2次元リストで地図を表示する

# landmap = [["森" for i in range(20)] for j in range(10)]
# landmap[0][0] = "城"
# landmap[0][19] = "町"
# landmap[9][19] = "町"
# for i,line in enumerate(landmap):
#     print(str(i) + ":", end="")
#     for j,area in enumerate(line):
#         if (i % 2 == 0 or j % 3 == 0) and area == "森":
#             print("＋", end="")
#         else:
#             print(area, end="")
#     print()
    
    
# landmap = [["森" for i in range(19)] for j in range(10)]
# landmap[2][9] = "城"
# landmap[0][0] = "町"
# landmap[0][18] = "町"
# landmap[9][0] = "町"
# landmap[9][18] = "町"

# # 地図に道を作る
# for i, line in enumerate(landmap):
#     for j, area in enumerate(line):
#         # ここから足りないところを入力してください
#         if (i % 9 == 0 or j % 9 == 0) and area == "森":
#             print("＋", end="")
#         else:
#             print(area, end="")
#     print()
 
 
#   標準入力するデータ

# 0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0
# 1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1
# 1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1
# 1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1
# 0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0
# 0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0
# 0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1
# _


# 標準入力から _ までの入力を読み込む

# while True:
#     line = input()
#     if line == "_":
#         break
#     print(line)


#  カンマで分割する

# while True:
#     line = input()
#     if line == "_":
#         break
#     print(line.split(","))
    
    
# 標準入力から読み込んだ2次元配列のドット絵を表示する

# enemy_img = []
# while True:
#     line = input()
#     if line == "_":
#         break
#     enemy_img.append(line.split(","))

# for line in enemy_img:
#     for dot in line:
#         if int(dot) == 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
    
    
# このチャプターで作成したコード

# # coding: utf-8
# # Your code here!

# # 標準入力から2次元リスト

# enemy_img = []
# while True:
#     line = input()
#     if line == "_":
#         break
#     enemy_img.append(line.split(","))

# # print(enemy_img)

# for line in enemy_img:
#     for dot in line:
#         if int(dot) == 1:
#             print("#", end="")
#         else:
#             print(" ", end="")
#     print()
    
    
    
# # coding: utf-8
# # Your code here!

# # 2次元リストで画像を配置

# # 画像用リスト
# players_img = [
#     "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png",
#     "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png",
#     "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png",
#     "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png",
#     "https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png"]

# # 配置データを読み込み
# team = []
# while True:
#     line = input()
#     if line == "_":
#         break
#     team.append(line.split(","))
# # print(team)

# # 配置に合わせて表示
# print("<table>")
# for line in team:
#     print("<tr>")
#     #print(line)
#     for person in line:
#         print("<td><img src='" + players_img[int(person)] + "'></td>")
#     print("</tr>")
# print("</table>")