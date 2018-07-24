def is_pangram(phrase):
    c = 0
    a = "abcdefghijklmnopqrstuvwxyz"
    phraseLetters = ""
    for char in phrase:
        for letter in a:
            if char == letter and char not in phraseLetters:
                phraseLetters += char
    for char in phraseLetters:
        for letter in a:
            if char == letter:
                c += 1
    if c == 26:
        print yes
        return True
    else:
        print phraseLetters, a
        print no
        return False

print is_pangram(myPhrase)
