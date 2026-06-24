def prime(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return False
        else:
            return True
    else:
        return False
b=print(prime(int(input())))