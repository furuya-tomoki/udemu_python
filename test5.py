N = int(input())
result = 0


rule = N>= 1 and N<=100
if(rule):
    n = input().split()
    if(len(n) == N):
        for _ in n:
            _ = int(_)
            result += _
    print(result)