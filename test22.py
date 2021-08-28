S = input()

count1 = S.count("_")
count2 = S.count("-")


if count1 > count2 or count1 == count2:
    print(S.replace("-", "_"))
else:
    print(S.replace("_", "-"))


# 入力例1
# ruby_python-java-php
# 出力例1
# ruby-python-java-php
# 入力例2
# paiza_coding-test
# 出力例2
# paiza_coding_test