例外処理の概要を理解しよう

print("start")
a = 1
print(b)
print("end")



print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print(e)
finally:
    print(2)
    
    
    
    
import traceback, sys

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    # print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)



# coding: utf-8
# 例外メッセージを指定しよう
import sys
enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[2 / number] + "と戦った")
except ZeroDivisionError as e:
    sys.stderr.write("その敵は表示できません")
finally:
    print("勇者は勝利した")



print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
finally:
    print(2)
    
    
    
    
import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number1 = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[number2] + "と戦った")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
finally:
    print("勇者は勝利した")



print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
finally:
    print(2)
    
    
# coding: utf-8
# 例外の種類を変更しよう その２

import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number1 = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[number2] + "と戦った")
except ZeroDivisionError as e:
    sys.stderr.write("その敵は表示できません")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")

finally:
    print("勇者は勝利した")



# coding: utf-8
# 間違い探し

import sys

print("Hello World")

try:
    raise ZeroDivisionError("強制エラー")
except NameError as e:
    sys.stderr.write("未定義の変数を呼び出しています")
except ZeroDivisionError as e:
    sys.stderr.write("0では割り算はできません")

finally:
    print("Hello Python3")




def test_exception(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        raise e
    print(6)

print(1)
try:
    answer = test_exception(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)



import sys

def calc():
    return 100 / 0


try:
    print(calc())
except ZeroDivisionError as e:
    sys.stderr.write("0で割り算はできません")
    
    
    
# coding: utf-8
# 呼び出し元へ例外を伝えよう

import sys

def test_exception(number):
    try:
        return 100 / number

    except ZeroDivisionError as e:
        raise e

    finally:
        print("処理が終了しました")


try:
    test_exception(0)

except ZeroDivisionError as e:
    sys.stderr.write("0で割り算できません")