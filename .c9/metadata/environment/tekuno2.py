{"filter":false,"title":"tekuno2.py","tooltip":"/tekuno2.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":20},"action":"insert","lines":["a = list(map(int, input().split()))","n = int(input())","","for i in range(n):","    c = list(map(int, input().split()))","    if c[0] > a[0]:","        print(\"Low\")","    elif c[0] < a[0]:","        print(\"High\")","    elif c[0] == a[0] and c[1] > a[1]:","        print(\"High\")","    else:","        print(\"Low\")"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":20},"end":{"row":12,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1629191629022,"hash":"062d077a341ac77da415bbbb9adaca94c083cc1f"}