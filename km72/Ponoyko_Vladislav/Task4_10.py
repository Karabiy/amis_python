def count(x,y):
    n=0;
    if(x<y):
        while(x<y):
            x+=1
            n+=1
    else:
        while(x>y):
            x+=-1
            n+=1
    return(n)
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
a=count(x1,y1)
b=count(x2,y2)
if((((x1==x2) & (y1!=y2)) | ((x1!=x2) & (y1==y2)))|(a==b)):
   print('YES')
else:
   print('NO')