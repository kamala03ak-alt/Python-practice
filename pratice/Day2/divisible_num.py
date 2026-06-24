try:
    
    num=int(input("enter the number:"))
    if num!=0 and num%5==0 and num%11==0:
        print("True")
    else:
        print("False")
except:
    print("Enter the valid input")