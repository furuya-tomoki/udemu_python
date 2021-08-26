n = gets.chomp
# 変数nに「gets、chomp」メソッドを定義
# chompを付けると改行をなくす


# loopを使えば、breakでループを終了させない限りループし続ける処理
loop {
  r = n.chars.each_slice(1).map(&:join).reverse.join.to_i
  # charsメソッド = 使用すると1文字ずつ分割
  # each_slice = 項目ごとにグループ化してから処理を行いたい
  # joinメソッド = 配列の要素を結合して一つの文字列とする
  # reverse = 要素を行区順に並べた配列を生成
  n = n.to_i
  # 数値型に変換するメソッド
  if n == r
    puts r
  break
  else 
n += r
  end
  n = n.to_s
  # 文字列に変換するメソッド
}

# 入力例1
# 261
# 出力例1
# 747
# 入力例2
# 1000
# 出力例2
# 1001