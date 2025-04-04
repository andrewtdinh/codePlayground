import random, sys

args = sys.argv
start = int(args[1]) if len(args) >= 2 else 1
stop = int(args[2]) if len(args) >= 3 else 10

numbers = list(range(start, stop + 1))
target = random.choice(numbers)
guess = None
tries = 5
while tries > 0 and guess != target:
  guess = int(input(f"Guess a number from {start} to {stop}, inclusive: "))
  if guess == target:
    print("You are a genius!!")
    break
  elif tries == 1:
    print("Sorry, that's not it.  You are out of tries!")
    break
  else:
    print(f"Sorry, better luck on the next guess.")
    tries -= 1

