import math


# calculate square root numbers
def estimateRoot(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    #Estimate and return the result
    while True:
        # finding next estimate
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break
    return estimate


def main():
    # looping
    while True:
        # User input
        x = input("Enter a postive number or (simply enter to quit): ")
        try:
            #floating
            x = float(x)
            print("Your program's estimate is", estimateRoot(x))
            print("Python's estimate is ", math.sqrt(x))
        except:
            break

if __name__ == '__main__':
    main()
