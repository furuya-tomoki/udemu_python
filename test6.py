s = input().rstrip().split(' ')
s = list(map(int, s)) 
n = sum(s)

print(str(n)[-1])