#!/usr/bin/python
number = 5
running = True
while running:
    guess = int(input("Enter an integer:"))
    if guess==number:
        print("Yes!")
        running = False
    elif guess<number:
        print("It's a little higher than that")
    else:
        print("It's a little lower than that")
else:
    print("Loop is over")
print("Done")
