icom=int(input("Enter your Income\n"))

if icom<=10000:
    res=(icom*0)//100
    print(res)
else:
    newicom=icom-20000
    print("Income Tax Payable is:",((newicom*20)//100)+((10000*10)//100))