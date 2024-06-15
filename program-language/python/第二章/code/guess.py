import random

rng = random.randint(0, 100)
# print('random number is ', rng)
x = int(input("Please enter an integer:"))
limit = 6

while x != rng:
    if x > 100 or x < 0:
        x = int(input("Ignore invalid integer, input again:"))
        continue

    if rng < x:
        print('Bigger')
    elif rng > x:
        print('Smaller')
    if limit == 0:
        print("Quota exhaust")
        break

    x = int(input("Try again:"))
    limit -= 1
else:
    print('Correct')
