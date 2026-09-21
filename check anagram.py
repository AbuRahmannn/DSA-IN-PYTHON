str = "cat"
sample = "act"

if len(str) != len(sample):
    print("Not an anagram")
else:
    for i in str:
        if i not in sample:
            print("Not an anagram")
            break
    else:
        print("Is an anagram")