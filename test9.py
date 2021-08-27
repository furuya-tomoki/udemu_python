n = int(input())
num_list = [int(input()) for _ in range(n)]
num1 = sum(num_list) / len(num_list)

print (round(num1))  # 出力を確認



lotre = input()
code = lotre[0].upper()
rule = len(lotre) == 4 and type(code) == str

if(rule):
    if(int(lotre[1]) == int(lotre[2]) == int(lotre[3])):
        print("Yes")
    else:
        print("No")
        
print(code)