a = list(map(int, input().split()))
n = int(input())

for i in range(n):
    c = list(map(int, input().split()))
    if c[0] > a[0]:
        print("Low")
    elif c[0] < a[0]:
        print("High")
    elif c[0] == a[0] and c[1] > a[1]:
        print("High")
    else:
        print("Low")