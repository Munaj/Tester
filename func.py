
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

print(add(1,2,3,4,5))

def about(name, age, likes):
    sentence = f"Meet {name}! They are {age} years old and they like {likes}."
    return sentence
dictionary = {"name":"Jakub","age":22,"likes":"Python"}

print(about(**dictionary))

def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

foo(huda = "Female",jakub = "male")
