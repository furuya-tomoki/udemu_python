s = str(input())

print(s.replace('noaki', ''))
 # 特定の文字を削除
 
input_lines = input()
new = input_lines.translate(str.maketrans("012", "CAB"))

print(new)

# 文字変換 = 012 → CAB