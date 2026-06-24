try:
    a=int(input("Enter the start number:"))
    b=int(input("Enter the end number:"))
    count_a=0
    count_b=0
    for i in range(a,b+1):
        if i%2==0:
            count_a=count_a+1
        else:
            count_b=count_b+1
    print("Count of even number:",count_a)
    print("Count of odd number:",count_b)
except:
    print("Invalid input")