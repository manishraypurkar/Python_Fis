#positional argument,keyword and variable length argument
from setuptools import sic


def Hello(name,*n):  #*n variable length argument by default tuple data type if u used **n take Dictonary data type
    print("Hello",name,n)

Hello("manish","good afternoon!")#positional argument
Hello(name="manish from keyword argument")#keyword argument

#variables

value="hello" #global variable

def hello():
    valuelocal=" world" #local variable
    print(value+valuelocal)

hello()
#print(valuelocal)  local variable not accessible ouside block or acccessible using global keyword

#lambda keyword and function

square=lambda a:a*a
print(square(5))
print(square(7))

#exception handling

try:
    a,b=[int(i) for i in input("enter two nos:").split(',')]
    print("division is:",a/b)
except ZeroDivisionError:
    print("divide by zero error")
except:print("handled any exception")      #defualt exception handling
finally:print("always executed!")

#cmdline argument

import sys

temp=0
for i in sys.argv:
    temp=temp+1
    print(temp,i)

print("Length of cmd-line argument is:",len(sys.argv))
