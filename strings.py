word = "supercalifragilisticexpialidocious"


# slices string_name[start:end(not included):step(optional)]
print(word[::-1])#reverse string

#basic string slicing
#index 5 up to 9
print(word[5:9])
print(word[5:9:1])
#5 to end
print(word[5:])
#5 to end with steps
print(word[5::2])
#start up tp 5
print(word[:5])
#index counting from end
print(word[-2])


print(word[word.index("cali"):word.index("frag")])
print(word[word.index("doci"):])
