{"filter":false,"title":"paiza3.py","tooltip":"/paiza3.py","undoManager":{"mark":89,"position":89,"stack":[[{"start":{"row":0,"column":0},"end":{"row":6,"column":10},"action":"insert","lines":["for inの基本形","","# coding: utf-8","# for inによるループ処理","","for カウンタ変数 in 繰り返す範囲:","    繰り返し処理"],"id":1}],[{"start":{"row":6,"column":10},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":8,"column":4},"end":{"row":12,"column":24},"action":"insert","lines":[" range関数","繰り返しの回数を指定する","","range(10) 0から9まで、10回繰り返す","range(6, 11) 6から10まで繰り返す"],"id":3}],[{"start":{"row":12,"column":24},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":18,"column":22},"action":"insert","lines":["# coding: utf-8","# for inによるループ処理","for i in range(6, 11):","    print(\"hello\" + str(i))","print(\"last\" + str(i))"],"id":5}],[{"start":{"row":18,"column":22},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":28,"column":13},"action":"insert","lines":[" whileの基本形","","# coding: utf-8","# whileによるループ処理","","カウンタ変数を初期化","while 条件式:","    繰り返し処理","    カウンタ変数を更新"],"id":8}],[{"start":{"row":28,"column":13},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":9},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"insert","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":31,"column":18},"action":"insert","lines":[" str関数","数値データをテキストデータに変換する"],"id":10}],[{"start":{"row":31,"column":18},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":41,"column":22},"action":"insert","lines":["# coding: utf-8","# whileによるループ処理","i = 1","while i <= 10:","    print(i)","    i = i + 1","    print(\"next\" + str(i))","    ","print(\"last\" + str(i))"],"id":12}],[{"start":{"row":41,"column":22},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":42,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":43,"column":0},"end":{"row":51,"column":15},"action":"insert","lines":[" whileの基本形","","# coding: utf-8","# whileによるループ処理","","カウンタ変数を初期化","while 条件式:","      繰り返し処理","      カウンタ変数を更新"],"id":14}],[{"start":{"row":51,"column":15},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":52,"column":0},"end":{"row":52,"column":6},"action":"insert","lines":["      "]},{"start":{"row":52,"column":6},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":53,"column":6},"action":"insert","lines":["      "]}],[{"start":{"row":53,"column":6},"end":{"row":54,"column":18},"action":"insert","lines":["str関数","数値データをテキストデータに変換する"],"id":16}],[{"start":{"row":54,"column":18},"end":{"row":55,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":55,"column":0},"end":{"row":56,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":56,"column":0},"end":{"row":59,"column":36},"action":"insert","lines":["代入演算子","演算子\t使用例\t意味\t別の書き方","+=\ta += 1\ta変数の値を1増加させる。\ta = a + 1と同じ","-=\ta -= 1\ta変数の値を1減少させる。\ta = a - 1と同じ"],"id":18}],[{"start":{"row":59,"column":36},"end":{"row":60,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":60,"column":0},"end":{"row":61,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":61,"column":0},"end":{"row":70,"column":12},"action":"insert","lines":["# coding: utf-8","# whileによるループ処理","","import random ","hp = 30","while hp > 0:","    hit = random.randint(1,10)","    print(\"スライムに\" + str(hit) + \"のダメージを与えた\")","    hp -= hit","print(\"倒した\")"],"id":20}],[{"start":{"row":70,"column":12},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":72,"column":0},"end":{"row":78,"column":10},"action":"insert","lines":[" for inの基本形","","# coding: utf-8","# for inによるループ処理","","for カウンタ変数 in 繰り返す範囲:","    繰り返し処理"],"id":22}],[{"start":{"row":78,"column":10},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]},{"start":{"row":79,"column":4},"end":{"row":80,"column":0},"action":"insert","lines":["",""]},{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":80,"column":4},"end":{"row":81,"column":18},"action":"insert","lines":[" str関数","数値データをテキストデータに変換する"],"id":24}],[{"start":{"row":81,"column":18},"end":{"row":82,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":83,"column":0},"end":{"row":87,"column":24},"action":"insert","lines":[" range関数","繰り返しの回数を指定する","","range(10) 0から9まで、10回繰り返す","range(6, 11) 6から10まで繰り返す"],"id":26}],[{"start":{"row":87,"column":24},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":27},{"start":{"row":88,"column":0},"end":{"row":89,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":89,"column":0},"end":{"row":95,"column":9},"action":"insert","lines":[" プルダウン表示の基本形","","<select name='age'>","  <option>1才</option>","  <option>2才</option>","  <option>3才</option>","</select>"],"id":28}],[{"start":{"row":95,"column":9},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":96,"column":0},"end":{"row":97,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":97,"column":0},"end":{"row":103,"column":0},"action":"insert","lines":["# coding: utf-8","# 年齢入力のプルダウン作成","print(\"<select name=\\'age\\'>\")","for age in range(100):","    print(\"<option>\" + str(age + 1) + \"歳</option>\")","print(\"</select>\")",""],"id":30}],[{"start":{"row":102,"column":18},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":103,"column":0},"end":{"row":104,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":104,"column":0},"end":{"row":106,"column":100},"action":"insert","lines":["標準入力とは","もともとはLINUXなどのUnix系OSで用意されていた仕組みです。","標準入力に対応するようにプログラムを作っておけば、プログラム実行時に、ファイルを読み込んだり、キーボードからデータを読み込んだり、パラメータを指定したりというように、入力先を切り替えることができます。"],"id":32}],[{"start":{"row":107,"column":0},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":33}],[{"start":{"row":108,"column":0},"end":{"row":112,"column":14},"action":"insert","lines":["input()","標準入力から1行読み込む","","","line = input()"],"id":34}],[{"start":{"row":112,"column":14},"end":{"row":113,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":113,"column":0},"end":{"row":114,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":114,"column":0},"end":{"row":117,"column":16},"action":"insert","lines":["# coding: utf-8","# inputによる入力処理","line = int(input())","print(line * 10)"],"id":36}],[{"start":{"row":117,"column":16},"end":{"row":118,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":118,"column":0},"end":{"row":119,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":119,"column":0},"end":{"row":128,"column":26},"action":"insert","lines":[""," 複数行読み込みの基本形","","# coding: utf-8","# 標準入力とループ処理","count = int(input())","print(\"データ個数 \" + str(count))","for i in range(count):","    line = input().rstrip()","    print(\"hello \" + line)"],"id":38}],[{"start":{"row":128,"column":26},"end":{"row":129,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":129,"column":0},"end":{"row":129,"column":4},"action":"remove","lines":["    "],"id":40}],[{"start":{"row":129,"column":0},"end":{"row":130,"column":0},"action":"insert","lines":["",""],"id":41}],[{"start":{"row":130,"column":0},"end":{"row":139,"column":26},"action":"insert","lines":[""," 複数行読み込みの基本形","","# coding: utf-8","# 標準入力とループ処理","count = int(input())","print(\"データ個数 \" + str(count))","for i in range(count):","    line = input().rstrip()","    print(\"hello \" + line)"],"id":42}],[{"start":{"row":139,"column":26},"end":{"row":140,"column":0},"action":"insert","lines":["",""],"id":43},{"start":{"row":140,"column":0},"end":{"row":140,"column":4},"action":"insert","lines":["    "]},{"start":{"row":140,"column":4},"end":{"row":141,"column":0},"action":"insert","lines":["",""]},{"start":{"row":141,"column":0},"end":{"row":141,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":141,"column":4},"end":{"row":146,"column":23},"action":"insert","lines":[" rstrip()","データの行末の改行を削除する。","改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しています。インプットの後に、ドットに続けて記述することで、インプットの戻り値の改行を削除することができます。","","","line = input().rstrip()"],"id":44}],[{"start":{"row":146,"column":23},"end":{"row":147,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":147,"column":0},"end":{"row":148,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":148,"column":0},"end":{"row":153,"column":26},"action":"insert","lines":["","count = int(input())","print(\"データ個数 \" + str(count))","for i in range(count):","    line = input().rstrip()","    print(\"hello \" + line)"],"id":46}],[{"start":{"row":153,"column":26},"end":{"row":154,"column":0},"action":"insert","lines":["",""],"id":47},{"start":{"row":154,"column":0},"end":{"row":154,"column":4},"action":"insert","lines":["    "]},{"start":{"row":154,"column":4},"end":{"row":155,"column":0},"action":"insert","lines":["",""]},{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":155,"column":0},"end":{"row":155,"column":4},"action":"remove","lines":["    "],"id":48}],[{"start":{"row":155,"column":0},"end":{"row":155,"column":1},"action":"insert","lines":["n"],"id":49},{"start":{"row":155,"column":1},"end":{"row":155,"column":2},"action":"insert","lines":["u"]},{"start":{"row":155,"column":2},"end":{"row":155,"column":3},"action":"insert","lines":["m"]},{"start":{"row":155,"column":3},"end":{"row":155,"column":4},"action":"insert","lines":["1"]}],[{"start":{"row":155,"column":4},"end":{"row":155,"column":5},"action":"insert","lines":[" "],"id":50},{"start":{"row":155,"column":5},"end":{"row":155,"column":6},"action":"insert","lines":["="]}],[{"start":{"row":155,"column":6},"end":{"row":155,"column":7},"action":"insert","lines":[" "],"id":51},{"start":{"row":155,"column":7},"end":{"row":155,"column":8},"action":"insert","lines":["i"]},{"start":{"row":155,"column":8},"end":{"row":155,"column":9},"action":"insert","lines":["n"]},{"start":{"row":155,"column":9},"end":{"row":155,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":155,"column":10},"end":{"row":155,"column":12},"action":"insert","lines":["()"],"id":52}],[{"start":{"row":155,"column":11},"end":{"row":155,"column":12},"action":"insert","lines":["i"],"id":53},{"start":{"row":155,"column":12},"end":{"row":155,"column":13},"action":"insert","lines":["n"]},{"start":{"row":155,"column":13},"end":{"row":155,"column":14},"action":"insert","lines":["p"]},{"start":{"row":155,"column":14},"end":{"row":155,"column":15},"action":"insert","lines":["u"]},{"start":{"row":155,"column":15},"end":{"row":155,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":155,"column":16},"end":{"row":155,"column":18},"action":"insert","lines":["()"],"id":54}],[{"start":{"row":155,"column":19},"end":{"row":156,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":156,"column":0},"end":{"row":156,"column":1},"action":"insert","lines":["n"]},{"start":{"row":156,"column":1},"end":{"row":156,"column":2},"action":"insert","lines":["u"]},{"start":{"row":156,"column":2},"end":{"row":156,"column":3},"action":"insert","lines":["m"]},{"start":{"row":156,"column":3},"end":{"row":156,"column":4},"action":"insert","lines":["2"]}],[{"start":{"row":156,"column":4},"end":{"row":156,"column":5},"action":"insert","lines":[" "],"id":56},{"start":{"row":156,"column":5},"end":{"row":156,"column":6},"action":"insert","lines":["0"]}],[{"start":{"row":156,"column":5},"end":{"row":156,"column":6},"action":"remove","lines":["0"],"id":57}],[{"start":{"row":156,"column":5},"end":{"row":156,"column":6},"action":"insert","lines":["="],"id":58}],[{"start":{"row":156,"column":6},"end":{"row":156,"column":7},"action":"insert","lines":[" "],"id":59},{"start":{"row":156,"column":7},"end":{"row":156,"column":8},"action":"insert","lines":["i"]},{"start":{"row":156,"column":8},"end":{"row":156,"column":9},"action":"insert","lines":["n"]},{"start":{"row":156,"column":9},"end":{"row":156,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":156,"column":10},"end":{"row":156,"column":12},"action":"insert","lines":["()"],"id":60}],[{"start":{"row":156,"column":11},"end":{"row":156,"column":12},"action":"insert","lines":["i"],"id":61},{"start":{"row":156,"column":12},"end":{"row":156,"column":13},"action":"insert","lines":["n"]},{"start":{"row":156,"column":13},"end":{"row":156,"column":14},"action":"insert","lines":["p"]},{"start":{"row":156,"column":14},"end":{"row":156,"column":15},"action":"insert","lines":["u"]},{"start":{"row":156,"column":15},"end":{"row":156,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":156,"column":16},"end":{"row":156,"column":18},"action":"insert","lines":["()"],"id":62}],[{"start":{"row":156,"column":19},"end":{"row":157,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":157,"column":0},"end":{"row":158,"column":0},"action":"insert","lines":["",""]},{"start":{"row":158,"column":0},"end":{"row":158,"column":1},"action":"insert","lines":["f"]},{"start":{"row":158,"column":1},"end":{"row":158,"column":2},"action":"insert","lines":["o"]},{"start":{"row":158,"column":2},"end":{"row":158,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":158,"column":3},"end":{"row":158,"column":4},"action":"insert","lines":[" "],"id":64},{"start":{"row":158,"column":4},"end":{"row":158,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":158,"column":5},"end":{"row":158,"column":6},"action":"insert","lines":[" "],"id":65},{"start":{"row":158,"column":6},"end":{"row":158,"column":7},"action":"insert","lines":["i"]},{"start":{"row":158,"column":7},"end":{"row":158,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":158,"column":8},"end":{"row":158,"column":9},"action":"insert","lines":[" "],"id":66},{"start":{"row":158,"column":9},"end":{"row":158,"column":10},"action":"insert","lines":["r"]},{"start":{"row":158,"column":10},"end":{"row":158,"column":11},"action":"insert","lines":["a"]},{"start":{"row":158,"column":11},"end":{"row":158,"column":12},"action":"insert","lines":["n"]},{"start":{"row":158,"column":12},"end":{"row":158,"column":13},"action":"insert","lines":["g"]},{"start":{"row":158,"column":13},"end":{"row":158,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":158,"column":13},"end":{"row":158,"column":14},"action":"remove","lines":["e"],"id":67},{"start":{"row":158,"column":12},"end":{"row":158,"column":13},"action":"remove","lines":["g"]},{"start":{"row":158,"column":11},"end":{"row":158,"column":12},"action":"remove","lines":["n"]},{"start":{"row":158,"column":10},"end":{"row":158,"column":11},"action":"remove","lines":["a"]},{"start":{"row":158,"column":9},"end":{"row":158,"column":10},"action":"remove","lines":["r"]}],[{"start":{"row":158,"column":9},"end":{"row":158,"column":10},"action":"insert","lines":["r"],"id":68},{"start":{"row":158,"column":10},"end":{"row":158,"column":11},"action":"insert","lines":["a"]},{"start":{"row":158,"column":11},"end":{"row":158,"column":12},"action":"insert","lines":["n"]},{"start":{"row":158,"column":12},"end":{"row":158,"column":13},"action":"insert","lines":["g"]},{"start":{"row":158,"column":13},"end":{"row":158,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":158,"column":14},"end":{"row":158,"column":16},"action":"insert","lines":["()"],"id":69}],[{"start":{"row":158,"column":15},"end":{"row":158,"column":16},"action":"insert","lines":["n"],"id":70},{"start":{"row":158,"column":16},"end":{"row":158,"column":17},"action":"insert","lines":["u"]},{"start":{"row":158,"column":17},"end":{"row":158,"column":18},"action":"insert","lines":["m"]},{"start":{"row":158,"column":18},"end":{"row":158,"column":19},"action":"insert","lines":["1"]},{"start":{"row":158,"column":19},"end":{"row":158,"column":20},"action":"insert","lines":[","]}],[{"start":{"row":158,"column":20},"end":{"row":158,"column":21},"action":"insert","lines":[" "],"id":71},{"start":{"row":158,"column":21},"end":{"row":158,"column":22},"action":"insert","lines":["n"]},{"start":{"row":158,"column":22},"end":{"row":158,"column":23},"action":"insert","lines":["u"]},{"start":{"row":158,"column":23},"end":{"row":158,"column":24},"action":"insert","lines":["m"]},{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"insert","lines":["2"]}],[{"start":{"row":158,"column":25},"end":{"row":158,"column":26},"action":"insert","lines":[" "],"id":72},{"start":{"row":158,"column":26},"end":{"row":158,"column":27},"action":"insert","lines":["+"]}],[{"start":{"row":158,"column":27},"end":{"row":158,"column":28},"action":"insert","lines":[" "],"id":73},{"start":{"row":158,"column":28},"end":{"row":158,"column":29},"action":"insert","lines":["1"]}],[{"start":{"row":158,"column":30},"end":{"row":159,"column":0},"action":"insert","lines":["",""],"id":74}],[{"start":{"row":158,"column":30},"end":{"row":159,"column":0},"action":"remove","lines":["",""],"id":75}],[{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"insert","lines":[":"],"id":76}],[{"start":{"row":158,"column":31},"end":{"row":159,"column":0},"action":"insert","lines":["",""],"id":77},{"start":{"row":159,"column":0},"end":{"row":159,"column":4},"action":"insert","lines":["    "]},{"start":{"row":159,"column":4},"end":{"row":159,"column":5},"action":"insert","lines":["p"]},{"start":{"row":159,"column":5},"end":{"row":159,"column":6},"action":"insert","lines":["r"]},{"start":{"row":159,"column":6},"end":{"row":159,"column":7},"action":"insert","lines":["i"]},{"start":{"row":159,"column":7},"end":{"row":159,"column":8},"action":"insert","lines":["n"]},{"start":{"row":159,"column":8},"end":{"row":159,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":159,"column":9},"end":{"row":159,"column":11},"action":"insert","lines":["()"],"id":78}],[{"start":{"row":159,"column":10},"end":{"row":159,"column":11},"action":"insert","lines":["i"],"id":79}],[{"start":{"row":159,"column":12},"end":{"row":160,"column":0},"action":"insert","lines":["",""],"id":80},{"start":{"row":160,"column":0},"end":{"row":160,"column":4},"action":"insert","lines":["    "]},{"start":{"row":160,"column":4},"end":{"row":161,"column":0},"action":"insert","lines":["",""]},{"start":{"row":161,"column":0},"end":{"row":161,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":161,"column":0},"end":{"row":161,"column":4},"action":"remove","lines":["    "],"id":81}],[{"start":{"row":161,"column":0},"end":{"row":167,"column":10},"action":"insert","lines":[" for inの基本形","","# coding: utf-8","# for inによるループ処理","","for カウンタ変数 in 繰り返す範囲:","    繰り返し処理"],"id":82}],[{"start":{"row":167,"column":10},"end":{"row":168,"column":0},"action":"insert","lines":["",""],"id":83},{"start":{"row":168,"column":0},"end":{"row":168,"column":4},"action":"insert","lines":["    "]},{"start":{"row":168,"column":4},"end":{"row":169,"column":0},"action":"insert","lines":["",""]},{"start":{"row":169,"column":0},"end":{"row":169,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":169,"column":4},"end":{"row":190,"column":35},"action":"insert","lines":[" 西暦年／平成年の計算方法","平成年から西暦年を求めるには、平成年に「1988」を足します","","","西暦年 = 平成年 + 1988","","","例)","平成1年に「1988」を足すと、1989 > 平成1年は1989年。","平成2年に「1988」を足すと、1990 > 平成2年は1990年。","平成3年に「1988」を足すと、1990 > 平成3年は1991年。","","","西暦年から平成年を求めるには、これとは逆に、西暦年から「1988」を引きます。","","平成年 = 西暦年 - 1988","","","例)","西暦1989年から「1988」を引くと、1 > 1989年は平成1年。","西暦1990年から「1988」を引くと、2 > 1990年は平成2年。","西暦1991年から「1988」を引くと、3 > 1991年は平成3年。"],"id":84}],[{"start":{"row":190,"column":35},"end":{"row":191,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":191,"column":0},"end":{"row":192,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":192,"column":0},"end":{"row":198,"column":38},"action":"insert","lines":["# 西暦年と平成年の対応表を作る","# 1989年から2016年までをループで出力","# ループ内で、各西暦年を平成年に変換","for seireki in range(1989, 2017):","    print(\"西暦\" + str(seireki) + \"年は、\", end=\"\" )","    heisei = seireki - 1989","    print(\"平成\" + str(heisei) + \"年です。\")"],"id":86}],[{"start":{"row":198,"column":38},"end":{"row":199,"column":0},"action":"insert","lines":["",""],"id":87},{"start":{"row":199,"column":0},"end":{"row":199,"column":4},"action":"insert","lines":["    "]},{"start":{"row":199,"column":4},"end":{"row":200,"column":0},"action":"insert","lines":["",""]},{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":200,"column":4},"end":{"row":203,"column":36},"action":"insert","lines":["for seireki in range(num1, num1 + num2):","    print(\"西暦\" + str(seireki) + \"年は\",end=\"\")","    showa = seireki - 1925","    print(\"昭和\" + str(showa) + \"年です\")"],"id":88}],[{"start":{"row":199,"column":4},"end":{"row":200,"column":0},"action":"insert","lines":["",""],"id":89},{"start":{"row":200,"column":0},"end":{"row":200,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["#"],"id":90},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["#"]},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"remove","lines":["#"]},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["#"]},{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"remove","lines":["#"]},{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["#"]},{"start":{"row":33,"column":0},"end":{"row":33,"column":1},"action":"remove","lines":["#"]},{"start":{"row":34,"column":0},"end":{"row":34,"column":1},"action":"remove","lines":["#"]},{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"remove","lines":["#"]},{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"remove","lines":["#"]},{"start":{"row":61,"column":0},"end":{"row":61,"column":1},"action":"remove","lines":["#"]},{"start":{"row":62,"column":0},"end":{"row":62,"column":1},"action":"remove","lines":["#"]},{"start":{"row":74,"column":0},"end":{"row":74,"column":1},"action":"remove","lines":["#"]},{"start":{"row":75,"column":0},"end":{"row":75,"column":1},"action":"remove","lines":["#"]},{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"remove","lines":["#"]},{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["#"]},{"start":{"row":114,"column":0},"end":{"row":114,"column":1},"action":"remove","lines":["#"]},{"start":{"row":115,"column":0},"end":{"row":115,"column":1},"action":"remove","lines":["#"]},{"start":{"row":122,"column":0},"end":{"row":122,"column":1},"action":"remove","lines":["#"]},{"start":{"row":123,"column":0},"end":{"row":123,"column":1},"action":"remove","lines":["#"]},{"start":{"row":133,"column":0},"end":{"row":133,"column":1},"action":"remove","lines":["#"]},{"start":{"row":134,"column":0},"end":{"row":134,"column":1},"action":"remove","lines":["#"]},{"start":{"row":163,"column":0},"end":{"row":163,"column":1},"action":"remove","lines":["#"]},{"start":{"row":164,"column":0},"end":{"row":164,"column":1},"action":"remove","lines":["#"]},{"start":{"row":192,"column":0},"end":{"row":192,"column":1},"action":"remove","lines":["#"]},{"start":{"row":193,"column":0},"end":{"row":193,"column":1},"action":"remove","lines":["#"]},{"start":{"row":194,"column":0},"end":{"row":194,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":91},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":2},"action":"insert","lines":["# "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["# "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["# "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["# "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["# "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":2},"action":"insert","lines":["# "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":2},"action":"insert","lines":["# "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":2},"action":"insert","lines":["# "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"insert","lines":["# "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["# "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"insert","lines":["# "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"insert","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["# "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":2},"action":"insert","lines":["# "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":2},"action":"insert","lines":["# "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["# "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":2},"action":"insert","lines":["# "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["# "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":2},"action":"insert","lines":["# "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["# "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["# "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":2},"action":"insert","lines":["# "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["# "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["# "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":2},"action":"insert","lines":["# "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":2},"action":"insert","lines":["# "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":2},"action":"insert","lines":["# "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":2},"action":"insert","lines":["# "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":2},"action":"insert","lines":["# "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":2},"action":"insert","lines":["# "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":2},"action":"insert","lines":["# "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":2},"action":"insert","lines":["# "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":2},"action":"insert","lines":["# "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":2},"action":"insert","lines":["# "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["# "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"insert","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["# "]},{"start":{"row":128,"column":0},"end":{"row":128,"column":2},"action":"insert","lines":["# "]},{"start":{"row":131,"column":0},"end":{"row":131,"column":2},"action":"insert","lines":["# "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":2},"action":"insert","lines":["# "]},{"start":{"row":134,"column":0},"end":{"row":134,"column":2},"action":"insert","lines":["# "]},{"start":{"row":135,"column":0},"end":{"row":135,"column":2},"action":"insert","lines":["# "]},{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["# "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["# "]},{"start":{"row":138,"column":0},"end":{"row":138,"column":2},"action":"insert","lines":["# "]},{"start":{"row":139,"column":0},"end":{"row":139,"column":2},"action":"insert","lines":["# "]},{"start":{"row":141,"column":0},"end":{"row":141,"column":2},"action":"insert","lines":["# "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":2},"action":"insert","lines":["# "]},{"start":{"row":143,"column":0},"end":{"row":143,"column":2},"action":"insert","lines":["# "]},{"start":{"row":146,"column":0},"end":{"row":146,"column":2},"action":"insert","lines":["# "]},{"start":{"row":149,"column":0},"end":{"row":149,"column":2},"action":"insert","lines":["# "]},{"start":{"row":150,"column":0},"end":{"row":150,"column":2},"action":"insert","lines":["# "]},{"start":{"row":151,"column":0},"end":{"row":151,"column":2},"action":"insert","lines":["# "]},{"start":{"row":152,"column":0},"end":{"row":152,"column":2},"action":"insert","lines":["# "]},{"start":{"row":153,"column":0},"end":{"row":153,"column":2},"action":"insert","lines":["# "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":2},"action":"insert","lines":["# "]},{"start":{"row":156,"column":0},"end":{"row":156,"column":2},"action":"insert","lines":["# "]},{"start":{"row":158,"column":0},"end":{"row":158,"column":2},"action":"insert","lines":["# "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":2},"action":"insert","lines":["# "]},{"start":{"row":161,"column":0},"end":{"row":161,"column":2},"action":"insert","lines":["# "]},{"start":{"row":163,"column":0},"end":{"row":163,"column":2},"action":"insert","lines":["# "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":2},"action":"insert","lines":["# "]},{"start":{"row":166,"column":0},"end":{"row":166,"column":2},"action":"insert","lines":["# "]},{"start":{"row":167,"column":0},"end":{"row":167,"column":2},"action":"insert","lines":["# "]},{"start":{"row":169,"column":0},"end":{"row":169,"column":2},"action":"insert","lines":["# "]},{"start":{"row":170,"column":0},"end":{"row":170,"column":2},"action":"insert","lines":["# "]},{"start":{"row":173,"column":0},"end":{"row":173,"column":2},"action":"insert","lines":["# "]},{"start":{"row":176,"column":0},"end":{"row":176,"column":2},"action":"insert","lines":["# "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":2},"action":"insert","lines":["# "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":2},"action":"insert","lines":["# "]},{"start":{"row":179,"column":0},"end":{"row":179,"column":2},"action":"insert","lines":["# "]},{"start":{"row":182,"column":0},"end":{"row":182,"column":2},"action":"insert","lines":["# "]},{"start":{"row":184,"column":0},"end":{"row":184,"column":2},"action":"insert","lines":["# "]},{"start":{"row":187,"column":0},"end":{"row":187,"column":2},"action":"insert","lines":["# "]},{"start":{"row":188,"column":0},"end":{"row":188,"column":2},"action":"insert","lines":["# "]},{"start":{"row":189,"column":0},"end":{"row":189,"column":2},"action":"insert","lines":["# "]},{"start":{"row":190,"column":0},"end":{"row":190,"column":2},"action":"insert","lines":["# "]},{"start":{"row":192,"column":0},"end":{"row":192,"column":2},"action":"insert","lines":["# "]},{"start":{"row":193,"column":0},"end":{"row":193,"column":2},"action":"insert","lines":["# "]},{"start":{"row":194,"column":0},"end":{"row":194,"column":2},"action":"insert","lines":["# "]},{"start":{"row":195,"column":0},"end":{"row":195,"column":2},"action":"insert","lines":["# "]},{"start":{"row":196,"column":0},"end":{"row":196,"column":2},"action":"insert","lines":["# "]},{"start":{"row":197,"column":0},"end":{"row":197,"column":2},"action":"insert","lines":["# "]},{"start":{"row":198,"column":0},"end":{"row":198,"column":2},"action":"insert","lines":["# "]},{"start":{"row":201,"column":0},"end":{"row":201,"column":2},"action":"insert","lines":["# "]},{"start":{"row":202,"column":0},"end":{"row":202,"column":2},"action":"insert","lines":["# "]},{"start":{"row":203,"column":0},"end":{"row":203,"column":2},"action":"insert","lines":["# "]},{"start":{"row":204,"column":0},"end":{"row":204,"column":2},"action":"insert","lines":["# "]}]]},"ace":{"folds":[],"scrolltop":827,"scrollleft":19.5,"selection":{"start":{"row":0,"column":0},"end":{"row":204,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"mode":"ace/mode/python"}},"timestamp":1628635728023,"hash":"068f5c3966f5d81651526b76e0e24ab815cd71f7"}