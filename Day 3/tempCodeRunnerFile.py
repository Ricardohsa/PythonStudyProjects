year = int(input("Which year do you want to check year\n"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 5) == 0:
            print("Leap year.")
    else:
        print("Not a leap year.")    
else:
    print("Not a leap year.")