from random import choice


questions = ["Why am i here?", "How many people lives on earth?","Where is haven?"]
a = "just because"
q = choice(questions)
b = input(q).strip().lower()
print(b)
while a != b:
    print("But Why? ")
    b = input("").strip().lower()


print("Fine")
