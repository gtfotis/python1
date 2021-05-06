day = int(input('Day (1-7)? '))
if day-1 == 0:
    print("Sunday")
elif day-1 == 1:
    print("Monday")
elif day-1 == 2:
    print("Tuesday")
elif day-1 == 3:
    print("Humpday")
elif day-1 == 4:
    print("Thursday")
elif day-1 == 5:
    print("TGIFriday")
elif day-1 == 6:
    print("Saturday")
else:
    print("Not a valid day number")