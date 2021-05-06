day = int(input('Day (1-7)? '))
if day == 1 or day == 7:
    print("Sleep in")
elif day == 2 or day == 3 or day == 4 or day == 5 or day == 6:
    print("Go to work")
else:
    print("How many days are in a week again?")