x=int(input())
y=int(input())
z=int(input())
if(x<=y & x<=z):
    min=x
elif(y<=x & y<=z):
    min=y
else:
    min=z
print(min)
