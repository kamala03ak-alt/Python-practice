year=int(input("Enter the Year:"))
if(year%4==0):
    print("leaf year")
elif(year%100==0):
    print("Not a leaf year")
elif(year%400==0):
    print("leaf year")
else:
    print("Not a leaf year")