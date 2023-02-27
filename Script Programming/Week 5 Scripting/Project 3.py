import math

print("Think of a number between 1 and 100 and I'll try to guess it.")
print("After each guess, tell me if the number is higher, lower, or correct.")

lower_bound = 1
upper_bound = 100

number_of_guesses = int(math.log2(upper_bound - lower_bound + 1)) + 1

for i in range(number_of_guesses):
  guess = (lower_bound + upper_bound) // 2
  print(f"My guess is {guess}. Is the number higher, lower, or correct?")
  response = input()
  if response == "higher":
    lower_bound = guess + 1
  elif response == "lower":
    upper_bound = guess - 1
  elif response == "correct":
    print(f"I got it in {i+1} guesses!")
    break
  else:
    print("Invalid response. Please enter higher, lower, or correct.")
