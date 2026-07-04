n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print(chr(j+65),end="")
    for j in range(i-2,-1,-1):
        print(chr(j+65),end="")
    print()