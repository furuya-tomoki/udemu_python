{"filter":false,"title":"paiza10.py","tooltip":"/paiza10.py","ace":{"folds":[],"scrolltop":2498.5,"scrollleft":0,"selection":{"start":{"row":176,"column":4},"end":{"row":176,"column":4},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":155,"state":"start","mode":"ace/mode/python"}},"hash":"e1bb1c9b9fa2a63047fe0e760b3571f42d494ad5","mime":"text/x-script.python","undoManager":{"mark":37,"position":37,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":12},"action":"insert","lines":["print(\"start\")","a = 1","print(b)","print(\"end\")"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":13},"action":"insert","lines":["例外処理の概要を理解しよう"],"id":3}],[{"start":{"row":5,"column":12},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":9,"column":0},"end":{"row":17,"column":12},"action":"insert","lines":["print(1)","try:","    number = 0","    answer = 100 / number","    print(answer)","except ZeroDivisionError as e:","    print(e)","finally:","    print(2)"],"id":7}],[{"start":{"row":17,"column":12},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "],"id":9}],[{"start":{"row":19,"column":0},"end":{"row":32,"column":0},"action":"insert","lines":["import traceback, sys","","print(1)","try:","    number = 0","    answer = 100 / number","    print(answer)","except ZeroDivisionError as e:","    print(\"0では割り算できません\")","    # print(traceback.format_exc())","    sys.stderr.write(traceback.format_exc())","finally:","    print(2)",""],"id":10}],[{"start":{"row":17,"column":12},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "]},{"start":{"row":18,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["",""]},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":19,"column":4},"end":{"row":20,"column":0},"action":"insert","lines":["",""]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""]},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":38,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["# coding: utf-8","# 例外メッセージを指定しよう","import sys","enemies = [\"スライム\", \"ドラゴン\", \"魔王\"]","","try:","    number = 0","    print(\"勇者は敵に遭遇した\")","    print(\"勇者は\" + enemies[2 / number] + \"と戦った\")","except ZeroDivisionError as e:","    sys.stderr.write(\"その敵は表示できません\")","finally:","    print(\"勇者は勝利した\")",""],"id":13}],[{"start":{"row":51,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":14},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"insert","lines":["",""]},{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":54,"column":0},"end":{"row":63,"column":12},"action":"insert","lines":["print(1)","try:","    number = 1","    answer = 100 / number","    print(answer2)","except NameError as e:","    print(\"未定義の変数を呼び出しています\")","    print(e)","finally:","    print(2)"],"id":15}],[{"start":{"row":63,"column":12},"end":{"row":64,"column":0},"action":"insert","lines":["",""],"id":16},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":4},"end":{"row":65,"column":0},"action":"insert","lines":["",""]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]},{"start":{"row":65,"column":4},"end":{"row":66,"column":0},"action":"insert","lines":["",""]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"insert","lines":["    "]},{"start":{"row":66,"column":4},"end":{"row":67,"column":0},"action":"insert","lines":["",""]},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":4},"end":{"row":68,"column":0},"action":"insert","lines":["",""]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"remove","lines":["    "],"id":17}],[{"start":{"row":68,"column":0},"end":{"row":80,"column":0},"action":"insert","lines":["import sys","","enemies = [\"スライム\", \"ドラゴン\", \"魔王\"]","","try:","    number1 = 0","    print(\"勇者は敵に遭遇した\")","    print(\"勇者は\" + enemies[number2] + \"と戦った\")","except NameError as e:","    sys.stderr.write(\"未定義の変数を呼び出しています\")","finally:","    print(\"勇者は勝利した\")",""],"id":18}],[{"start":{"row":80,"column":0},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":19},{"start":{"row":81,"column":0},"end":{"row":82,"column":0},"action":"insert","lines":["",""]},{"start":{"row":82,"column":0},"end":{"row":83,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":83,"column":0},"end":{"row":98,"column":12},"action":"insert","lines":["print(1)","try:","    number = 0","    answer = 100 / number","    print(answer2)","except Exception as e:","    print(\"予期せぬエラーが発生しました\")","    print(e)","except ZeroDivisionError as e:","    print(\"0では割り算できません\")","    print(e)","except NameError as e:","    print(\"未定義の変数を呼び出しています\")","    print(e)","finally:","    print(2)"],"id":20}],[{"start":{"row":98,"column":12},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":99,"column":4},"end":{"row":100,"column":0},"action":"insert","lines":["",""]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":100,"column":4},"end":{"row":101,"column":0},"action":"insert","lines":["",""]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"remove","lines":["    "],"id":22}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":15},"action":"insert","lines":["未定義の変数を呼び出しています"],"id":23}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":15},"action":"remove","lines":["未定義の変数を呼び出しています"],"id":24}],[{"start":{"row":101,"column":0},"end":{"row":119,"column":0},"action":"insert","lines":["# coding: utf-8","# 例外の種類を変更しよう その２","","import sys","","enemies = [\"スライム\", \"ドラゴン\", \"魔王\"]","","try:","    number1 = 0","    print(\"勇者は敵に遭遇した\")","    print(\"勇者は\" + enemies[number2] + \"と戦った\")","except ZeroDivisionError as e:","    sys.stderr.write(\"その敵は表示できません\")","except NameError as e:","    sys.stderr.write(\"未定義の変数を呼び出しています\")","","finally:","    print(\"勇者は勝利した\")",""],"id":25}],[{"start":{"row":119,"column":0},"end":{"row":120,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":120,"column":0},"end":{"row":121,"column":0},"action":"insert","lines":["",""]},{"start":{"row":121,"column":0},"end":{"row":122,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":122,"column":0},"end":{"row":138,"column":0},"action":"insert","lines":["# coding: utf-8","# 間違い探し","","import sys","","print(\"Hello World\")","","try:","    raise ZeroDivisionError(\"強制エラー\")","except NameError as e:","    sys.stderr.write(\"未定義の変数を呼び出しています\")","except ZeroDivisionError as e:","    sys.stderr.write(\"0では割り算はできません\")","","finally:","    print(\"Hello Python3\")",""],"id":28}],[{"start":{"row":138,"column":0},"end":{"row":139,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":139,"column":0},"end":{"row":140,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":140,"column":0},"end":{"row":159,"column":0},"action":"insert","lines":["def test_exception(number):","    print(2)","    try:","        print(3)","        answer = 100 / number","        return answer","        print(4)","    except ZeroDivisionError as e:","        print(5)","        raise e","    print(6)","","print(1)","try:","    answer = test_exception(0)","    print(7)","except ZeroDivisionError as e:","    print(8)","    print(e)",""],"id":30}],[{"start":{"row":139,"column":0},"end":{"row":140,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":140,"column":0},"end":{"row":141,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":161,"column":0},"end":{"row":162,"column":0},"action":"insert","lines":["",""],"id":32},{"start":{"row":162,"column":0},"end":{"row":163,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":163,"column":0},"end":{"row":173,"column":35},"action":"insert","lines":["import sys","","","def calc():","    return 100 / 0","","","try:","    print(calc())","except ZeroDivisionError as e:","    sys.stderr.write(\"0で割り算はできません\")"],"id":33}],[{"start":{"row":161,"column":0},"end":{"row":162,"column":0},"action":"insert","lines":["",""],"id":34}],[{"start":{"row":165,"column":0},"end":{"row":166,"column":0},"action":"remove","lines":["",""],"id":35}],[{"start":{"row":173,"column":35},"end":{"row":174,"column":0},"action":"insert","lines":["",""],"id":36},{"start":{"row":174,"column":0},"end":{"row":174,"column":4},"action":"insert","lines":["    "]},{"start":{"row":174,"column":4},"end":{"row":175,"column":0},"action":"insert","lines":["",""]},{"start":{"row":175,"column":0},"end":{"row":175,"column":4},"action":"insert","lines":["    "]},{"start":{"row":175,"column":4},"end":{"row":176,"column":0},"action":"insert","lines":["",""]},{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":176,"column":4},"end":{"row":196,"column":34},"action":"insert","lines":["# coding: utf-8","# 呼び出し元へ例外を伝えよう","","import sys","","def test_exception(number):","    try:","        return 100 / number","","    except ZeroDivisionError as e:","        raise e","","    finally:","        print(\"処理が終了しました\")","","","try:","    test_exception(0)","","except ZeroDivisionError as e:","    sys.stderr.write(\"0で割り算できません\")"],"id":37}],[{"start":{"row":175,"column":4},"end":{"row":176,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":176,"column":0},"end":{"row":176,"column":4},"action":"insert","lines":["    "]},{"start":{"row":176,"column":4},"end":{"row":177,"column":0},"action":"insert","lines":["",""]},{"start":{"row":177,"column":0},"end":{"row":177,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":177,"column":0},"end":{"row":198,"column":34},"action":"remove","lines":["    ","    # coding: utf-8","# 呼び出し元へ例外を伝えよう","","import sys","","def test_exception(number):","    try:","        return 100 / number","","    except ZeroDivisionError as e:","        raise e","","    finally:","        print(\"処理が終了しました\")","","","try:","    test_exception(0)","","except ZeroDivisionError as e:","    sys.stderr.write(\"0で割り算できません\")"],"id":39}],[{"start":{"row":177,"column":0},"end":{"row":197,"column":34},"action":"insert","lines":["# coding: utf-8","# 呼び出し元へ例外を伝えよう","","import sys","","def test_exception(number):","    try:","        return 100 / number","","    except ZeroDivisionError as e:","        raise e","","    finally:","        print(\"処理が終了しました\")","","","try:","    test_exception(0)","","except ZeroDivisionError as e:","    sys.stderr.write(\"0で割り算できません\")"],"id":40}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["# "],"id":41},{"start":{"row":2,"column":0},"end":{"row":2,"column":2},"action":"insert","lines":["# "]},{"start":{"row":3,"column":0},"end":{"row":3,"column":2},"action":"insert","lines":["# "]},{"start":{"row":4,"column":0},"end":{"row":4,"column":2},"action":"insert","lines":["# "]},{"start":{"row":5,"column":0},"end":{"row":5,"column":2},"action":"insert","lines":["# "]},{"start":{"row":9,"column":0},"end":{"row":9,"column":2},"action":"insert","lines":["# "]},{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "]},{"start":{"row":11,"column":0},"end":{"row":11,"column":2},"action":"insert","lines":["# "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":2},"action":"insert","lines":["# "]},{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "]},{"start":{"row":14,"column":0},"end":{"row":14,"column":2},"action":"insert","lines":["# "]},{"start":{"row":15,"column":0},"end":{"row":15,"column":2},"action":"insert","lines":["# "]},{"start":{"row":16,"column":0},"end":{"row":16,"column":2},"action":"insert","lines":["# "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":2},"action":"insert","lines":["# "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":2},"action":"insert","lines":["# "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":2},"action":"insert","lines":["# "]},{"start":{"row":25,"column":0},"end":{"row":25,"column":2},"action":"insert","lines":["# "]},{"start":{"row":26,"column":0},"end":{"row":26,"column":2},"action":"insert","lines":["# "]},{"start":{"row":27,"column":0},"end":{"row":27,"column":2},"action":"insert","lines":["# "]},{"start":{"row":28,"column":0},"end":{"row":28,"column":2},"action":"insert","lines":["# "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":2},"action":"insert","lines":["# "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":2},"action":"insert","lines":["# "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":2},"action":"insert","lines":["# "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":2},"action":"insert","lines":["# "]},{"start":{"row":33,"column":0},"end":{"row":33,"column":2},"action":"insert","lines":["# "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":2},"action":"insert","lines":["# "]},{"start":{"row":38,"column":0},"end":{"row":38,"column":2},"action":"insert","lines":["# "]},{"start":{"row":39,"column":0},"end":{"row":39,"column":2},"action":"insert","lines":["# "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":2},"action":"insert","lines":["# "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":2},"action":"insert","lines":["# "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":2},"action":"insert","lines":["# "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":2},"action":"insert","lines":["# "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":2},"action":"insert","lines":["# "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":2},"action":"insert","lines":["# "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":2},"action":"insert","lines":["# "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":2},"action":"insert","lines":["# "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":2},"action":"insert","lines":["# "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":2},"action":"insert","lines":["# "]},{"start":{"row":54,"column":0},"end":{"row":54,"column":2},"action":"insert","lines":["# "]},{"start":{"row":55,"column":0},"end":{"row":55,"column":2},"action":"insert","lines":["# "]},{"start":{"row":56,"column":0},"end":{"row":56,"column":2},"action":"insert","lines":["# "]},{"start":{"row":57,"column":0},"end":{"row":57,"column":2},"action":"insert","lines":["# "]},{"start":{"row":58,"column":0},"end":{"row":58,"column":2},"action":"insert","lines":["# "]},{"start":{"row":59,"column":0},"end":{"row":59,"column":2},"action":"insert","lines":["# "]},{"start":{"row":60,"column":0},"end":{"row":60,"column":2},"action":"insert","lines":["# "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":2},"action":"insert","lines":["# "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":2},"action":"insert","lines":["# "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":2},"action":"insert","lines":["# "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":2},"action":"insert","lines":["# "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":2},"action":"insert","lines":["# "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":2},"action":"insert","lines":["# "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":2},"action":"insert","lines":["# "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":2},"action":"insert","lines":["# "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":2},"action":"insert","lines":["# "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":2},"action":"insert","lines":["# "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":2},"action":"insert","lines":["# "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":2},"action":"insert","lines":["# "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["# "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":2},"action":"insert","lines":["# "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":2},"action":"insert","lines":["# "]},{"start":{"row":85,"column":0},"end":{"row":85,"column":2},"action":"insert","lines":["# "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":2},"action":"insert","lines":["# "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"insert","lines":["# "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":2},"action":"insert","lines":["# "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"insert","lines":["# "]},{"start":{"row":90,"column":0},"end":{"row":90,"column":2},"action":"insert","lines":["# "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":2},"action":"insert","lines":["# "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":2},"action":"insert","lines":["# "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":2},"action":"insert","lines":["# "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":2},"action":"insert","lines":["# "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":2},"action":"insert","lines":["# "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":2},"action":"insert","lines":["# "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":2},"action":"insert","lines":["# "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":2},"action":"insert","lines":["# "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":2},"action":"insert","lines":["# "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":2},"action":"insert","lines":["# "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":2},"action":"insert","lines":["# "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":2},"action":"insert","lines":["# "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":2},"action":"insert","lines":["# "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":2},"action":"insert","lines":["# "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":2},"action":"insert","lines":["# "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":2},"action":"insert","lines":["# "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":2},"action":"insert","lines":["# "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":2},"action":"insert","lines":["# "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":2},"action":"insert","lines":["# "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":2},"action":"insert","lines":["# "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":2},"action":"insert","lines":["# "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":2},"action":"insert","lines":["# "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":2},"action":"insert","lines":["# "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":2},"action":"insert","lines":["# "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":2},"action":"insert","lines":["# "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":2},"action":"insert","lines":["# "]},{"start":{"row":129,"column":0},"end":{"row":129,"column":2},"action":"insert","lines":["# "]},{"start":{"row":130,"column":0},"end":{"row":130,"column":2},"action":"insert","lines":["# "]},{"start":{"row":131,"column":0},"end":{"row":131,"column":2},"action":"insert","lines":["# "]},{"start":{"row":132,"column":0},"end":{"row":132,"column":2},"action":"insert","lines":["# "]},{"start":{"row":133,"column":0},"end":{"row":133,"column":2},"action":"insert","lines":["# "]},{"start":{"row":134,"column":0},"end":{"row":134,"column":2},"action":"insert","lines":["# "]},{"start":{"row":136,"column":0},"end":{"row":136,"column":2},"action":"insert","lines":["# "]},{"start":{"row":137,"column":0},"end":{"row":137,"column":2},"action":"insert","lines":["# "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":2},"action":"insert","lines":["# "]},{"start":{"row":143,"column":0},"end":{"row":143,"column":2},"action":"insert","lines":["# "]},{"start":{"row":144,"column":0},"end":{"row":144,"column":2},"action":"insert","lines":["# "]},{"start":{"row":145,"column":0},"end":{"row":145,"column":2},"action":"insert","lines":["# "]},{"start":{"row":146,"column":0},"end":{"row":146,"column":2},"action":"insert","lines":["# "]},{"start":{"row":147,"column":0},"end":{"row":147,"column":2},"action":"insert","lines":["# "]},{"start":{"row":148,"column":0},"end":{"row":148,"column":2},"action":"insert","lines":["# "]},{"start":{"row":149,"column":0},"end":{"row":149,"column":2},"action":"insert","lines":["# "]},{"start":{"row":150,"column":0},"end":{"row":150,"column":2},"action":"insert","lines":["# "]},{"start":{"row":151,"column":0},"end":{"row":151,"column":2},"action":"insert","lines":["# "]},{"start":{"row":152,"column":0},"end":{"row":152,"column":2},"action":"insert","lines":["# "]},{"start":{"row":154,"column":0},"end":{"row":154,"column":2},"action":"insert","lines":["# "]},{"start":{"row":155,"column":0},"end":{"row":155,"column":2},"action":"insert","lines":["# "]},{"start":{"row":156,"column":0},"end":{"row":156,"column":2},"action":"insert","lines":["# "]},{"start":{"row":157,"column":0},"end":{"row":157,"column":2},"action":"insert","lines":["# "]},{"start":{"row":158,"column":0},"end":{"row":158,"column":2},"action":"insert","lines":["# "]},{"start":{"row":159,"column":0},"end":{"row":159,"column":2},"action":"insert","lines":["# "]},{"start":{"row":160,"column":0},"end":{"row":160,"column":2},"action":"insert","lines":["# "]},{"start":{"row":164,"column":0},"end":{"row":164,"column":2},"action":"insert","lines":["# "]},{"start":{"row":166,"column":0},"end":{"row":166,"column":2},"action":"insert","lines":["# "]},{"start":{"row":167,"column":0},"end":{"row":167,"column":2},"action":"insert","lines":["# "]},{"start":{"row":170,"column":0},"end":{"row":170,"column":2},"action":"insert","lines":["# "]},{"start":{"row":171,"column":0},"end":{"row":171,"column":2},"action":"insert","lines":["# "]},{"start":{"row":172,"column":0},"end":{"row":172,"column":2},"action":"insert","lines":["# "]},{"start":{"row":173,"column":0},"end":{"row":173,"column":2},"action":"insert","lines":["# "]},{"start":{"row":177,"column":0},"end":{"row":177,"column":2},"action":"insert","lines":["# "]},{"start":{"row":178,"column":0},"end":{"row":178,"column":2},"action":"insert","lines":["# "]},{"start":{"row":180,"column":0},"end":{"row":180,"column":2},"action":"insert","lines":["# "]},{"start":{"row":182,"column":0},"end":{"row":182,"column":2},"action":"insert","lines":["# "]},{"start":{"row":183,"column":0},"end":{"row":183,"column":2},"action":"insert","lines":["# "]},{"start":{"row":184,"column":0},"end":{"row":184,"column":2},"action":"insert","lines":["# "]},{"start":{"row":186,"column":0},"end":{"row":186,"column":2},"action":"insert","lines":["# "]},{"start":{"row":187,"column":0},"end":{"row":187,"column":2},"action":"insert","lines":["# "]},{"start":{"row":189,"column":0},"end":{"row":189,"column":2},"action":"insert","lines":["# "]},{"start":{"row":190,"column":0},"end":{"row":190,"column":2},"action":"insert","lines":["# "]},{"start":{"row":193,"column":0},"end":{"row":193,"column":2},"action":"insert","lines":["# "]},{"start":{"row":194,"column":0},"end":{"row":194,"column":2},"action":"insert","lines":["# "]},{"start":{"row":196,"column":0},"end":{"row":196,"column":2},"action":"insert","lines":["# "]},{"start":{"row":197,"column":0},"end":{"row":197,"column":2},"action":"insert","lines":["# "]}]]},"timestamp":1628863198453}