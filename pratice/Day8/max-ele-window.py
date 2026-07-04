a=[1,3,2,5,4]
b=2
for i in range(len(a)-b+1):
    c=max(a[i:i+b])
    print (c,end=" ")
