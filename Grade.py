print("*****Grading System*****")
percentage = int(input("Enter your Percentage\n"))
if percentage>80 and percentage<=100:
    print("Grade A")
elif percentage>70 and percentage<=80:
    print("Grade B")
elif percentage>60 and percentage<=70:
    print("Grade C")
elif percentage>40 and percentage<=60:
    print("Grade D")
elif percentage>35 and percentage<=40:
    print("Grade E")
elif percentage>100 or percentage<=0:
    print("Invalid")
else :print("Failed!")
