s1 = input("Please enter a word:")
s2 = input("Please enter another word:")

for i in range(0, len(s1), 1):
    if i in range (0, len(s2), 1):
        print("its anagram")
