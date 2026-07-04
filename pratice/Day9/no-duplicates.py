arr=[1,2,3,4,3,2,3,6,7,5]
b={}
for i in arr:
    if i in b:
        b[i]=b[i]+1
    else:
        b[i]=1
c=0
for key,value in b.items():
    if value>1:
        c+=1
print(c)