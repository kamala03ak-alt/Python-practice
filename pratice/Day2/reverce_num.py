# n=123
# o=123%10
# n=n//10
# t=n%10
# n=n//10
# h=n%10
# c=o*100+t*10+h
# print(c)

num=int(input())
rev=0
while(num>0):
    last=num%10
    rev=rev*10+last
    num=num//10
print(rev)