day = int(input('Day (1-7)? '))
if day-1 == 0 or day-1 == 6:
    print("Sleep in")
elif day-1 == 1 or day-1 == 2 or day-1 == 3 or day-1 == 4 or day-1 == 5:
    print("Go to work")
else:
    print("How many days are in a week again?")