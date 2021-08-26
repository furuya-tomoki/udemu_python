n = gets.chomp
  r = n.chars.each_slice(1).map(&:join).reverse.join.to_i
puts (r)