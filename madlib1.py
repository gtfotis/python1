print("Please fill in the blanks below:")
print("_(name)_'s favorite video game is _(subject)_.")
user_name = input("What is your name? ")
favorite_game = input("What is your favorite game? ")
length_of_name = len(user_name)
length_of_game = len(favorite_game)
if length_of_name > 0 and length_of_game >0:
    print("%s's favorite game is %s." % (user_name, favorite_game))
else:
    print("Well that was rude, I'll ask later I guess :(")