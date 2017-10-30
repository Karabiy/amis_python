from math import fabs
def minus(x,x2):
    n=0;
    if(x<x2):
        while(x<x2):
            n+=1
            x+=1
    else:
        while(x>x2):
            x+=-1
            n+=-1
    return (n)

x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
k=minus(y1,x1)
print(k)
i=minus(y2,x2)
print(i)
if(fabs(k%2)==fabs(i%2)):
    print('YES')
else:
    print("NO")