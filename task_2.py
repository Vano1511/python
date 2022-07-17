
lines = 0
words = 0
file = open('new.txt', 'r')
for line in file:
    lines += 1
    word = line.split()
    words += len(word)
file.close()
print(lines)
print(words)