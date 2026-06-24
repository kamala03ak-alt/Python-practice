n=[]
a=int(input("Enter a number: "))
for i in range(1,a+1):
    val=int(input("Enter a value: "))
    n.append(val)
print("The list is:", n)
print("The sum of the list is:", sum(n))

