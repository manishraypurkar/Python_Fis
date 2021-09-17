s=input("Enter string")
print(s)
countu=0
countl=0

for i in s:
    if(i.isupper()):
        countu=countu+1
    elif(i.islower()):
        countl=countl+1
print("Upper letters count:",countu)
print("Lower letters count:",countl)