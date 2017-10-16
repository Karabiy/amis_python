def count(x,y):
    n=0;
    if(x<y):
        while(x<y):
            x+=1
            n+=1
            print(x,n)
            
    else:
        while(x>y):
            x+=-1
            n+=1
            print(x,n)
    return(n)
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
x1=count(x1,y1)
x2=count(x2,y2)
if(x1==x2):
    print('YES')
else:
    print('NO')