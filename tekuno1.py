input_line = gets.chomp.split("")
# gets = 変数input _lineに「getsによる標準入力」
# chomp = 末尾の連続する改行コードを全て取り除きます
# split = 文字列を指定した区切り文字で分割し、配列で返すメソッド
input_line.each {|word|
# each文で繰り返し処理
# 変数input＿lineをブロック変数wordに代入
    case word
     #  一つの値に対して複数の候補の中で一致するものを探すような場合には「case」文を使用
     when "A"
     # thenは省略可能
        print "4"
     when "E"
        print "3"
     when "G"
        print "6"
     when "I"
        print "1"
     when "O"
        print "0"
     when "S"
        print "5"
     when "Z"
        print "2"
    else
        print word
    end    
}



s = input()
m = {'A':'4', 'E':'3', 'G':'6', 'I':'1', 'O':'0', 'S':'5','Z':'2'}

t = s.translate(str.maketrans(m))
# 複数の文字を変換したいときは「str.translate()」
# maketrans（）メソッドは文字のマッピング変換テーブルを作成するために使用
print(t)