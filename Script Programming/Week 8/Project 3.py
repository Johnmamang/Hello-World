import math

def newton(number):
    estimate = number / 2
    while True:
        new_estimate = (estimate + number / estimate) / 2
        if abs(new_estimate - estimate) < 0.0001:
            return new_estimate
        estimate = new_estimate

if __name__ == '__main__':
    while True:
        user_input = input("Enter a number to find its square root (press enter to quit): ")
        if not user_input:
            break
        number = float(user_input)
        if number < 0:
            print("Cannot find the square root of a negative number.")
        else:
            estimate = newton(number)
            print(f"The approximate square root of {number} is {estimate:.4f}.")
            print(f"The actual square root of {number} is {math.sqrt(number):.4f}.")
