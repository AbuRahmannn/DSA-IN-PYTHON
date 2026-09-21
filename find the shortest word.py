str = "hello world python"
words = str.split()
min = words[0]
for i in range(len(words)):
    if len(words[i]) < len(min):
        min = words[i]
print(min)