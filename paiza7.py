# 関数を作る

def say_hello():
    print("hello world")

say_hello()
say_hello()

 関数の定義方法
defを使って定義します。

def hello():
    print("hello world")


定義された関数は、それより下の位置から呼び出すことができます。
def hello():
    print("hello world")

hello()


関数の命名規則
関数の名前は、次のルールに従って付けます。
・1文字目：英語または、「_」(アンダーバー)
・2文字目以降：英語の大文字・小文字・数字「_」(アンダーバー)

例：
・ hello　 1文字目が、英小文字
・ _attack　 1文字目が、「_」(アンダーバー)
・ move01 2文字目以降に数字
・ move_left 2文字目以降「_」(アンダーバー)
・ moveLeft 2文字目以降に英大文字

慣習として、関数の先頭には大文字を使いません。
また、動詞を表す単語を使うと、コードがわかりやすくなります。


作成したコード

# 引数と戻り値を追加する

def sum(x, y):
    return x + y

num1 = sum(3, 4)
print(num1)
num2 = sum(300, 400)
print(num2)

 関数定義に引数と戻り値を追加する
引数と戻り値を追加します。

def sum(x, y):
    return x + y

num1 = sum(3, 4)
print(num1)


# 九九の表を作成してみよう

def multiply(x, y):
    return x * y
for step in range(1, 10):
  for num in range(1, 10):
    print(multiply(step, num), end="")
    if num < 9:
        print(", ", end="")
  print("")
  
  
  
  # スコープを理解する

message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    global message
     # グローバル変数を変更した場合のみ記載
     # global + 変数名
    message += "paiza"
    print(message + " " + str(a))
    return x + y

num = sum(a, b)
print(num)
print(message + " " + str(a))



スコープとは、変数の有効範囲が決まっていることです。
Pythonでは、関数定義の中と外ではローカル変数は分離しています。
同じ名前の変数があっても、独立しているので、それぞれ違う変数として扱われます。


グローバル変数
スコープがなく、関数定義を超えて利用できます。
ただし、どこで値が代入されたのか分かりにくくなるので、あまり奨励されません。



import random

def attack(enemy):
    print("勇者は、" + enemy + "を攻撃した。")
    hit = random.randint(1,10)
    if hit < 6:
        print(enemy + "に、" + str(hit) + "のダメージを与えた！")
    else:
        print("クリティカルヒット！" + enemy + "に、100のダメージを与えた！！")





enemies = ["スライム", "モンスター", "ドラゴン"]
for enemy in enemies:
    # print("勇者は、" + enemy + "を攻撃した。")
    attack(enemy)
    
    
作成したコード１（引数のデフォルト値）

# 引数のデフォルト値

def introduce(greeting, name = "村人"):
    print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者")
introduce("こんにちは")


 作成したコード２（可変長引数）

# 可変長引数

def introduce(greeting, *names):
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者", "村人", "兵士")


作成したコード３（可変長引数 - 辞書）

# 可変長引数 - 辞書

def introduce(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)

introduce(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします")


def battle(*enemies):
	for enemy in enemies:
		print("戦士は" + enemy + "と戦った")

battle("スライム", "モンスター", "ドラゴン")



引数のデフォルト値とは
関数定義のところで、引数にデフォルト値を指定できます。
引数呼び出しで、引数を省略した場合、このデフォルト値が適用されます。

# キーワード引数

def say_hello(greeting = "hello", target = "world"):
    print(greeting + " " + target)

say_hello()                      # hello world
say_hello("こんにちは", "皆さん")   # こんにちは 皆さん



# キーワード引数

def say_hello(greeting = "hello", target = "world"):
    print(greeting + " " + target)

say_hello()
say_hello("こんにちは", "皆さん")
say_hello("good morning!")
say_hello(greeting = "ネコ先生", target = "皆さん")
say_hello(target = "ネコ先生", greeting = "おはようございます")
say_hello(target = "ネコ先生")
say_hello(greeting = "おはようございます")