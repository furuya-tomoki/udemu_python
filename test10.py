inputa = input().split()
 # 3, 5が代入されている
kolom = int(inputa[0])
 # 3が代入
baris = int(inputa[1])
 # 5が代入

rule = kolom,baris >= 1 and kolom,baris<=20

if(rule):
    for b in range(baris):
        stringa = input()
        if(len(stringa) == kolom):
            print(stringa)


# 入力例1
# 3 5
# abc
# def
# hij
# klm
# nop

# 出力例1
# abc
# def
# hij
# klm
# nop