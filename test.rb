n = 0
input_line = gets.chomp
str = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
10.times do
    input_line = input_line.delete(str[n])
    n += 1
end
puts input_line