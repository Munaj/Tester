
orginal = input("Enter a sentence: ").lower().strip()
words = orginal.split()
vowels = ["a","i","e","o","u","y"]
new_words = []
for x in words:
    if x[0] in vowels:
        new_word = x +"yay"
        new_words.append(new_word )
    else:
        vowel_pos = 0
        for letter in x:
            if letter not in vowels:
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = x[:vowel_pos]
        the_rest = x[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
