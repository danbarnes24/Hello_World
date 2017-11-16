import random

place = ["World" , "New York" , "Aunt Sally" , "Planet Earth" , "Nurse"]

Greetings = ["Hello" , "Hi" , "What's Up" , "Salutations" , "plz respond"]

i = 0

def sentence() :
    print(random.choice(Greetings) + ' ' + random.choice(place))

def main() :
    while i < 10:
        i = i + 1
        sentence()
