{"filter":false,"title":"paiza6.py","tooltip":"/paiza6.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":161,"column":8},"end":{"row":161,"column":9},"action":"insert","lines":["p"],"id":48},{"start":{"row":161,"column":9},"end":{"row":161,"column":10},"action":"insert","lines":["a"]},{"start":{"row":161,"column":10},"end":{"row":161,"column":11},"action":"insert","lines":["i"]},{"start":{"row":161,"column":11},"end":{"row":161,"column":12},"action":"insert","lines":["z"]},{"start":{"row":161,"column":12},"end":{"row":161,"column":13},"action":"insert","lines":["a"]}],[{"start":{"row":161,"column":14},"end":{"row":161,"column":15},"action":"insert","lines":[" "],"id":49},{"start":{"row":161,"column":15},"end":{"row":161,"column":16},"action":"insert","lines":["f"]},{"start":{"row":161,"column":16},"end":{"row":161,"column":17},"action":"insert","lines":["o"]},{"start":{"row":161,"column":17},"end":{"row":161,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"insert","lines":[" "],"id":50},{"start":{"row":161,"column":19},"end":{"row":161,"column":20},"action":"insert","lines":["i"]}],[{"start":{"row":161,"column":20},"end":{"row":161,"column":21},"action":"insert","lines":[" "],"id":51},{"start":{"row":161,"column":21},"end":{"row":161,"column":22},"action":"insert","lines":["i"]},{"start":{"row":161,"column":22},"end":{"row":161,"column":23},"action":"insert","lines":["n"]}],[{"start":{"row":161,"column":23},"end":{"row":161,"column":24},"action":"insert","lines":[" "],"id":52},{"start":{"row":161,"column":24},"end":{"row":161,"column":25},"action":"insert","lines":["r"]},{"start":{"row":161,"column":25},"end":{"row":161,"column":26},"action":"insert","lines":["a"]},{"start":{"row":161,"column":26},"end":{"row":161,"column":27},"action":"insert","lines":["n"]},{"start":{"row":161,"column":27},"end":{"row":161,"column":28},"action":"insert","lines":["g"]},{"start":{"row":161,"column":28},"end":{"row":161,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":161,"column":29},"end":{"row":161,"column":31},"action":"insert","lines":["()"],"id":53}],[{"start":{"row":161,"column":30},"end":{"row":161,"column":31},"action":"insert","lines":["5"],"id":54}],[{"start":{"row":161,"column":33},"end":{"row":162,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":162,"column":0},"end":{"row":162,"column":1},"action":"insert","lines":["p"]},{"start":{"row":162,"column":1},"end":{"row":162,"column":2},"action":"insert","lines":["r"]},{"start":{"row":162,"column":2},"end":{"row":162,"column":3},"action":"insert","lines":["i"]},{"start":{"row":162,"column":3},"end":{"row":162,"column":4},"action":"insert","lines":["n"]},{"start":{"row":162,"column":4},"end":{"row":162,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":162,"column":5},"end":{"row":162,"column":7},"action":"insert","lines":["()"],"id":56}],[{"start":{"row":162,"column":6},"end":{"row":162,"column":7},"action":"insert","lines":["9"],"id":57}],[{"start":{"row":162,"column":6},"end":{"row":162,"column":7},"action":"remove","lines":["9"],"id":58}],[{"start":{"row":162,"column":6},"end":{"row":162,"column":7},"action":"insert","lines":["a"],"id":59},{"start":{"row":162,"column":7},"end":{"row":162,"column":8},"action":"insert","lines":["n"]},{"start":{"row":162,"column":8},"end":{"row":162,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":162,"column":10},"end":{"row":163,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":163,"column":0},"end":{"row":164,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":164,"column":0},"end":{"row":165,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":166,"column":0},"end":{"row":167,"column":10},"action":"insert","lines":["num = [[7 for i in range(4)] for j in range(5)]","print(num)"],"id":62}],[{"start":{"row":167,"column":10},"end":{"row":168,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":168,"column":0},"end":{"row":169,"column":0},"action":"insert","lines":["",""]},{"start":{"row":169,"column":0},"end":{"row":170,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":170,"column":0},"end":{"row":186,"column":11},"action":"insert","lines":["# ドット絵を表示する","","enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],","             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],","             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],","             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]","","for line in enemy_img:","    for dot in line:","        if dot == 1:","            print(\"#\", end=\"\")","        else:","            print(\" \", end=\"\")","    print()"],"id":64}],[{"start":{"row":186,"column":11},"end":{"row":187,"column":0},"action":"insert","lines":["",""],"id":65},{"start":{"row":187,"column":0},"end":{"row":187,"column":4},"action":"insert","lines":["    "]},{"start":{"row":187,"column":4},"end":{"row":188,"column":0},"action":"insert","lines":["",""]},{"start":{"row":188,"column":0},"end":{"row":188,"column":4},"action":"insert","lines":["    "]},{"start":{"row":188,"column":4},"end":{"row":189,"column":0},"action":"insert","lines":["",""]},{"start":{"row":189,"column":0},"end":{"row":189,"column":4},"action":"insert","lines":["    "]},{"start":{"row":189,"column":4},"end":{"row":190,"column":0},"action":"insert","lines":["",""]},{"start":{"row":190,"column":0},"end":{"row":190,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":190,"column":0},"end":{"row":190,"column":4},"action":"remove","lines":["    "],"id":66}],[{"start":{"row":190,"column":0},"end":{"row":205,"column":13},"action":"insert","lines":["letter_A = [[0,0,1,1,0,0],","            [0,1,0,0,1,0],","            [1,0,0,0,0,1],","            [1,1,1,1,1,1],","            [1,0,0,0,0,1],","            [1,0,0,0,0,1]]","","# ここに、ドットを表示するコードを記述する","for line in letter_A:","    for dot in line:","        if dot == 1:","            print(\"@\", end=\"\")","        else:","            print(\" \", end=\"\")","            ","    print(\"\")"],"id":67}],[{"start":{"row":205,"column":13},"end":{"row":206,"column":0},"action":"insert","lines":["",""],"id":68},{"start":{"row":206,"column":0},"end":{"row":206,"column":4},"action":"insert","lines":["    "]},{"start":{"row":206,"column":4},"end":{"row":206,"column":5},"action":"insert","lines":[" "]}],[{"start":{"row":206,"column":5},"end":{"row":206,"column":6},"action":"insert","lines":["f"],"id":69},{"start":{"row":206,"column":6},"end":{"row":206,"column":7},"action":"insert","lines":["o"]},{"start":{"row":206,"column":7},"end":{"row":206,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":206,"column":8},"end":{"row":206,"column":9},"action":"insert","lines":["　"],"id":70}],[{"start":{"row":206,"column":8},"end":{"row":206,"column":9},"action":"remove","lines":["　"],"id":71}],[{"start":{"row":206,"column":8},"end":{"row":206,"column":9},"action":"insert","lines":["の"],"id":72},{"start":{"row":206,"column":9},"end":{"row":206,"column":22},"action":"insert","lines":["位置にインデントをサロエル"]}],[{"start":{"row":206,"column":21},"end":{"row":206,"column":22},"action":"remove","lines":["ル"],"id":73},{"start":{"row":206,"column":20},"end":{"row":206,"column":21},"action":"remove","lines":["エ"]},{"start":{"row":206,"column":19},"end":{"row":206,"column":20},"action":"remove","lines":["ロ"]},{"start":{"row":206,"column":18},"end":{"row":206,"column":19},"action":"remove","lines":["サ"]}],[{"start":{"row":206,"column":18},"end":{"row":206,"column":21},"action":"insert","lines":["揃える"],"id":74}],[{"start":{"row":206,"column":21},"end":{"row":207,"column":0},"action":"insert","lines":["",""],"id":75},{"start":{"row":207,"column":0},"end":{"row":207,"column":5},"action":"insert","lines":["     "]},{"start":{"row":207,"column":5},"end":{"row":208,"column":0},"action":"insert","lines":["",""]},{"start":{"row":208,"column":0},"end":{"row":208,"column":5},"action":"insert","lines":["     "]},{"start":{"row":208,"column":5},"end":{"row":209,"column":0},"action":"insert","lines":["",""]},{"start":{"row":209,"column":0},"end":{"row":209,"column":5},"action":"insert","lines":["     "]}],[{"start":{"row":209,"column":4},"end":{"row":209,"column":5},"action":"remove","lines":[" "],"id":76},{"start":{"row":209,"column":0},"end":{"row":209,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":209,"column":0},"end":{"row":233,"column":49},"action":"insert","lines":["3次元配列","カギかっこを3重にすると、3次元配列になる。","","","enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],","              [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],","              [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],","             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],","              [1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],","              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]],","             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],","              [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],","              [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]]]"],"id":77}],[{"start":{"row":233,"column":49},"end":{"row":234,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":234,"column":0},"end":{"row":234,"column":14},"action":"insert","lines":["              "]},{"start":{"row":234,"column":14},"end":{"row":235,"column":0},"action":"insert","lines":["",""]},{"start":{"row":235,"column":0},"end":{"row":235,"column":14},"action":"insert","lines":["              "]}],[{"start":{"row":235,"column":13},"end":{"row":235,"column":14},"action":"remove","lines":[" "],"id":79},{"start":{"row":235,"column":12},"end":{"row":235,"column":13},"action":"remove","lines":[" "]},{"start":{"row":235,"column":8},"end":{"row":235,"column":12},"action":"remove","lines":["    "]},{"start":{"row":235,"column":4},"end":{"row":235,"column":8},"action":"remove","lines":["    "]},{"start":{"row":235,"column":0},"end":{"row":235,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":235,"column":0},"end":{"row":236,"column":0},"action":"insert","lines":["",""],"id":80}],[{"start":{"row":236,"column":0},"end":{"row":245,"column":15},"action":"insert","lines":[" 3次元配列で、3つのドット絵を表示するループ","","for img in enemy_img:","    for line in img:","        for dot in line:","            if dot == 1:","                print(\"#\", end=\"\")","            else:","                print(\" \", end=\"\")","        print()"],"id":81}],[{"start":{"row":245,"column":15},"end":{"row":246,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":246,"column":0},"end":{"row":246,"column":8},"action":"insert","lines":["        "]},{"start":{"row":246,"column":8},"end":{"row":247,"column":0},"action":"insert","lines":["",""]},{"start":{"row":247,"column":0},"end":{"row":247,"column":8},"action":"insert","lines":["        "]},{"start":{"row":247,"column":8},"end":{"row":248,"column":0},"action":"insert","lines":["",""]},{"start":{"row":248,"column":0},"end":{"row":248,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":248,"column":4},"end":{"row":248,"column":8},"action":"remove","lines":["    "],"id":83},{"start":{"row":248,"column":0},"end":{"row":248,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":248,"column":0},"end":{"row":287,"column":15},"action":"insert","lines":["","# 3次元リストでドット絵を表示する","","enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],","              [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],","              [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],","             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],","              [1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],","              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]],","             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],","              [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],","              [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]],","             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],","              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],","              [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],","              [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],","              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],","              [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],","              [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]]]","","for img in enemy_img:","    for line in img:","        for dot in line:","            if dot == 1:","                print(\"#\", end=\"\")","            else:","                print(\" \", end=\"\")","        print()"],"id":84}],[{"start":{"row":280,"column":21},"end":{"row":281,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":281,"column":0},"end":{"row":281,"column":4},"action":"insert","lines":["    "]},{"start":{"row":281,"column":4},"end":{"row":281,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":281,"column":5},"end":{"row":281,"column":6},"action":"insert","lines":[" "],"id":86}],[{"start":{"row":281,"column":6},"end":{"row":281,"column":7},"action":"insert","lines":["へ"],"id":87}],[{"start":{"row":281,"column":7},"end":{"row":281,"column":8},"action":"insert","lines":["\b"],"id":88}],[{"start":{"row":281,"column":7},"end":{"row":281,"column":8},"action":"remove","lines":["\b"],"id":89},{"start":{"row":281,"column":6},"end":{"row":281,"column":7},"action":"remove","lines":["へ"]}],[{"start":{"row":281,"column":6},"end":{"row":281,"column":13},"action":"insert","lines":["配列を取り出す"],"id":90}],[{"start":{"row":282,"column":19},"end":{"row":282,"column":20},"action":"remove","lines":[":"],"id":91},{"start":{"row":282,"column":19},"end":{"row":283,"column":0},"action":"insert","lines":["",""]},{"start":{"row":283,"column":0},"end":{"row":283,"column":4},"action":"insert","lines":["    "]},{"start":{"row":283,"column":4},"end":{"row":283,"column":5},"action":"insert","lines":[" "]},{"start":{"row":283,"column":5},"end":{"row":283,"column":6},"action":"insert","lines":["#"]}],[{"start":{"row":283,"column":6},"end":{"row":283,"column":7},"action":"insert","lines":[" "],"id":92}],[{"start":{"row":283,"column":7},"end":{"row":283,"column":16},"action":"insert","lines":["1行ずつ取り出す「"],"id":93}],[{"start":{"row":283,"column":15},"end":{"row":283,"column":16},"action":"remove","lines":["「"],"id":94}],[{"start":{"row":284,"column":24},"end":{"row":285,"column":0},"action":"insert","lines":["",""],"id":95},{"start":{"row":285,"column":0},"end":{"row":285,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":285,"column":12},"end":{"row":285,"column":13},"action":"insert","lines":["#"],"id":96}],[{"start":{"row":285,"column":13},"end":{"row":285,"column":14},"action":"insert","lines":[" "],"id":97}],[{"start":{"row":285,"column":14},"end":{"row":285,"column":26},"action":"insert","lines":["各行から1行ずつ取り出す"],"id":98}],[{"start":{"row":290,"column":15},"end":{"row":291,"column":0},"action":"insert","lines":["",""],"id":99},{"start":{"row":291,"column":0},"end":{"row":291,"column":8},"action":"insert","lines":["        "]},{"start":{"row":291,"column":8},"end":{"row":292,"column":0},"action":"insert","lines":["",""]},{"start":{"row":292,"column":0},"end":{"row":292,"column":8},"action":"insert","lines":["        "]},{"start":{"row":292,"column":8},"end":{"row":293,"column":0},"action":"insert","lines":["",""]},{"start":{"row":293,"column":0},"end":{"row":293,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":293,"column":4},"end":{"row":293,"column":8},"action":"remove","lines":["    "],"id":100},{"start":{"row":293,"column":0},"end":{"row":293,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":293,"column":0},"end":{"row":322,"column":9},"action":"insert","lines":["","letters = [[[0,0,1,1,0,0],","             [0,1,0,0,1,0],","             [1,0,0,0,0,1],","             [1,1,1,1,1,1],","             [1,0,0,0,0,1],","             [1,0,0,0,0,1]],","            [[1,1,1,1,1,0],","             [1,0,0,0,0,1],","             [1,1,1,1,1,0],","             [1,0,0,0,0,1],","             [1,0,0,0,0,1],","             [1,1,1,1,1,0]],","            [[0,1,1,1,1,0],","             [1,0,0,0,0,1],","             [1,0,0,0,0,0],","             [1,0,0,0,0,0],","             [1,0,0,0,0,1],","             [0,1,1,1,1,0]]]","","# ここに、ドットを表示するコードを記述する","for img in letters:","  for line in img:","    for dot in line:","        if dot == 1:","            print(\"@\", end=\"\")","        else:","            print(\" \", end=\"\")","    print()","  print()"],"id":102}],[{"start":{"row":322,"column":9},"end":{"row":323,"column":0},"action":"insert","lines":["",""],"id":104},{"start":{"row":323,"column":0},"end":{"row":323,"column":2},"action":"insert","lines":["  "]},{"start":{"row":323,"column":2},"end":{"row":324,"column":0},"action":"insert","lines":["",""]},{"start":{"row":324,"column":0},"end":{"row":324,"column":2},"action":"insert","lines":["  "]},{"start":{"row":324,"column":2},"end":{"row":325,"column":0},"action":"insert","lines":["",""]},{"start":{"row":325,"column":0},"end":{"row":325,"column":2},"action":"insert","lines":["  "]}],[{"start":{"row":325,"column":1},"end":{"row":325,"column":2},"action":"remove","lines":[" "],"id":105}],[{"start":{"row":325,"column":1},"end":{"row":331,"column":11},"action":"insert","lines":[" 2次元配列で地図を作成・表示する","","landmap = [[\"森\" for i in range(20)] for j in range(10)]","for line in landmap:","    for area in line:","        print(area, end=\"\")","    print()"],"id":106}],[{"start":{"row":331,"column":11},"end":{"row":332,"column":0},"action":"insert","lines":["",""],"id":107},{"start":{"row":332,"column":0},"end":{"row":332,"column":4},"action":"insert","lines":["    "]},{"start":{"row":332,"column":4},"end":{"row":333,"column":0},"action":"insert","lines":["",""]},{"start":{"row":333,"column":0},"end":{"row":333,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":333,"column":0},"end":{"row":333,"column":4},"action":"remove","lines":["    "],"id":108}],[{"start":{"row":333,"column":0},"end":{"row":339,"column":11},"action":"insert","lines":[" 行番号を表示する","","for i,line in enumerate(landmap):","    print(str(i) + \":\", end=\"\")","    for area in line:","        print(area, end=\"\")","    print()"],"id":109}],[{"start":{"row":339,"column":11},"end":{"row":340,"column":0},"action":"insert","lines":["",""],"id":110},{"start":{"row":340,"column":0},"end":{"row":340,"column":4},"action":"insert","lines":["    "]},{"start":{"row":340,"column":4},"end":{"row":341,"column":0},"action":"insert","lines":["",""]},{"start":{"row":341,"column":0},"end":{"row":341,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":341,"column":0},"end":{"row":341,"column":4},"action":"remove","lines":["    "],"id":111},{"start":{"row":340,"column":4},"end":{"row":341,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":340,"column":4},"end":{"row":341,"column":0},"action":"insert","lines":["",""],"id":112},{"start":{"row":341,"column":0},"end":{"row":341,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":341,"column":0},"end":{"row":341,"column":4},"action":"remove","lines":["    "],"id":113}],[{"start":{"row":341,"column":0},"end":{"row":354,"column":11},"action":"insert","lines":["# coding: utf-8","# Your code here!","","# 2次元リストで地図を表示する","","landmap = [[\"森\" for i in range(20)] for j in range(10)]","landmap[0][0] = \"城\"","landmap[0][19] = \"町\"","landmap[9][19] = \"町\"","for i,line in enumerate(landmap):","    print(str(i) + \":\", end=\"\")","    for area in line:","        print(area, end=\"\")","    print()"],"id":114}],[{"start":{"row":354,"column":11},"end":{"row":355,"column":0},"action":"insert","lines":["",""],"id":115},{"start":{"row":355,"column":0},"end":{"row":355,"column":4},"action":"insert","lines":["    "]},{"start":{"row":355,"column":4},"end":{"row":356,"column":0},"action":"insert","lines":["",""]},{"start":{"row":356,"column":0},"end":{"row":356,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":356,"column":0},"end":{"row":356,"column":4},"action":"remove","lines":["    "],"id":116}],[{"start":{"row":356,"column":0},"end":{"row":364,"column":0},"action":"insert","lines":["text = [\"吾輩は猫である\",","        \"名前はまだ無い\",","        \"どこで生まれたか\",","        \"とんと見当がつかぬ\"]","","#ここに、行番号を表示するコードを記述する","for i,line in  enumerate(text):","    print(str(i + 1) + \":\" + line)",""],"id":117}],[{"start":{"row":364,"column":0},"end":{"row":365,"column":0},"action":"insert","lines":["",""],"id":118},{"start":{"row":365,"column":0},"end":{"row":366,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":366,"column":0},"end":{"row":376,"column":8},"action":"insert","lines":[" AND(論理積)について","ANDは、両方の条件が成立した場合、全体の条件が成立します。","全てが不成立、どれか1つでも不成立の場合には、不成立となります。","Pythonでは、「and」と記述します。","","","条件Ａ\t条件Ｂ\t全体","不成立\t不成立\t不成立","成立\t不成立\t不成立","不成立\t成立\t不成立","成立\t成立\t成立"],"id":119}],[{"start":{"row":376,"column":8},"end":{"row":377,"column":0},"action":"insert","lines":["",""],"id":120},{"start":{"row":377,"column":0},"end":{"row":378,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":378,"column":0},"end":{"row":388,"column":8},"action":"insert","lines":[" OR(論理和)について","ORは、どれか１つの条件が成立した場合、全体の条件が成立します。","全てが不成立の場合には、不成立となります。","Pythonでは、「or」と記述します。","","","条件Ａ\t条件Ｂ\t全体","不成立\t不成立\t不成立","成立\t不成立\t成立","不成立\t成立\t成立","成立\t成立\t成立"],"id":121}],[{"start":{"row":377,"column":0},"end":{"row":378,"column":0},"action":"insert","lines":["",""],"id":122},{"start":{"row":378,"column":0},"end":{"row":379,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":390,"column":8},"end":{"row":391,"column":0},"action":"insert","lines":["",""],"id":123},{"start":{"row":391,"column":0},"end":{"row":392,"column":0},"action":"insert","lines":["",""]},{"start":{"row":392,"column":0},"end":{"row":393,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":393,"column":0},"end":{"row":399,"column":11},"action":"insert","lines":[" 2次元配列で地図を表示する","","landmap = [[\"森\" for i in range(20)] for j in range(10)]","for line in landmap:","    for area in line:","        print(area, end=\"\")","    print()"],"id":124}],[{"start":{"row":399,"column":11},"end":{"row":400,"column":0},"action":"insert","lines":["",""],"id":125},{"start":{"row":400,"column":0},"end":{"row":400,"column":4},"action":"insert","lines":["    "]},{"start":{"row":400,"column":4},"end":{"row":401,"column":0},"action":"insert","lines":["",""]},{"start":{"row":401,"column":0},"end":{"row":401,"column":4},"action":"insert","lines":["    "]},{"start":{"row":401,"column":4},"end":{"row":402,"column":0},"action":"insert","lines":["",""]},{"start":{"row":402,"column":0},"end":{"row":402,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":402,"column":0},"end":{"row":402,"column":4},"action":"remove","lines":["    "],"id":126},{"start":{"row":401,"column":4},"end":{"row":402,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":401,"column":4},"end":{"row":402,"column":0},"action":"insert","lines":["",""],"id":127},{"start":{"row":402,"column":0},"end":{"row":402,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":402,"column":0},"end":{"row":402,"column":4},"action":"remove","lines":["    "],"id":128}],[{"start":{"row":402,"column":0},"end":{"row":417,"column":11},"action":"insert","lines":["城と町を配置して、道でつなぐ","道は、行が2で割り切れるか、列が3で割り切れる場合で、そこが「森」の時に配置する。","","","landmap = [[\"森\" for i in range(20)] for j in range(10)]","landmap[0][0] = \"城\"","landmap[0][19] = \"町\"","landmap[9][19] = \"町\"","for i,line in enumerate(landmap):","    print(str(i) + \":\", end=\"\")","    for j,area in enumerate(line):","        if (i % 2 == 0 or j % 3 == 0) and area == \"森\":","            print(\"＋\", end=\"\")","        else:","            print(area, end=\"\")","    print()"],"id":129}],[{"start":{"row":417,"column":11},"end":{"row":418,"column":0},"action":"insert","lines":["",""],"id":130},{"start":{"row":418,"column":0},"end":{"row":418,"column":4},"action":"insert","lines":["    "]},{"start":{"row":418,"column":4},"end":{"row":419,"column":0},"action":"insert","lines":["",""]},{"start":{"row":419,"column":0},"end":{"row":419,"column":4},"action":"insert","lines":["    "]},{"start":{"row":419,"column":4},"end":{"row":420,"column":0},"action":"insert","lines":["",""]},{"start":{"row":420,"column":0},"end":{"row":420,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":420,"column":0},"end":{"row":420,"column":4},"action":"remove","lines":["    "],"id":131}],[{"start":{"row":420,"column":0},"end":{"row":438,"column":11},"action":"insert","lines":["このチャプターで作成したコード","","# coding: utf-8","# Your code here!","","# 2次元リストで地図を表示する","","landmap = [[\"森\" for i in range(20)] for j in range(10)]","landmap[0][0] = \"城\"","landmap[0][19] = \"町\"","landmap[9][19] = \"町\"","for i,line in enumerate(landmap):","    print(str(i) + \":\", end=\"\")","    for j,area in enumerate(line):","        if (i % 2 == 0 or j % 3 == 0) and area == \"森\":","            print(\"＋\", end=\"\")","        else:","            print(area, end=\"\")","    print()"],"id":132}],[{"start":{"row":438,"column":11},"end":{"row":439,"column":0},"action":"insert","lines":["",""],"id":133},{"start":{"row":439,"column":0},"end":{"row":439,"column":4},"action":"insert","lines":["    "]},{"start":{"row":439,"column":4},"end":{"row":440,"column":0},"action":"insert","lines":["",""]},{"start":{"row":440,"column":0},"end":{"row":440,"column":4},"action":"insert","lines":["    "]},{"start":{"row":440,"column":4},"end":{"row":441,"column":0},"action":"insert","lines":["",""]},{"start":{"row":441,"column":0},"end":{"row":441,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":441,"column":0},"end":{"row":441,"column":4},"action":"remove","lines":["    "],"id":134}],[{"start":{"row":441,"column":0},"end":{"row":457,"column":1},"action":"insert","lines":["landmap = [[\"森\" for i in range(19)] for j in range(10)]","landmap[2][9] = \"城\"","landmap[0][0] = \"町\"","landmap[0][18] = \"町\"","landmap[9][0] = \"町\"","landmap[9][18] = \"町\"","","# 地図に道を作る","for i, line in enumerate(landmap):","    for j, area in enumerate(line):","        # ここから足りないところを入力してください","        if (i % 9 == 0 or j % 9 == 0) and area == \"森\":","            print(\"＋\", end=\"\")","        else:","            print(area, end=\"\")","    print()"," "],"id":136}],[{"start":{"row":457,"column":1},"end":{"row":458,"column":0},"action":"insert","lines":["",""],"id":137},{"start":{"row":458,"column":0},"end":{"row":458,"column":1},"action":"insert","lines":[" "]},{"start":{"row":458,"column":1},"end":{"row":459,"column":0},"action":"insert","lines":["",""]},{"start":{"row":459,"column":0},"end":{"row":459,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":459,"column":1},"end":{"row":468,"column":1},"action":"insert","lines":[" 標準入力するデータ","","0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0","1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1","1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1","1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1","0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0","0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0","0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1","_"],"id":138}],[{"start":{"row":468,"column":1},"end":{"row":469,"column":0},"action":"insert","lines":["",""],"id":139},{"start":{"row":469,"column":0},"end":{"row":470,"column":0},"action":"insert","lines":["",""]},{"start":{"row":470,"column":0},"end":{"row":471,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":471,"column":0},"end":{"row":478,"column":0},"action":"insert","lines":["標準入力から _ までの入力を読み込む","","while True:","    line = input()","    if line == \"_\":","        break","    print(line)",""],"id":140}],[{"start":{"row":478,"column":0},"end":{"row":479,"column":0},"action":"insert","lines":["",""],"id":141},{"start":{"row":479,"column":0},"end":{"row":480,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":480,"column":0},"end":{"row":486,"column":26},"action":"insert","lines":[" カンマで分割する","","while True:","    line = input()","    if line == \"_\":","        break","    print(line.split(\",\"))"],"id":142}],[{"start":{"row":486,"column":26},"end":{"row":487,"column":0},"action":"insert","lines":["",""],"id":143},{"start":{"row":487,"column":0},"end":{"row":487,"column":4},"action":"insert","lines":["    "]},{"start":{"row":487,"column":4},"end":{"row":488,"column":0},"action":"insert","lines":["",""]},{"start":{"row":488,"column":0},"end":{"row":488,"column":4},"action":"insert","lines":["    "]},{"start":{"row":488,"column":4},"end":{"row":489,"column":0},"action":"insert","lines":["",""]},{"start":{"row":489,"column":0},"end":{"row":489,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":489,"column":0},"end":{"row":489,"column":4},"action":"remove","lines":["    "],"id":144}],[{"start":{"row":489,"column":0},"end":{"row":504,"column":11},"action":"insert","lines":["標準入力から読み込んだ2次元配列のドット絵を表示する","","enemy_img = []","while True:","    line = input()","    if line == \"_\":","        break","    enemy_img.append(line.split(\",\"))","","for line in enemy_img:","    for dot in line:","        if int(dot) == 1:","            print(\"#\", end=\"\")","        else:","            print(\" \", end=\"\")","    print()"],"id":145}],[{"start":{"row":504,"column":11},"end":{"row":505,"column":0},"action":"insert","lines":["",""],"id":146},{"start":{"row":505,"column":0},"end":{"row":505,"column":4},"action":"insert","lines":["    "]},{"start":{"row":505,"column":4},"end":{"row":506,"column":0},"action":"insert","lines":["",""]},{"start":{"row":506,"column":0},"end":{"row":506,"column":4},"action":"insert","lines":["    "]},{"start":{"row":506,"column":4},"end":{"row":507,"column":0},"action":"insert","lines":["",""]},{"start":{"row":507,"column":0},"end":{"row":507,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":507,"column":0},"end":{"row":507,"column":4},"action":"remove","lines":["    "],"id":147}],[{"start":{"row":507,"column":0},"end":{"row":529,"column":11},"action":"insert","lines":["このチャプターで作成したコード","","# coding: utf-8","# Your code here!","","# 標準入力から2次元リスト","","enemy_img = []","while True:","    line = input()","    if line == \"_\":","        break","    enemy_img.append(line.split(\",\"))","","# print(enemy_img)","","for line in enemy_img:","    for dot in line:","        if int(dot) == 1:","            print(\"#\", end=\"\")","        else:","            print(\" \", end=\"\")","    print()"],"id":148}],[{"start":{"row":529,"column":11},"end":{"row":530,"column":0},"action":"insert","lines":["",""],"id":149},{"start":{"row":530,"column":0},"end":{"row":530,"column":4},"action":"insert","lines":["    "]},{"start":{"row":530,"column":4},"end":{"row":531,"column":0},"action":"insert","lines":["",""]},{"start":{"row":531,"column":0},"end":{"row":531,"column":4},"action":"insert","lines":["    "]},{"start":{"row":531,"column":4},"end":{"row":532,"column":0},"action":"insert","lines":["",""]},{"start":{"row":532,"column":0},"end":{"row":532,"column":4},"action":"insert","lines":["    "]},{"start":{"row":532,"column":4},"end":{"row":533,"column":0},"action":"insert","lines":["",""]},{"start":{"row":533,"column":0},"end":{"row":533,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":533,"column":0},"end":{"row":533,"column":4},"action":"remove","lines":["    "],"id":150}],[{"start":{"row":533,"column":0},"end":{"row":563,"column":17},"action":"insert","lines":["# coding: utf-8","# Your code here!","","# 2次元リストで画像を配置","","# 画像用リスト","players_img = [","    \"https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Empty.png\",","    \"https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Dragon.png\",","    \"https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Crystal.png\",","    \"https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Hero.png\",","    \"https://paiza-webapp.s3.amazonaws.com/files/learning/rpg/Heroine.png\"]","","# 配置データを読み込み","team = []","while True:","    line = input()","    if line == \"_\":","        break","    team.append(line.split(\",\"))","# print(team)","","# 配置に合わせて表示","print(\"<table>\")","for line in team:","    print(\"<tr>\")","    #print(line)","    for person in line:","        print(\"<td><img src='\" + players_img[int(person)] + \"'></td>\")","    print(\"</tr>\")","print(\"</table>\")"],"id":151}]]},"ace":{"folds":[],"scrolltop":8341,"scrollleft":0,"selection":{"start":{"row":563,"column":17},"end":{"row":563,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":520,"state":"start","mode":"ace/mode/python"}},"timestamp":1628729034415,"hash":"cd4cf0c63749f15de9b394d7c2160fe400e86e43"}