import random
user_input = int(input("Guess a number between 1 and 10: "))
magic_number = random.randint(1,10)
if user_input == magic_number:
    print("Nice")
else:
    print("Not nice, it was %d" % (magic_number))