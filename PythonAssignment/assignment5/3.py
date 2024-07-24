#3. Write a program to find the leap year or not, without using the calendar module. 

year = int(input())

if(year%4==0) and(year%100!=0 or year%400==0):
  print("YES")
else:
  print("NO")
