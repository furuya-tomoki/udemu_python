# for inの基本形

#  coding: utf-8
#  for inによるループ処理

# for カウンタ変数 in 繰り返す範囲:
#     繰り返し処理
    
#      range関数
# 繰り返しの回数を指定する

# range(10) 0から9まで、10回繰り返す
# range(6, 11) 6から10まで繰り返す

#  coding: utf-8
#  for inによるループ処理
# for i in range(6, 11):
#     print("hello" + str(i))
# print("last" + str(i))

#  whileの基本形

#  coding: utf-8
#  whileによるループ処理

# カウンタ変数を初期化
# while 条件式:
#     繰り返し処理
#     カウンタ変数を更新
    
#      str関数
# 数値データをテキストデータに変換する

#  coding: utf-8
#  whileによるループ処理
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
#     print("next" + str(i))
    
# print("last" + str(i))

#  whileの基本形

#  coding: utf-8
#  whileによるループ処理

# カウンタ変数を初期化
# while 条件式:
#       繰り返し処理
#       カウンタ変数を更新
      
#       str関数
# 数値データをテキストデータに変換する

# 代入演算子
# 演算子	使用例	意味	別の書き方
# +=	a += 1	a変数の値を1増加させる。	a = a + 1と同じ
# -=	a -= 1	a変数の値を1減少させる。	a = a - 1と同じ

#  coding: utf-8
#  whileによるループ処理

# import random 
# hp = 30
# while hp > 0:
#     hit = random.randint(1,10)
#     print("スライムに" + str(hit) + "のダメージを与えた")
#     hp -= hit
# print("倒した")

#  for inの基本形

#  coding: utf-8
#  for inによるループ処理

# for カウンタ変数 in 繰り返す範囲:
#     繰り返し処理
    
#      str関数
# 数値データをテキストデータに変換する

#  range関数
# 繰り返しの回数を指定する

# range(10) 0から9まで、10回繰り返す
# range(6, 11) 6から10まで繰り返す

#  プルダウン表示の基本形

# <select name='age'>
#   <option>1才</option>
#   <option>2才</option>
#   <option>3才</option>
# </select>

#  coding: utf-8
#  年齢入力のプルダウン作成
# print("<select name=\'age\'>")
# for age in range(100):
#     print("<option>" + str(age + 1) + "歳</option>")
# print("</select>")

# 標準入力とは
# もともとはLINUXなどのUnix系OSで用意されていた仕組みです。
# 標準入力に対応するようにプログラムを作っておけば、プログラム実行時に、ファイルを読み込んだり、キーボードからデータを読み込んだり、パラメータを指定したりというように、入力先を切り替えることができます。

# input()
# 標準入力から1行読み込む


# line = input()

#  coding: utf-8
#  inputによる入力処理
# line = int(input())
# print(line * 10)


#  複数行読み込みの基本形

#  coding: utf-8
#  標準入力とループ処理
# count = int(input())
# print("データ個数 " + str(count))
# for i in range(count):
#     line = input().rstrip()
#     print("hello " + line)


#  複数行読み込みの基本形

#  coding: utf-8
#  標準入力とループ処理
# count = int(input())
# print("データ個数 " + str(count))
# for i in range(count):
#     line = input().rstrip()
#     print("hello " + line)
    
#      rstrip()
# データの行末の改行を削除する。
# 改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しています。インプットの後に、ドットに続けて記述することで、インプットの戻り値の改行を削除することができます。


# line = input().rstrip()


# count = int(input())
# print("データ個数 " + str(count))
# for i in range(count):
#     line = input().rstrip()
#     print("hello " + line)
    
# num1 = int(input())
# num2 = int(input())

# for i in range(num1, num2 + 1):
#     print(i)
    
#  for inの基本形

#  coding: utf-8
#  for inによるループ処理

# for カウンタ変数 in 繰り返す範囲:
#     繰り返し処理
    
#      西暦年／平成年の計算方法
# 平成年から西暦年を求めるには、平成年に「1988」を足します


# 西暦年 = 平成年 + 1988


# 例)
# 平成1年に「1988」を足すと、1989 > 平成1年は1989年。
# 平成2年に「1988」を足すと、1990 > 平成2年は1990年。
# 平成3年に「1988」を足すと、1990 > 平成3年は1991年。


# 西暦年から平成年を求めるには、これとは逆に、西暦年から「1988」を引きます。

# 平成年 = 西暦年 - 1988


# 例)
# 西暦1989年から「1988」を引くと、1 > 1989年は平成1年。
# 西暦1990年から「1988」を引くと、2 > 1990年は平成2年。
# 西暦1991年から「1988」を引くと、3 > 1991年は平成3年。

#  西暦年と平成年の対応表を作る
#  1989年から2016年までをループで出力
#  ループ内で、各西暦年を平成年に変換
# for seireki in range(1989, 2017):
#     print("西暦" + str(seireki) + "年は、", end="" )
#     heisei = seireki - 1989
#     print("平成" + str(heisei) + "年です。")
    
    
#     for seireki in range(num1, num1 + num2):
#     print("西暦" + str(seireki) + "年は",end="")
#     showa = seireki - 1925
#     print("昭和" + str(showa) + "年です")