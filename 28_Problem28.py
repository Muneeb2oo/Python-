a1=int(input("Enter Number 1: "))
a2=int(input("Enter Number 2: "))
a3=int(input("Enter Number 3: "))
per=((a1+a2+a3)/150)*100
perA1=(a1/50)*100
perA2=(a2/50)*100
perA3=(a3/50)*100
print("Percentage of Subject 1 is ",perA1)
print("Percentage of Subject 2 is ",perA2)
print("Percentage of Subject 3 is ",perA3)
print("Total Percentage",per)
if(per>=40 and perA1>=33 and perA2>=33 and perA3>=33):
    print("you are Passed")
else:
    print("you are Failed")

