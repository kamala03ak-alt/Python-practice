num=int(input("Enter a number: "))
count=num-1
for i in range(1,num+1):
    print(" "*count,str(i)*i)
    count-=1

#print(" "*(num-i),str(i)*i)