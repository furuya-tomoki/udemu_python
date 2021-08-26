input_lines = input()
new = input_lines.translate(str.maketrans("54321", "ABCDE"))

print(new)