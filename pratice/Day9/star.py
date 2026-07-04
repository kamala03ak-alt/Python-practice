n=5
b=1
for i in range(n,0,-1):
    if i==5:
        print("*"*(n*2-1))
    else:
        print(i*"*"+b*" "+i*"*")
        b+=2
    
