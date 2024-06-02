1. Write a program to find the roots of a quadratic equation. ax^2 + bx + c = 0

a = int(input())
b = int(input())
c = int(input())

d = b*b - 4*a*c
if d>0:
  w = (-b+4*a*c*0.5)/2*a
  w = (-b-4*a*c*0.5)/2*a
  print(w)
elif d==0:
  w = -b/2*a
  print(w)
else:
  print("Imaginary numbers")
