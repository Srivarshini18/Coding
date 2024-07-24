#5. Write a program to count the minimum number of notes for a given amount. 

a = int(input())

Five_H_n = int(a/500)
two_h_n  = int(a%500/200)
one_h_n= int(a%500%200/100)
Fity_n = int(a%500%200%100/50)
two_n = int(a%500%200%100%50/20)
ten_n = int(a%500%200%100%50%20/10)

print((Five_H_n))
print((two_h_n))
print((one_h_n))
print((Fity_n))
print((two_n))
print((ten_n))
