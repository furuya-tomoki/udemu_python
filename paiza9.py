#  ＃02:クラスを継承する 
# ここでは、クラスの継承ついて学習します。例として、RPGで使うアイテムが入る宝箱クラスを作り、そこから宝石箱クラスを継承で作ってみましょう

# class Box:
#     def __init__(self, item):
#         self.item = item

#     def open(self):
#         print("宝箱を開いた。" + self.item + "を手に入れた。")

# class JewelryBox(Box):
#     def look(self):
#         print("宝箱はキラキラと輝いている。")

# box = Box("鋼鉄の剣")
# box.open()

# jewelrybox = JewelryBox("魔法の指輪")
# jewelrybox.look()
# jewelrybox.open()


# class Greeting:
#     def __init__(self):
#         self.msg = "hello"
#         self.target = "paiza"

# class Hello(Greeting):
#     # この下に、say_helloメソッドを記述する
#     def say_hello(self):
#         print(self.msg + " " + self.target)
    
# player = Hello()
# player.say_hello()



# メソッドのオーバーライドとは
# オーバーライドを利用すると、スーパークラスが持つメソッドを、サブクラスで書き換えて再定義することができます。


# class Box:
#     def __init__(self, item):
#         self.item = item

#     def open(self):
#         print("宝箱を開いた。" + self.item + "を手に入れた。")

# class MagicBox(Box):
#     def look(self):
#         print("宝箱は、妖しく輝いている。")

#     def open(self):
#         print("宝箱を開いた。" + self.item + "が襲ってきた！")

# box = Box("鋼鉄の剣")
# box.open()

# magicbox = MagicBox("モノマネモンスター")
# magicbox.look()
# magicbox.open()


# class Greeting:
#     def __init__(self):
#         self.msg = "hello"
#         self.target = "paiza"

#     def say_hello(self):
#         print(self.msg + " " + self.target)

# class Hello(Greeting):
#     # ここにオーバライドするメソッドを記述する
#     def say_hello(self, target):
#         print(self.msg + " " + target)
#          # 「self.target」だと「python」が入る場所がないので「target」で定義する


# player = Hello()
# player.say_hello("python")


# # メソッドをオーバーライドしよう2

# class Greeting:
#     def __init__(self):
#         self.msg = "hello"
#         self.target = "paiza"
    
#     def say_hello(self):
#         print(self.msg + " " + self.target)

# class Hello(Greeting):
#     def say_hello(self):
#         print(self.msg + " " + self.target)
#         print("YEAH YEAH YEAH!")


# player = Hello()
#  # 「Greeting」から「Hello」に変更するだけで、出力結果も変わる
# player.say_hello()



# class Player:
#     def __init__(self, name):
#         self.name = name

#     def attack(self, enemy):
#         print(self.name + "は、" + enemy + "を攻撃した！")

# print("=== パーティーでスライムと戦う ===")
# hero = Player("勇者")
# # hero.attack("スライム")
# warrior = Player("戦士")

# party = [hero, warrior]
# for member in party:
#     member.attack("スライム")
    
    
    
# class Player:
#     def __init__(self, name):
#         self.name = name

#     def attack(self, enemy):
#         print(self.name + "は、" + enemy + "を攻撃した！")

# class Wizard(Player):
#     def attack(self, enemy):
#         print("ズバーン！")
#         print(self.name + "は、" + enemy + "に炎を放った！")

# print("=== パーティーでスライムと戦う ===")
# hero = Player("勇者")
# # hero.attack("スライム")
# warrior = Player("戦士")
# wizard = Wizard("魔法使い")

# party = [hero, warrior, wizard]
# for member in party:
#     member.attack("スライム")
    
    
# # coding: utf-8
# # RPGの攻撃シーン

# class Player:
#     def __init__(self, name):
#         self.name = name

#     def attack(self, enemy):
#         print(self.name + "は" + enemy + "を攻撃した")

# class Warrior(Player):
#     def attack(self, enemy):
#         print(self.name + "は" + enemy + "を猛攻撃した")


# team = []
# team.append(Player("勇者"))
# team.append(Player("魔法使い"))
# team.append(Warrior("戦士"))

# for person in team:
#     person.attack("スライム")



# class Player:
#     def __init__(self, name):
#         self.name = name

#     def attack(self, enemy):
#         print(self.name + "は、" + enemy + "を攻撃した！")

# class Wizard(Player):
#     def __init__(self):
#         super().__init__("魔法使い")

#     def attack(self, enemy):
#         self.__spell()
#         print(self.name + "は、" + enemy + "に炎を放った！")

#     def __spell(self):
#         print("ズバーン！")

# print("=== パーティーでスライムと戦う ===")
# hero = Player("勇者")
# # hero.attack("スライム")
# warrior = Player("戦士")
# wizard = Wizard()

# party = [hero, warrior, wizard]
# for member in party:
#     member.attack("スライム")

# # wizard.__spell()



#  Player.charactor_count += 1

# Player.charactor_count = Player.charactor_count + 1

# を、省略する記法です。「-=」「/=」なども使用できます。


# クラス変数
# オブジェクト間で共通して利用できる変数のこと。


# クラスメソッド
# オブジェクト間で共通して利用できるメソッドのこと。
# 動画では、2つの方法でクラスメソッドを作成しましたが、デコレータを使用する方法が推奨されています。



#  デコレータ
# すでに定義されている関数に、新たに機能を追加できる仕組みのこと。
# デコレータは、すでに用意されていたり、自分で作成したりすることができます。

# 動画では、@classmethodを使用しました。


# @classmethod
# def summary(cls):
#     print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")
    
    
#     def summary(cls):
#     print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

# summary = classmethod(summary)



# from datetime import datetime, timedelta, timezone

# jst   = timezone(timedelta(hours=9))
# today = datetime.now(jst)
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

# day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
# print(day)