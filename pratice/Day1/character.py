a=input()
b=ord(a)
if(b>=65 and b<=90):
    print("uppercase")
elif(b>=97 and b<=122):
    print("lowercase")
elif(b>=48 and b<=57):
    print("digit")
else:
    print("special character")