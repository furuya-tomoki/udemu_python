{"filter":false,"title":"paiza9.py","tooltip":"/paiza9.py","undoManager":{"mark":67,"position":67,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":17},"action":"insert","lines":["class Box:","    def __init__(self, item):","        self.item = item","","    def open(self):","        print(\"宝箱を開いた。\" + self.item + \"を手に入れた。\")","","class JewelryBox(Box):","    def look(self):","        print(\"宝箱はキラキラと輝いている。\")","","box = Box(\"鋼鉄の剣\")","box.open()","","jewelrybox = JewelryBox(\"魔法の指輪\")","jewelrybox.look()","jewelrybox.open()"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":69},"action":"insert","lines":[" ＃02:クラスを継承する ","ここでは、クラスの継承ついて学習します。例として、RPGで使うアイテムが入る宝箱クラスを作り、そこから宝石箱クラスを継承で作ってみましょう"],"id":3}],[{"start":{"row":19,"column":17},"end":{"row":20,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""]},{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":22,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["class Greeting:","    def __init__(self):","        self.msg = \"hello\"","        self.target = \"paiza\"","","class Hello(Greeting):","    # この下に、say_helloメソッドを記述する","    def say_hello(self):","        print(self.msg + \" \" + self.target)","    ","player = Hello()","player.say_hello()",""],"id":5}],[{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"insert","lines":["",""]},{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":37,"column":0},"end":{"row":60,"column":15},"action":"insert","lines":["メソッドのオーバーライドとは","オーバーライドを利用すると、スーパークラスが持つメソッドを、サブクラスで書き換えて再定義することができます。","","","class Box:","    def __init__(self, item):","        self.item = item","","    def open(self):","        print(\"宝箱を開いた。\" + self.item + \"を手に入れた。\")","","class MagicBox(Box):","    def look(self):","        print(\"宝箱は、妖しく輝いている。\")","","    def open(self):","        print(\"宝箱を開いた。\" + self.item + \"が襲ってきた！\")","","box = Box(\"鋼鉄の剣\")","box.open()","","magicbox = MagicBox(\"モノマネモンスター\")","magicbox.look()","magicbox.open()"],"id":7}],[{"start":{"row":60,"column":15},"end":{"row":61,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":61,"column":0},"end":{"row":62,"column":0},"action":"insert","lines":["",""]},{"start":{"row":62,"column":0},"end":{"row":63,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":63,"column":0},"end":{"row":79,"column":0},"action":"insert","lines":["class Greeting:","    def __init__(self):","        self.msg = \"hello\"","        self.target = \"paiza\"","","    def say_hello(self):","        print(self.msg + \" \" + self.target)","","class Hello(Greeting):","    # ここにオーバライドするメソッドを記述する","    def say_hello(self, target):","        print(self.msg + \" \" + self.target)","","","player = Hello()","player.say_hello(\"python\")",""],"id":9}],[{"start":{"row":74,"column":35},"end":{"row":74,"column":36},"action":"remove","lines":["."],"id":10},{"start":{"row":74,"column":34},"end":{"row":74,"column":35},"action":"remove","lines":["f"]},{"start":{"row":74,"column":33},"end":{"row":74,"column":34},"action":"remove","lines":["l"]},{"start":{"row":74,"column":32},"end":{"row":74,"column":33},"action":"remove","lines":["e"]},{"start":{"row":74,"column":31},"end":{"row":74,"column":32},"action":"remove","lines":["s"]}],[{"start":{"row":74,"column":38},"end":{"row":75,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":75,"column":0},"end":{"row":75,"column":8},"action":"insert","lines":["        "]},{"start":{"row":75,"column":8},"end":{"row":75,"column":9},"action":"insert","lines":[" "]},{"start":{"row":75,"column":9},"end":{"row":75,"column":10},"action":"insert","lines":["#"]}],[{"start":{"row":75,"column":10},"end":{"row":75,"column":11},"action":"insert","lines":[" "],"id":12},{"start":{"row":75,"column":11},"end":{"row":75,"column":12},"action":"insert","lines":["s"]},{"start":{"row":75,"column":12},"end":{"row":75,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":75,"column":13},"end":{"row":75,"column":14},"action":"insert","lines":["l"],"id":13},{"start":{"row":75,"column":14},"end":{"row":75,"column":15},"action":"insert","lines":["f"]},{"start":{"row":75,"column":15},"end":{"row":75,"column":16},"action":"insert","lines":["."]},{"start":{"row":75,"column":16},"end":{"row":75,"column":17},"action":"insert","lines":["t"]},{"start":{"row":75,"column":17},"end":{"row":75,"column":18},"action":"insert","lines":["a"]},{"start":{"row":75,"column":18},"end":{"row":75,"column":19},"action":"insert","lines":["r"]}],[{"start":{"row":75,"column":19},"end":{"row":75,"column":20},"action":"insert","lines":["g"],"id":14},{"start":{"row":75,"column":20},"end":{"row":75,"column":21},"action":"insert","lines":["e"]},{"start":{"row":75,"column":21},"end":{"row":75,"column":22},"action":"insert","lines":["t"]}],[{"start":{"row":75,"column":22},"end":{"row":75,"column":24},"action":"insert","lines":["だと"],"id":15}],[{"start":{"row":75,"column":24},"end":{"row":75,"column":26},"action":"insert","lines":["[]"],"id":16}],[{"start":{"row":75,"column":26},"end":{"row":76,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":76,"column":0},"end":{"row":76,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":76,"column":8},"end":{"row":76,"column":9},"action":"remove","lines":[" "],"id":18},{"start":{"row":76,"column":4},"end":{"row":76,"column":8},"action":"remove","lines":["    "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"remove","lines":["    "]},{"start":{"row":75,"column":26},"end":{"row":76,"column":0},"action":"remove","lines":["",""]},{"start":{"row":75,"column":25},"end":{"row":75,"column":26},"action":"remove","lines":["]"]},{"start":{"row":75,"column":24},"end":{"row":75,"column":25},"action":"remove","lines":["["]}],[{"start":{"row":75,"column":11},"end":{"row":75,"column":12},"action":"insert","lines":["「"],"id":21}],[{"start":{"row":75,"column":23},"end":{"row":75,"column":24},"action":"insert","lines":["」"],"id":22}],[{"start":{"row":75,"column":26},"end":{"row":75,"column":28},"action":"insert","lines":["「」"],"id":23}],[{"start":{"row":75,"column":27},"end":{"row":75,"column":28},"action":"insert","lines":["p"],"id":24},{"start":{"row":75,"column":28},"end":{"row":75,"column":29},"action":"insert","lines":["y"]},{"start":{"row":75,"column":29},"end":{"row":75,"column":30},"action":"insert","lines":["t"]},{"start":{"row":75,"column":30},"end":{"row":75,"column":31},"action":"insert","lines":["h"]},{"start":{"row":75,"column":31},"end":{"row":75,"column":32},"action":"insert","lines":["o"]},{"start":{"row":75,"column":32},"end":{"row":75,"column":33},"action":"insert","lines":["n"]}],[{"start":{"row":75,"column":34},"end":{"row":75,"column":35},"action":"insert","lines":["が"],"id":25}],[{"start":{"row":75,"column":35},"end":{"row":75,"column":42},"action":"insert","lines":["入る場所がない"],"id":26}],[{"start":{"row":75,"column":42},"end":{"row":75,"column":44},"action":"insert","lines":["ので"],"id":27},{"start":{"row":75,"column":44},"end":{"row":75,"column":46},"action":"insert","lines":["「」"]}],[{"start":{"row":75,"column":45},"end":{"row":75,"column":46},"action":"insert","lines":["t"],"id":28},{"start":{"row":75,"column":46},"end":{"row":75,"column":47},"action":"insert","lines":["a"]},{"start":{"row":75,"column":47},"end":{"row":75,"column":48},"action":"insert","lines":["r"]},{"start":{"row":75,"column":48},"end":{"row":75,"column":49},"action":"insert","lines":["g"]},{"start":{"row":75,"column":49},"end":{"row":75,"column":50},"action":"insert","lines":["e"]},{"start":{"row":75,"column":50},"end":{"row":75,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":75,"column":52},"end":{"row":75,"column":53},"action":"insert","lines":["で"],"id":29}],[{"start":{"row":75,"column":53},"end":{"row":75,"column":57},"action":"insert","lines":["定義づる"],"id":30}],[{"start":{"row":75,"column":56},"end":{"row":75,"column":57},"action":"remove","lines":["る"],"id":31},{"start":{"row":75,"column":55},"end":{"row":75,"column":56},"action":"remove","lines":["づ"]}],[{"start":{"row":75,"column":55},"end":{"row":75,"column":57},"action":"insert","lines":["する"],"id":32}],[{"start":{"row":79,"column":26},"end":{"row":80,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":80,"column":0},"end":{"row":81,"column":0},"action":"insert","lines":["",""]},{"start":{"row":81,"column":0},"end":{"row":82,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":82,"column":0},"end":{"row":100,"column":0},"action":"insert","lines":["# メソッドをオーバーライドしよう2","","class Greeting:","    def __init__(self):","        self.msg = \"hello\"","        self.target = \"paiza\"","    ","    def say_hello(self):","        print(self.msg + \" \" + self.target)","","class Hello(Greeting):","    def say_hello(self):","        print(self.msg + \" \" + self.target)","        print(\"YEAH YEAH YEAH!\")","","","player = Greeting()","player.say_hello()",""],"id":34}],[{"start":{"row":98,"column":19},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":35},{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"insert","lines":[" "]},{"start":{"row":99,"column":1},"end":{"row":99,"column":2},"action":"insert","lines":["#"]}],[{"start":{"row":98,"column":16},"end":{"row":98,"column":17},"action":"remove","lines":["g"],"id":36},{"start":{"row":98,"column":15},"end":{"row":98,"column":16},"action":"remove","lines":["n"]},{"start":{"row":98,"column":14},"end":{"row":98,"column":15},"action":"remove","lines":["i"]},{"start":{"row":98,"column":13},"end":{"row":98,"column":14},"action":"remove","lines":["t"]},{"start":{"row":98,"column":12},"end":{"row":98,"column":13},"action":"remove","lines":["e"]},{"start":{"row":98,"column":11},"end":{"row":98,"column":12},"action":"remove","lines":["e"]},{"start":{"row":98,"column":10},"end":{"row":98,"column":11},"action":"remove","lines":["r"]},{"start":{"row":98,"column":9},"end":{"row":98,"column":10},"action":"remove","lines":["G"]}],[{"start":{"row":98,"column":9},"end":{"row":98,"column":10},"action":"insert","lines":["H"],"id":37},{"start":{"row":98,"column":10},"end":{"row":98,"column":11},"action":"insert","lines":["e"]},{"start":{"row":98,"column":11},"end":{"row":98,"column":12},"action":"insert","lines":["l"]},{"start":{"row":98,"column":12},"end":{"row":98,"column":13},"action":"insert","lines":["l"]},{"start":{"row":98,"column":13},"end":{"row":98,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":99,"column":2},"end":{"row":99,"column":3},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":99,"column":3},"end":{"row":99,"column":5},"action":"insert","lines":["[]"],"id":39}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"remove","lines":["]"],"id":40},{"start":{"row":99,"column":3},"end":{"row":99,"column":4},"action":"remove","lines":["["]}],[{"start":{"row":99,"column":3},"end":{"row":99,"column":7},"action":"insert","lines":["「」「」"],"id":41}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["G"],"id":42},{"start":{"row":99,"column":5},"end":{"row":99,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":99,"column":6},"end":{"row":99,"column":7},"action":"insert","lines":["e"],"id":43},{"start":{"row":99,"column":7},"end":{"row":99,"column":8},"action":"insert","lines":["e"]},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["t"]},{"start":{"row":99,"column":9},"end":{"row":99,"column":10},"action":"insert","lines":["i"]},{"start":{"row":99,"column":10},"end":{"row":99,"column":11},"action":"insert","lines":["n"]},{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["g"]}],[{"start":{"row":99,"column":13},"end":{"row":99,"column":15},"action":"insert","lines":["から"],"id":44}],[{"start":{"row":99,"column":16},"end":{"row":99,"column":17},"action":"insert","lines":["H"],"id":45},{"start":{"row":99,"column":17},"end":{"row":99,"column":18},"action":"insert","lines":["e"]},{"start":{"row":99,"column":18},"end":{"row":99,"column":19},"action":"insert","lines":["l"]},{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":["l"]},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":99,"column":22},"end":{"row":99,"column":23},"action":"insert","lines":["に"],"id":46}],[{"start":{"row":99,"column":23},"end":{"row":99,"column":31},"action":"insert","lines":["変更するだけで、"],"id":47}],[{"start":{"row":99,"column":31},"end":{"row":99,"column":39},"action":"insert","lines":["出力結果も変わる"],"id":48}],[{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":103,"column":0},"end":{"row":104,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":104,"column":0},"end":{"row":118,"column":25},"action":"insert","lines":["class Player:","    def __init__(self, name):","        self.name = name","","    def attack(self, enemy):","        print(self.name + \"は、\" + enemy + \"を攻撃した！\")","","print(\"=== パーティーでスライムと戦う ===\")","hero = Player(\"勇者\")","# hero.attack(\"スライム\")","warrior = Player(\"戦士\")","","party = [hero, warrior]","for member in party:","    member.attack(\"スライム\")"],"id":50}],[{"start":{"row":118,"column":25},"end":{"row":119,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":119,"column":0},"end":{"row":119,"column":4},"action":"insert","lines":["    "]},{"start":{"row":119,"column":4},"end":{"row":120,"column":0},"action":"insert","lines":["",""]},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"insert","lines":["    "]},{"start":{"row":120,"column":4},"end":{"row":121,"column":0},"action":"insert","lines":["",""]},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"insert","lines":["    "]},{"start":{"row":121,"column":4},"end":{"row":122,"column":0},"action":"insert","lines":["",""]},{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"remove","lines":["    "],"id":52}],[{"start":{"row":122,"column":0},"end":{"row":142,"column":25},"action":"insert","lines":["class Player:","    def __init__(self, name):","        self.name = name","","    def attack(self, enemy):","        print(self.name + \"は、\" + enemy + \"を攻撃した！\")","","class Wizard(Player):","    def attack(self, enemy):","        print(\"ズバーン！\")","        print(self.name + \"は、\" + enemy + \"に炎を放った！\")","","print(\"=== パーティーでスライムと戦う ===\")","hero = Player(\"勇者\")","# hero.attack(\"スライム\")","warrior = Player(\"戦士\")","wizard = Wizard(\"魔法使い\")","","party = [hero, warrior, wizard]","for member in party:","    member.attack(\"スライム\")"],"id":53}],[{"start":{"row":142,"column":25},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":143,"column":0},"end":{"row":143,"column":4},"action":"insert","lines":["    "]},{"start":{"row":143,"column":4},"end":{"row":144,"column":0},"action":"insert","lines":["",""]},{"start":{"row":144,"column":0},"end":{"row":144,"column":4},"action":"insert","lines":["    "]},{"start":{"row":144,"column":4},"end":{"row":145,"column":0},"action":"insert","lines":["",""]},{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":4},"action":"remove","lines":["    "],"id":55}],[{"start":{"row":145,"column":0},"end":{"row":167,"column":0},"action":"insert","lines":["# coding: utf-8","# RPGの攻撃シーン","","class Player:","    def __init__(self, name):","        self.name = name","","    def attack(self, enemy):","        print(self.name + \"は\" + enemy + \"を攻撃した\")","","class Warrior(Player):","    def attack(self, enemy):","        print(self.name + \"は\" + enemy + \"を猛攻撃した\")","","","team = []","team.append(Player(\"勇者\"))","team.append(Player(\"魔法使い\"))","team.append(Warrior(\"戦士\"))","","for person in team:","    person.attack(\"スライム\")",""],"id":56}],[{"start":{"row":167,"column":0},"end":{"row":168,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":168,"column":0},"end":{"row":169,"column":0},"action":"insert","lines":["",""]},{"start":{"row":169,"column":0},"end":{"row":170,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":170,"column":0},"end":{"row":198,"column":18},"action":"insert","lines":["class Player:","    def __init__(self, name):","        self.name = name","","    def attack(self, enemy):","        print(self.name + \"は、\" + enemy + \"を攻撃した！\")","","class Wizard(Player):","    def __init__(self):","        super().__init__(\"魔法使い\")","","    def attack(self, enemy):","        self.__spell()","        print(self.name + \"は、\" + enemy + \"に炎を放った！\")","","    def __spell(self):","        print(\"ズバーン！\")","","print(\"=== パーティーでスライムと戦う ===\")","hero = Player(\"勇者\")","# hero.attack(\"スライム\")","warrior = Player(\"戦士\")","wizard = Wizard()","","party = [hero, warrior, wizard]","for member in party:","    member.attack(\"スライム\")","","# wizard.__spell()"],"id":58}],[{"start":{"row":198,"column":18},"end":{"row":199,"column":0},"action":"insert","lines":["",""],"id":59},{"start":{"row":199,"column":0},"end":{"row":200,"column":0},"action":"insert","lines":["",""]},{"start":{"row":200,"column":0},"end":{"row":201,"column":0},"action":"insert","lines":["",""]},{"start":{"row":201,"column":0},"end":{"row":202,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":202,"column":0},"end":{"row":206,"column":29},"action":"insert","lines":[" Player.charactor_count += 1","","Player.charactor_count = Player.charactor_count + 1","","を、省略する記法です。「-=」「/=」なども使用できます。"],"id":60}],[{"start":{"row":206,"column":29},"end":{"row":207,"column":0},"action":"insert","lines":["",""],"id":61},{"start":{"row":207,"column":0},"end":{"row":208,"column":0},"action":"insert","lines":["",""]},{"start":{"row":208,"column":0},"end":{"row":209,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":209,"column":0},"end":{"row":210,"column":23},"action":"insert","lines":["クラス変数","オブジェクト間で共通して利用できる変数のこと。"],"id":62}],[{"start":{"row":210,"column":23},"end":{"row":211,"column":0},"action":"insert","lines":["",""],"id":63},{"start":{"row":211,"column":0},"end":{"row":212,"column":0},"action":"insert","lines":["",""]},{"start":{"row":212,"column":0},"end":{"row":213,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":213,"column":0},"end":{"row":216,"column":0},"action":"insert","lines":["クラスメソッド","オブジェクト間で共通して利用できるメソッドのこと。","動画では、2つの方法でクラスメソッドを作成しましたが、デコレータを使用する方法が推奨されています。",""],"id":64}],[{"start":{"row":216,"column":0},"end":{"row":217,"column":0},"action":"insert","lines":["",""],"id":65},{"start":{"row":217,"column":0},"end":{"row":218,"column":0},"action":"insert","lines":["",""]},{"start":{"row":218,"column":0},"end":{"row":219,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":219,"column":0},"end":{"row":228,"column":58},"action":"insert","lines":[" デコレータ","すでに定義されている関数に、新たに機能を追加できる仕組みのこと。","デコレータは、すでに用意されていたり、自分で作成したりすることができます。","","動画では、@classmethodを使用しました。","","","@classmethod","def summary(cls):","    print(str(Player.__charactor_count) + \"人で、スライムを攻撃した。\")"],"id":66}],[{"start":{"row":228,"column":58},"end":{"row":229,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":229,"column":0},"end":{"row":229,"column":4},"action":"insert","lines":["    "]},{"start":{"row":229,"column":4},"end":{"row":230,"column":0},"action":"insert","lines":["",""]},{"start":{"row":230,"column":0},"end":{"row":230,"column":4},"action":"insert","lines":["    "]},{"start":{"row":230,"column":4},"end":{"row":231,"column":0},"action":"insert","lines":["",""]},{"start":{"row":231,"column":0},"end":{"row":231,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":231,"column":4},"end":{"row":234,"column":30},"action":"insert","lines":["def summary(cls):","    print(str(Player.__charactor_count) + \"人で、スライムを攻撃した。\")","","summary = classmethod(summary)"],"id":68}],[{"start":{"row":234,"column":30},"end":{"row":235,"column":0},"action":"insert","lines":["",""],"id":69},{"start":{"row":235,"column":0},"end":{"row":236,"column":0},"action":"insert","lines":["",""]},{"start":{"row":236,"column":0},"end":{"row":237,"column":0},"action":"insert","lines":["",""]},{"start":{"row":237,"column":0},"end":{"row":238,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":238,"column":0},"end":{"row":248,"column":10},"action":"insert","lines":["from datetime import datetime, timedelta, timezone","","jst   = timezone(timedelta(hours=9))","today = datetime.now(jst)","print(today)","print(today.year)","print(today.month)","print(today.day)","","day = datetime.strptime(\"2030/01/10 06:02:19\", \"%Y/%m/%d %H:%M:%S\")","print(day)"],"id":70}]]},"ace":{"folds":[],"scrolltop":3410.5,"scrollleft":0,"selection":{"start":{"row":242,"column":12},"end":{"row":242,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":212,"state":"start","mode":"ace/mode/python"}},"timestamp":1628831150175,"hash":"9cbc867dd0c8c655ca3162d9ee49d2ae5fc48db9"}