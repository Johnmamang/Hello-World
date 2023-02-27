#define right triangle
def is_right_triangle(a, b, c):
  if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    return True
  else:
    return False

#User input for all 3 lengths
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

#if else statements
if is_right_triangle(a, b, c):
  print("The triangle is a right triangle.")
else:
  print("The triangle is not a right triangle.")
