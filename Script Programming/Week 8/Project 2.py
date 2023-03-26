import math

def newton(number):
   
    estimate = number / 2
    while True:
        new_estimate = (estimate + number / estimate) / 2
        if abs(new_estimate - estimate) < 0.0001:
            return new_estimate
        estimate = new_estimate

if __name__ == '__main__':
    number = float(input("Enter a number to find its square root: "))
    if number < 0:
        print("Cannot find the square root of a negative number.")
    else:
        estimate = newton(number)
        print(f"Your approximate square root of {number} is {estimate:.4f}.")
        print(f"The actual square root of {number} is {math.sqrt(number):.4f}.")
