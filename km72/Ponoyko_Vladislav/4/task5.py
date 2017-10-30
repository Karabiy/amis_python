a=int(input())
b=int(input())
c=int(input())
if(a==b & b==c):
    print('3')
elif((a==b) | (b==c) | (c==a) ):
    print('2')
else:
    print('0')