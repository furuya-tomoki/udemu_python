n = int(input())
h = "Hello"
print(h, end=" ")
for i in range(n-1):
     # 最後の「.」を作るために「範囲を-1」しなければいけない
    s1 = input()
    print(s1 + ",", end="")
s1 = input()
print(s1 + ".")