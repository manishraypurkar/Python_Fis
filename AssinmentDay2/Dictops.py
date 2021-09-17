dic={
    "empno":100,
    "salary":40000,
    "designation":"trainee"
}
print(dic)
for i in dic.items():
    print(i)

print("salary from get function: ",dic.get("salary"))
dic["designation"]="Software engineer"
print("After changing designation: ",dic)
print("Length is: ",len(dic))