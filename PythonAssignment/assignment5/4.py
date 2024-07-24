#4. Write a program to check if the input character is alphabet or not. and then it is vowel or consonant.
#if it is not an alphabet, then print whether it is a special character or a digit. if digit, even number or odd number. 

a = input()
if(a.isalpha()):
    print(a +" is alphabet");
    
    if(a =="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U"):
        print(a +" is Vowel")
    else:
        print(a +" is consonent")
else:
    if(a.isdigit()):
        print(a+ "it is digit")
        a=int(a)
        if(a%2==0):
            print(a + " even")
        else:
            print(a +" odd")
    else:
        print(a +" it is special character")


input 1 : 3
o/p --> 3 is digit
        3 odd

input 2: w
o/p     w is alphabet
        w is consonent

input 3: e
  o/p     e is alphabet
          e is Vowel
