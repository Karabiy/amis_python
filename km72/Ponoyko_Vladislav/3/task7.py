N=int(input())
while(N>1439):
    N+=-1440
K=0
while(N>59):
    K+=1
    N+=-60
print(K,':',N)
