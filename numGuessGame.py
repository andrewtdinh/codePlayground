import random, sys

args = sys.argv
start = int(args[1]) if len(args) >= 2 else 1
stop = int(args[2]) if len(args) >= 3 else 10

numbers = list(range(start, stop + 1))
target = random.choice(numbers)
guess = int(input(f"Guess a number from {start} to {stop}, inclusive: "))
if guess == target:
  print("You are a genius!!")
else:
  print(f"Sorry, better lucky next time. The target was {target}.")

