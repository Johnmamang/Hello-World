#define equilateral
def is_equilateral(a, b, c):
  if a == b and b == c:
    return True
  else:
    return False

#User input for all three sides
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

#if else statemets
if is_equilateral(a, b, c):
  print("The triangle is equilateral.")
else:
  print("The triangle is not equilateral.")
