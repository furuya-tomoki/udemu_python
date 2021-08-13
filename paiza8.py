オブジェクトとは
変数とメソッドをセットにしたもの。クラスからオブジェクトを作って利用する。

クラス: オブジェクトの設計図
オブジェクト: クラスから作成したもの


 今回作成したコード

# coding: utf-8
# クラスを作成する

class Player:
    def walk(self):
        print("勇者は荒野を歩いていた")

    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

player1 = Player()
player1.walk()
player1.attack("スライム")


class Greeting:
    def say_hello(self):
         # selfを記述すること
        print("hello paiza")

# この下に、必要なコードを追加してください
Greeting1 = Greeting()
 # 定義してから出力
Greeting1.say_hello()



# 変数をクラスで管理する

class Player:
    def __init__(self, job):
        self.job = job

    def walk(self):
        print(self.job + "は荒野を歩いていた")

player1 = Player("戦士")
player1.walk()


 インスタンス変数とは
インスタンス変数は、インスタンスが持つ変数です。
インスタンス変数は、インスタンスがある限りデータが保持されます。


# クラスにインスタンス変数を追加しよう

class Greeting:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello " + self.name)

paiza = Greeting("paiza")
paiza.say_hello()


class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(self.name + "は勇者を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:
    enemy.attack()
    
    
class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

team = []
team.append(Player("勇者"))
team.append(Player("戦士"))
team.append(Player("魔法使い"))

for player in team:
    player.attack("スライム")


 クラス変数とは
クラス変数を宣言したクラスのインスタンス全てで共有して利用できる変数。


商品ごとに単価と個数を保持して、合計金額を計算する

# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class Item:
    tax = 1.08

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return int(self.price * self.quantity * Item.tax)

apple = Item(120, 15)
total = apple.total()
print("合計金額は" + str(total) + "円です")

orange = Item(85, 32)
print("合計金額は" + str(orange.total()) + "円です")


小数を整数にする処理
今回は、int関数を用いて、小数点以下を切り捨てました。
切り捨て以外にも、mathモジュールを用いると、様々な方法で、小数から整数に変換できます。

例えば、trunc(x)は、int関数と同様に、xの小数部分を削除します。
ceil(x)は、x以上の最小の整数を返します。天井関数と呼ばれています。
floor(x)は、x以下の最大の整数を返します。床関数と呼ばれています。
round(x)は、端数が0.5より大きいならは切り上げ、端数が0.5より小さいなら切り捨てた整数を返します。
ただし、端数がちょうど0.5の場合、切り捨てと切り上げのうち、結果が偶数になる整数を返します。
一般的な四捨五入と異なる動作をするので注意が必要です。


class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    def sum(self):
        return str(self.kokugo + self.sansu)

# この下に、必要な処理を記述します
yamada = Gakusei(70, 43)
sum = yamada.sum()
print("合計は" + str(sum) +  "点です")


text = "pYthon"
print(text)
print(text.capitalize())
print(text.upper())

players = "勇者,戦士,魔法使い,忍者"
list = players.split(",")
print(list)
list.remove("忍者")
print(list)
list.append("霧島")
print(list)


# 文字列に対してメソッドを実行する

msg = input()
# この下に、msgが全て小文字かどうかを表示する処理を記述する
print(msg.islower())


team = ["勇者", "戦士", "魔法使い", "忍者"]
# この下に、インデックス3に「盗賊」を追加して、リストを表示する処理を記述する

team.insert(3, "盗賊")
print(team)


# coding: utf-8
# アクセス制限を理解する

class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")

    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player("戦士", "剣")
player1.walk()
# player1.__attack("スライム")
# print(player1.__weapon)



# アクセス制限を理解する

class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")
        self.__attack("スライム")

    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")


player1 = Player("戦士", "剣")
player1.walk()
# player1.__attack("スライム")
# print(player1.__weapon)