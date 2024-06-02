#5. Calculate the area and circumference of a circle, taking the diameter of the circle as an input from the console. 

diameter = int(input())# d is twice radius
radius = d/2 #radius is half od diameter
pi = 3.14
Area = pi*radius*radius
C= 2*pi*radius

print("Area of circle :",Area)
print("Circumstance of circle: ",C)
