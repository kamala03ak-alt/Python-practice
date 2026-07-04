class WeakPassword(Exception):
    pass
try:
    p=(input())
    if len(p)<8:
        raise WeakPassword("**Enter the longer password..!")
    else:
        print("Your Password:",p)
except WeakPassword as W:
    print(W)