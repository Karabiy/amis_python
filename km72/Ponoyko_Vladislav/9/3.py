def power(a,n,k,c=1):
    c+=1
    a=a*k
    if(c<n):
        a=power(a,n,k,c)
        return a
    else:
        return a
a=float(input())
n=int(input())
k=a
print(power(a,n,k))
