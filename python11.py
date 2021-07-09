a = 1
b = 2

# 等しい
a == b
# 異なる
a != b
# より小さい
a < b
# よりも大きい
a > b
# 以下である
a <= b
# 以上である
a >= b

if a > 0:
    if b > 0:
        print("a positive")
        
if a > 0 and b > 0:
    print("a b posituve")


a = -1
b = 1

if a > 0:
    print("a or b positive")
elif b > 0:
    print("a or b positive")
if a > 0 or b > 0:
    print("a or b positive")