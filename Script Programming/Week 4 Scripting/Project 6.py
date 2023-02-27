#leibniz pi calculation
def leibniz_pi(n):
    pi = 0
    for i in range(n):
        pi += (-1)**i / (2 * i + 1)
    return 4 * pi

#Input from the user
n = int(input("Enter the number of iterations: "))

#approximation 
approximation = leibniz_pi(n)

#Print 
print("The approximation of pi after", n, "iterations is:", approximation)
