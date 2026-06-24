try:
    num=int(input("Enter the number:"))
    found=False

    for i in range(1,num+1):
        if i*i<num:
            if i*i==num:
                print(i)
                found=True
                break
        else:
            break
    
    if found==False:
        print("Not a perefect square")

except:
    print("Invalid input")