vowel = 'aeiouAEIOU'
name = 'Torvalds'
cname = ''.join(s for s in name if s not in vowel)
print(cname)  # Trvlds


n = 0
input_line = gets.chomp
str = ["a", "e", "i", "o", "u"]
5.times do
 
    input_line = input_line.delete(str[n])
    n += 1
end
puts input_line






n = 0
input_line = gets.chomp
str = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
10.times do
    input_line = input_line.delete(str[n])
    n += 1
end
puts input_line