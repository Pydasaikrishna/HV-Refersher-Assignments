##=================Default inputs================
import pandas as pd

set1 = pd.Series([1,3,5,7,9])
set2 = pd.Series([2,4,6,8,10])

add = (set1+set2)
sub = (set1-set2)
mul = (set1*set2)
div = (set1/set2)
mod = (set1%set2)

print("Addition of two numbers: ")
print(add)
print("subtraction of two numbers: ")
print(sub)
print("Multiplication of two numbers: ")
print(mul)
print("Division of two numbers: ")
print(div)
print("Modulation of two numbers: ")
print(mod)







##====================User inputs====================
import pandas as pd

x=pd.Series([int(input("Enter the First Numbers: "))for i in range(3)])
y=pd.Series([int(input("Enter the Second Number: "))for i in range(3)])

print("Adding of two numbers are: ")
print(x+y)
print("Subtraction of two numbers are: ")
print(x-y)
print("Multiplication of two numbers are: ")
print(x*y)
print("Division of two numbers are: ")
print(x/y)
print("Modulation of two numbers are: ")
print(x%y)

