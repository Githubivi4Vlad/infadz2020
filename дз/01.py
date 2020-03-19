a = int(input())
n = int(input())
q = int(input())
k = int(input())

b = a*(q*(n-k))

def func(a,q,n,k):
 if (a,q,n,k) == 0:
    return 0
 else:
    return(a*(q*(n-k)))

print(func(0,12,13,54))

