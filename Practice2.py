#day2
#Slicing
s="manish raypurkar"
print(s[1:3]) #beg+End-1
print(s[:-1])#beg+excludingend
print(s[::-1])#beg+end-1+step(defult=1)

#functions

def hello(name):
    return "Hello "+name+"!"  #concatenation also
print(hello("Manish"))

#String function

print(s.find('h',1,10))
print(s.count('m'))
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.strip())
i=0
for i in range(11):
    if i%2==0:
         break
    print(i)
print("ouside loop")

for i in range(11):
    if i%2==0:
        continue
    print(i)

#List

list1=[1,2,3,4,5]
print(list1)
for i in list1:
    print(i)

list1.append(6) # added at last
list1.insert(6,7) #added at index 6
print(list1)
list1.remove(7) #remove 7 element
print(list1)

list1.reverse() #reverse list
print(list1)
print(*list1,sep=",")
list1.clear()
print(list1)

#tuple

t1=(1,2,3,4,5) #readonly list
print(type(t1))
print(t1)

print(len(t1))
for i in t1:
    print(i)

#set mutable

s1={1,2,3,4}
print(type(s1))
print(s1)
s1.add(5)
print(s1)
#s1.add(5)#duplicate not allow
s1.pop()
print("after poping\n",s1)

#frozenset immutable

fs={1,2,3,4}
print(fs)
fs.add(5)

#dictonary key:value

dic={
    "brand":"dell",
    "price":50000
}

print(dic)

dic["brand"]="hp","lenovo","asus" #unique key multiple values
dic["price"]=60000,40000,450000
print(dic)
print("Brand Price")
for i in dic:
    print(i,dic[i])

for i in dic.items(): #using item fun of dictonory
    print(i)

