no=int(input("Enter number\n"))
temp=no
newno=0

while no>0:
    rem=no%10
    newno=(newno*10)+rem
    no=no//10

if newno==temp:
    print("true")
else:print("false")