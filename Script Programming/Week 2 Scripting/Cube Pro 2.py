#Name:Cubic Calculation Project 2

#User input
sideLength = int(input("What is the length of one side of your cube?"))

#side and surface areas calculation
sideArea = sideLength ** 2
surfaceArea = sideArea * 6

#display the surface area
print("The surface area of the cube is", surfaceArea, \
      "cubic units.")
