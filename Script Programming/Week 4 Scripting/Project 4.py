#Calculation
def total_distance(height, bounces):
    total_distance = height
    for i in range(bounces):
        height = height * 0.6
        total_distance += 2 * height
    return total_distance

# Height and bounce input
initial_height = float(input("Enter the initial height from which the ball is dropped (in feet): "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))

#result and print
result = total_distance(initial_height, bounces)
print("The total distance traveled by the ball is:", result, "feet")
