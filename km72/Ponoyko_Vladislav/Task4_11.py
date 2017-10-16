def func(x1,x2,y1,y2):
    return(((x1+2==y1) & (x2+1==y2))|((x1-2==y1) & (x2-1==y2))|((x1+2==y1) & (x2-1==y2))|((x1-2==y1) & (x2+1==y2)))
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
if((func(x1,x2,y1,y2)==1)|(func(x2,x1,y2,y1)==1)):
    print('YES')
else:
    print('NO')