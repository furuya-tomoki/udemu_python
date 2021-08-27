input_lines = input()
new = input_lines.translate(str.maketrans("54321", "ABCDE"))
 # 複数の文字（長さ1の文字列）を指定して置換する場合は文字列（str型）のtranslate()メソッドを使う。
 # translate()に指定する変換テーブルはstr.maketrans()関数で作成する。
 # 複数の文字（長さ1の文字列）を置換する場合はtranslate()
 # str.maketrans()関数には置換元文字をキー、置換先文字列を値とする辞書を指定する。

print(new)