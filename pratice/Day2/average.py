a=int(input("Enter the 1st num:"))
b=int(input("Enter the 2nd num:"))
count=0
sum=0
for i in range(a,b+1):
    count=count+1
    sum=sum+i
    
avg=sum/count

print("Sum of all numbers:",sum)
print("Average of all numbers:",avg)