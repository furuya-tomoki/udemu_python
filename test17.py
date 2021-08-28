nlist = []
hand = 4

for i in range(hand):
    nlist.append(int(input()))
print(15 - sum(nlist))
 # 1~5を足したら15なので、引いた数が出力結果