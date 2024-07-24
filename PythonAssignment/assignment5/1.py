#5. Control flow -- Conditional statements
# Explore about if, elif, else statements, and the nested conditions. 
 #1. if - it is used to print the statement wheather the condition is true or false

ex:=

a = 10
if(a<20):
  print("true")

o/p = true


#2.elif - It is the other condition to check if it is not satisfy by if statement

a = 8
if(a>10):
  print("may be above 10");
elif (a<10):
  print("may be below 10")

o/p = may be below 10

#3. else - It is end condition if is not satistify with if and elif condition then it will moves to else condition

a= 20
if(a<10):
  print("less than 10")
elif (a=10):
  print("equal to 10")
else:
  print("greater than 10")

o/p= greater then 10

#Nested - if or if-else statements that are placed inside other if or else statements

gender = "M"
if gender == "M":
  print("You're a man.")
else: 
  if gender == "F":
    print("You're a woman.")
  else:
    print("I'm sorry, but I can't identify.")

o/p = You're a man
