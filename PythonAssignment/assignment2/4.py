#. Write a progarm to convert the given number of days into years, months and days. 

d = int(input())
years = d/365
d = d%365
months = d/30
days = d%30

print(years)
print(int(months))
print(int(days))
