dic={
    "empno":100,
    "salary":40000,
    "designation":"trainee"
}
print(dic)
temp=0
key=input("enter key to check")
for i in dic:
    if i==key:
        temp=1
        break

if temp:
    print("Key exist")
else:print("Key dosen't exist")

tuple=tuple(dic)
print(type(tuple))
print(tuple)