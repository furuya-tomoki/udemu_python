i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
# インデックス番号0を100に変更
print("j =", j)
print("i =", i)
# 配列内の要素が「i」「j」も変更されてしまう

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print("y =",y)
print("x =",x)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ["a", "b"]
Y = X
Y[0] = "p"
print(id(X))
print(id(Y))
print(Y)
print(X)
