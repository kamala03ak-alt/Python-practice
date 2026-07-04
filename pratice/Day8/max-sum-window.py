a=[2,1,5,1,3,2]
b=3
for i in range(len(a)-b+1):
    c=[a[i+(i+b)]]
    print(c)