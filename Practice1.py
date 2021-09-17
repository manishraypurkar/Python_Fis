print("hello world!")

a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
print("addition:", a+b)
print("substraction:", a-b)
print("multipication:", a*b)
print("division:", a/b)
print("mod:", a%b)
print("power:", a**b)

#relational operators
print(10 > 5)

#Day1afternoon

value=int(input("Enter number to print table\n"))
for i in range(1, 11): #2's table
    print(i*value)

#ternary operator
a = input("Enter a,b,c value\n")
b = input()
c = input()
maximum = a if a>b and a>c else b if b>c else c         #max betn 3 no's
print(maximum)

#identity check and return address

x=10
y="10"
print(id(x)) #print address of x variable
print(id(y)) #print address of y variable

print(x is y) #checking identity

