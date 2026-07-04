n=int(input())
a=n//2
b=n-a
for i in range(1,n+1):
    if(i<=a):
        print("*"*i)
    else:
        print("*"*b)
        b-=1
        
