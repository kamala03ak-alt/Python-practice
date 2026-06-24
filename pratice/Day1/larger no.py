a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if(a==b and b==c):
    print("All are equal")
else:
    if(a>=b and a>=c):
     print("a is greatest number")
    if(b>=a and b>=c):
     print("b is greatest number")
    if(c>=a and c>=b):
     print("c is greatest number")

#print("The greatest number is:",max(a,b,c))


