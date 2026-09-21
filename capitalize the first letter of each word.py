str = "hello world python"
words = str.split()
for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1::]
print(words)