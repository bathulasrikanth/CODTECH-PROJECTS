import math 
import numpy
from colorama import Fore,Back,Style

print(10*" ",Fore.RED,"SMIPLE CALCULATOR",Style.RESET_ALL)
print(Fore.GREEN,''' 1. SUM
          2. MULTIPLICATION
          3. DIVISION
          4. FACTORIAL''',Style.RESET_ALL)
def add():
    l=[]
    n=int(input("Enter the no. of values: "))
    for i in range(n):
        i=int(input("enter the value: "))
        l.append(i)
    return "sum of numbers is: ",sum(l) 
def mul():
    l=[]
    k=1
    n=int(input("Enter the no. of values: "))
    for i in range(n):
        i=int(input("enter the value: "))
        l.append(i)
        k=k*i
    return "Multiplication of Numbers is: ",k 

def div():
    numerator=int(input("enter the numerator:  "))
    denominator=int(input("enter the denominator: "))
    if denominator!=0:
        a=numerator/denominator
        return "The ans is: ",round(a,2)  
    else:
        return "ERROR --  'The Denominator is Zero-(0)'"    

def factorial(n):
    if n==0 or n==1:
        return 1 
    elif n<0:
        return "The entered Number is less than zero: enter the correct value. "    
    else:
        fact=n*factorial(n-1)
        return fact
    

option=int(input("enter the option: "))
if option==1:
    print(add())
elif option==2:
    print(mul())
elif option==3:
    print(div())
elif option==4:
    n=int(input("enter the n value:  "))
    print(factorial(n))    


