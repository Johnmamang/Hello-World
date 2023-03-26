import turtle
import math

#This function is used to draw a circle
def drawCircle(t, x, y, radius):
    """Draws a circle with the given turtle t, center point (x, y),
    and radius."""
    
    circumference = 2.0 * math.pi * radius  # calculate the circumference of the circle
    step = circumference / 120.0  # calculate the distance to move for each segment
    
    t.up()
    t.goto(x + radius, y)  # move turtle to starting point on circumference
    t.setheading(90)  # point turtle in the direction of the top of the circle
    t.down()
    
    for _ in range(120):  # draw the circle's circumference
        t.forward(step)
        t.left(3)
        
def main():
    t = turtle.Turtle()
    drawCircle(t, 40, 75, 100)

#Call the main function
if __name__ == '__main__':
    main()
