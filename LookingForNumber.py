
import random

print("We'll play a game? Find the number from 1 to 10. Remember! You only have 3 chances!")
number = int(random.randint(1,10))
steps = 3

while True:
    enter = input("\n enter the number from 1 to 10: ")
    steps = steps - 1
    if number == int(enter):
        print("Congratulations, you get it!")
        break
    else:
        print("keep trying, you still have to " + str(steps) + " attemps")
        if int(enter) > number:
            print("lower")
        if int(enter) < number:
            print("more")
    if steps <= 0:
        print("Unfortunately, this was your last chance. Play again")
        break
print("Are You won?")


git init