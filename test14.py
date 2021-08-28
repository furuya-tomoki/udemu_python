import re
s = input()
result = re.sub(r"\D", "", s)
 # re.sub()は、文字列を置換するための関数
 #「r”\D”」で数字以外を指定し、置換後の文字列を「””」とし
 # 文字列から数字だけを取り出すことができます
print(result)