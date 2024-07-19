2. Create a each of the below data types and perform various operations that can be performed on it. 
a. String 
b. List 
c. Tuple
d. Dictionary 
e. Set
Various operations such as, concatenation, multiplication, index accessing, negative indexing, etc.


1.String = collection of words.There are different functions in string to perform.("")

Concatenation = +,join(),%,format
Method 1  --->     perform addition by "+"
      a = "Sri"
      b ="varshini"
      print(a+b)
      # output = Srivarshini
Method 2------>   Using format() function
      a = "sri"
      b="varshini"
      print("{}{}".format(a,b))
Method 3------>  Using join()
      print("".join([a,b]))


Multiplication = 
a = "sri"
print(a*3)

indexAccessing
a = "home"
print(a[0])
#h

negative Indexing
print(a[-1])
#e
------------------------------------------------------------ <=============================== >------------------------------------------------------------------
2..List = can store homogenous data types[]

Concentation 
a=[1,2,3]
b = [3,4,5]
print(a+b)
#-->[1,2,3,3,4,5]

Multiplication


indexaccessing
a=a.index(2)
print(a)
# 1

negative indexing
--------------------------------------------------------------------------------<<<<<<===============>>>>>>>>>>>>>>>>-----------------
3.Tuple = ordered collection of elements  ,immutable data type -->()
Concatenation
a=(1,2,3)
b =(0,1,2)
print(a+b)
#(1,2,3,0,1,2)

Indexing
a=(1,2,3)
b =(0,1,2)
print(a.index(2))
=================================================================================<<<<<<<<<<<<<<<<<===>>>>>>>>>>>>>>>>>======================
4.Dictionary = {},contain key:value pairs

a={"k":1,"r":2}
print(a.keys())#{'k','r}
print(a.items())#{'k',1,'r',2}
print(a.values())#{1,2}

=========================================================================================================================================
5.Set{} ,no duplicate
a ={1,2,3}
b={3,4,5}

print(a.union(b))
#{1,2,3,4,5}

##no indexing 






            
