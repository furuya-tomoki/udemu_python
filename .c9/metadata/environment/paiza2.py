{"filter":false,"title":"paiza2.py","tooltip":"/paiza2.py","ace":{"folds":[],"scrolltop":1750.5,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":129,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"69a696eac123059792a3b37fc9d345a7684a9cc0","mime":"text/x-script.python","undoManager":{"mark":27,"position":27,"stack":[[{"start":{"row":0,"column":0},"end":{"row":8,"column":36},"action":"insert","lines":[" if else文の基本形","","# coding: utf-8","# if文による条件分岐","number = 1","if number == 1:","    print( \"スキ！\")  #条件式が成立したときの処理","else:","    print( \"キライ\")  #条件式が成立しなかったときの処理"],"id":1}],[{"start":{"row":8,"column":36},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":4},"end":{"row":18,"column":33},"action":"insert","lines":[" インデント","コードの行頭を字下げすることを「インデント」といいます。","Pythonでは、１段のインデントに、タブか半角スペース4つを入力します。","","インデントは、Python では、条件式が成立した時に実行する処理を表すと同時に、","プログラマーにとって、条件式に応じて実行する処理を見分けやすくします。","","Pythonでは、条件式のあとの「:」(コロン)やelseのあとの「:」(コロン)から始まって、","インデント行が終わるまでを、ひとかたまりのブロックとして扱います。"],"id":3}],[{"start":{"row":18,"column":33},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":19,"column":0},"end":{"row":20,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":20,"column":0},"end":{"row":25,"column":33},"action":"insert","lines":[" 作ったプログラムをスキ/キライ占いにしてみる方法","このチャプターで作ったプログラムに","randomモジュールをインポートしたあと、","n = 1 としているところを","n = random.randint(1,2) とすると","コードの実行毎にランダムで結果が変わるスキ/キライ占いが作れます！"],"id":5}],[{"start":{"row":25,"column":33},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":27,"column":0},"end":{"row":37,"column":39},"action":"insert","lines":[" if elif else文の基本形","","# coding: utf-8","# if文による条件分岐","number = 1","if 条件式1:","    print( \"スキ！\")  #条件式1が成立したときの処理","elif 条件式2:","    print( \"どちらでもない\")  #条件式2が成立したときの処理","else:","    print( \"キライ\")  #条件式がどれも成立しなかったときの処理"],"id":7}],[{"start":{"row":37,"column":39},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]},{"start":{"row":38,"column":4},"end":{"row":39,"column":0},"action":"insert","lines":["",""]},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":49,"column":39},"action":"insert","lines":[" if elif else文の基本形","","# coding: utf-8","# if文による条件分岐","number = 1","if 条件式1:","    print( \"スキ！\")  #条件式1が成立したときの処理","elif 条件式2:","    print( \"どちらでもない\")  #条件式2が成立したときの処理","else:","    print( \"キライ\")  #条件式がどれも成立しなかったときの処理"],"id":9}],[{"start":{"row":49,"column":39},"end":{"row":50,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]},{"start":{"row":50,"column":4},"end":{"row":51,"column":0},"action":"insert","lines":["",""]},{"start":{"row":51,"column":0},"end":{"row":51,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":51,"column":4},"end":{"row":56,"column":27},"action":"insert","lines":["利用例\t意味\t真になる例","a < b\ta が b よりも小さい\t10 < 15","a > b\ta が b よりも大きい\t10 > 7","a <= b\ta が b 以下である\t10 <= 15","a >= b\ta が b 以上である\t10 >= 7","a != b\ta と b が等しくない\t10 != 1"],"id":11}],[{"start":{"row":56,"column":27},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":57,"column":0},"end":{"row":58,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":58,"column":0},"end":{"row":70,"column":33},"action":"insert","lines":[" print関数で改行したくない場合","print関数で改行したくない場合、ひとつの方法は、文字列を「,」で区切ります。","この場合、出力された文字列は、スペースで区切られます。","","","print(\"<h1>hello world</h1>\", \"<p>世界の皆さん、\", \"<b>こんにちは</b></p>\")","","","もうひとつの方法は、カッコの中に「, end=\"\"」を追加します。","","print(\"<h1>hello world</h1>\", end=\"\")","print(\"<p>世界の皆さん、\", end=\"\")","print(\"<b>こんにちは</b></p>\", end=\"\")"],"id":13}],[{"start":{"row":58,"column":0},"end":{"row":58,"column":1},"action":"remove","lines":[" "],"id":14}],[{"start":{"row":70,"column":33},"end":{"row":71,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":71,"column":0},"end":{"row":72,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":72,"column":0},"end":{"row":82,"column":38},"action":"insert","lines":[" if elif else文の基本形","","# coding: utf-8","# if文による条件分岐","number = 1","if 条件式1:","    print( \"スキ！\")\t#条件式1が成立したときの処理","elif 条件式2:","    print( \"どちらでもない\")\t#条件式2が成立したときの処理","else:","    print( \"キライ\")\t#条件式がどれも成立しなかったときの処理"],"id":16}],[{"start":{"row":82,"column":38},"end":{"row":83,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":83,"column":0},"end":{"row":83,"column":4},"action":"insert","lines":["    "]},{"start":{"row":83,"column":4},"end":{"row":84,"column":0},"action":"insert","lines":["",""]},{"start":{"row":84,"column":0},"end":{"row":84,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":84,"column":4},"end":{"row":89,"column":27},"action":"insert","lines":["利用例\t意味\t真になる例","a < b\ta が b よりも小さい\t10 < 15","a > b\ta が b よりも大きい\t10 > 7","a <= b\ta が b 以下である\t10 <= 15","a >= b\ta が b 以上である\t10 >= 7","a != b\ta と b が等しくない\t10 != 1"],"id":18}],[{"start":{"row":89,"column":27},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":90,"column":0},"end":{"row":91,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":91,"column":0},"end":{"row":98,"column":40},"action":"insert","lines":["デバッグとは","デバッグ (debug) とは、プログラムの不具合・欠陥を発見および修正し、","正常に動作させるための作業全般のことです。このような、プログラム上の","不具合・欠陥をバグ(bug)と呼びます。","","動画の中では、デバッグとして、","randint関数で何の値がomikuji変数に代入されたかを出力して、","omiokuji変数の値に対して、if文が期待通りに動いているか確認しています。"],"id":20}],[{"start":{"row":98,"column":40},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":99,"column":0},"end":{"row":100,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":100,"column":0},"end":{"row":110,"column":38},"action":"insert","lines":[" if elif else文の基本形","","# coding: utf-8","# if文による条件分岐","number = 1","if 条件式1:","    print( \"スキ！\")\t#条件式1が成立したときの処理","elif 条件式2:","    print( \"どちらでもない\")\t#条件式2が成立したときの処理","else:","    print( \"キライ\")\t#条件式がどれも成立しなかったときの処理"],"id":22}],[{"start":{"row":110,"column":38},"end":{"row":111,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"insert","lines":["    "]},{"start":{"row":111,"column":4},"end":{"row":112,"column":0},"action":"insert","lines":["",""]},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":112,"column":4},"end":{"row":123,"column":36},"action":"insert","lines":["西暦年／平成年の計算方法","平成年から西暦年を求めるには、平成年に「1988」を足します","　例)","　平成1年に「1988」を足すと、1989 > 平成1年は1989年。","　平成2年に「1988」を足すと、1990 > 平成2年は1990年。","　平成3年に「1988」を足すと、1990 > 平成3年は1991年。","","西暦年から平成年を求めるには、これとは逆に、西暦年から「1988」を引きます。","　例)","　西暦1989年から「1988」を引くと、1 > 1989年は平成1年。","　西暦1990年から「1988」を引くと、2 > 1990年は平成2年。","　西暦1991年から「1988」を引くと、3 > 1991年は平成3年。"],"id":24}],[{"start":{"row":112,"column":3},"end":{"row":123,"column":36},"action":"remove","lines":[" 西暦年／平成年の計算方法","平成年から西暦年を求めるには、平成年に「1988」を足します","　例)","　平成1年に「1988」を足すと、1989 > 平成1年は1989年。","　平成2年に「1988」を足すと、1990 > 平成2年は1990年。","　平成3年に「1988」を足すと、1990 > 平成3年は1991年。","","西暦年から平成年を求めるには、これとは逆に、西暦年から「1988」を引きます。","　例)","　西暦1989年から「1988」を引くと、1 > 1989年は平成1年。","　西暦1990年から「1988」を引くと、2 > 1990年は平成2年。","　西暦1991年から「1988」を引くと、3 > 1991年は平成3年。"],"id":25},{"start":{"row":112,"column":2},"end":{"row":112,"column":3},"action":"remove","lines":[" "]},{"start":{"row":112,"column":1},"end":{"row":112,"column":2},"action":"remove","lines":[" "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":112,"column":0},"end":{"row":129,"column":34},"action":"insert","lines":["# coding: utf-8","# 西暦年から平成年を求める","import datetime","seireki = datatime.data,today().year","print(\"西暦\" + str(seireki) + \"年は、\",end=\"\")","# 平成年から西暦年を求めるには、平成年に「1988」を足します","# 　例)","# 　平成1年に「1988」を足すと、1989 > 平成1年は1989年。","# 　平成2年に「1988」を足すと、1990 > 平成2年は1990年。","# 　平成3年に「1988」を足すと、1990 > 平成3年は1991年。","","# 西暦年から平成年を求めるには、これとは逆に、西暦年から「1988」を引きます。","# 　例)","# 　西暦1989年から「1988」を引くと、1 > 1989年は平成1年。","# 　西暦1990年から「1988」を引くと、2 > 1990年は平成2年。","# 　西暦1991年から「1988」を引くと、3 > 1991年は平成3年。","","print(\"平成\" + str(heisei) + \"年です。\")"],"id":26}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["#"],"id":27},{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["#"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"remove","lines":["#"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["#"]},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":["#"]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["#"]},{"start":{"row":33,"column":19},"end":{"row":33,"column":20},"action":"remove","lines":["#"]},{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"remove","lines":["#"]},{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"remove","lines":["#"]},{"start":{"row":41,"column":0},"end":{"row":41,"column":1},"action":"remove","lines":["#"]},{"start":{"row":42,"column":0},"end":{"row":42,"column":1},"action":"remove","lines":["#"]},{"start":{"row":45,"column":19},"end":{"row":45,"column":20},"action":"remove","lines":["#"]},{"start":{"row":47,"column":23},"end":{"row":47,"column":24},"action":"remove","lines":["#"]},{"start":{"row":49,"column":19},"end":{"row":49,"column":20},"action":"remove","lines":["#"]},{"start":{"row":74,"column":0},"end":{"row":74,"column":1},"action":"remove","lines":["#"]},{"start":{"row":75,"column":0},"end":{"row":75,"column":1},"action":"remove","lines":["#"]},{"start":{"row":78,"column":18},"end":{"row":78,"column":19},"action":"remove","lines":["#"]},{"start":{"row":80,"column":22},"end":{"row":80,"column":23},"action":"remove","lines":["#"]},{"start":{"row":82,"column":18},"end":{"row":82,"column":19},"action":"remove","lines":["#"]},{"start":{"row":102,"column":0},"end":{"row":102,"column":1},"action":"remove","lines":["#"]},{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["#"]},{"start":{"row":106,"column":18},"end":{"row":106,"column":19},"action":"remove","lines":["#"]},{"start":{"row":108,"column":22},"end":{"row":108,"column":23},"action":"remove","lines":["#"]},{"start":{"row":110,"column":18},"end":{"row":110,"column":19},"action":"remove","lines":["#"]},{"start":{"row":112,"column":0},"end":{"row":112,"column":1},"action":"remove","lines":["#"]},{"start":{"row":113,"column":0},"end":{"row":113,"column":1},"action":"remove","lines":["#"]},{"start":{"row":117,"column":0},"end":{"row":117,"column":1},"action":"remove","lines":["#"]},{"start":{"row":118,"column":0},"end":{"row":118,"column":1},"action":"remove","lines":["#"]},{"start":{"row":119,"column":0},"end":{"row":119,"column":1},"action":"remove","lines":["#"]},{"start":{"row":120,"column":0},"end":{"row":120,"column":1},"action":"remove","lines":["#"]},{"start":{"row":121,"column":0},"end":{"row":121,"column":1},"action":"remove","lines":["#"]},{"start":{"row":123,"column":0},"end":{"row":123,"column":1},"action":"remove","lines":["#"]},{"start":{"row":124,"column":0},"end":{"row":124,"column":1},"action":"remove","lines":["#"]},{"start":{"row":125,"column":0},"end":{"row":125,"column":1},"action":"remove","lines":["#"]},{"start":{"row":126,"column":0},"end":{"row":126,"column":1},"action":"remove","lines":["#"]},{"start":{"row":127,"column":0},"end":{"row":127,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":28},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":6,"column":0},"end":{"row":6,"column":2},"action":"insert","lines":["# "]},{"start":{"row":7,"column":0},"end":{"row":7,"column":2},"action":"insert","lines":["# "]},{"start":{"row":8,"column":0},"end":{"row":8,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":18,"column":0},"end":{"row":18,"column":2},"action":"insert","lines":["# "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":2},"action":"insert","lines":["# "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":2},"action":"insert","lines":["# "]},{"start":{"row":36,"column":0},"end":{"row":36,"column":2},"action":"insert","lines":["# "]},{"start":{"row":37,"column":0},"end":{"row":37,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["# "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":51,"column":0},"end":{"row":51,"column":2},"action":"insert","lines":["# "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["# "]},{"start":{"row":53,"column":0},"end":{"row":53,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":2},"action":"insert","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":2},"action":"insert","lines":["# "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["# "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["# "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["# "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":2},"action":"insert","lines":["# "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["# "]},{"start":{"row":82,"column":0},"end":{"row":82,"column":2},"action":"insert","lines":["# "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":2},"action":"insert","lines":["# "]},{"start":{"row":85,"column":0},"end":{"row":85,"column":2},"action":"insert","lines":["# "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":2},"action":"insert","lines":["# "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"insert","lines":["# "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":2},"action":"insert","lines":["# "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["# "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"insert","lines":["# "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"insert","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["# "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"insert","lines":["# "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":2},"action":"insert","lines":["# "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["# "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":2},"action":"insert","lines":["# "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["# "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":2},"action":"insert","lines":["# "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["# "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":2},"action":"insert","lines":["# "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["# "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":2},"action":"insert","lines":["# "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["# "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":2},"action":"insert","lines":["# "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":2},"action":"insert","lines":["# "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":2},"action":"insert","lines":["# "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":2},"action":"insert","lines":["# "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":2},"action":"insert","lines":["# "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":2},"action":"insert","lines":["# "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":2},"action":"insert","lines":["# "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":2},"action":"insert","lines":["# "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":2},"action":"insert","lines":["# "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":2},"action":"insert","lines":["# "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":2},"action":"insert","lines":["# "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":2},"action":"insert","lines":["# "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":2},"action":"insert","lines":["# "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":2},"action":"insert","lines":["# "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["# "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":2},"action":"insert","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["# "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":2},"action":"insert","lines":["# "]}]]},"timestamp":1628575544005}