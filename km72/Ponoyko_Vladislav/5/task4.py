def iput(mas1):
    mas1.append(input())
    return(mas1)
N=int(input('Кількість кеглів = '))
K=int(input('Кількість кидів = '))
levo=[]
pravo=[]
i=0
p=set([])
for i in range (K):
    print("Введіть яку кеглю зліва зіб'є")
    iput(levo)
    print("Введіть яку кеглю справа зіб'є куля")
    iput(pravo)
j=0

for j in range (len(levo)):
    n=int(pravo[j])-int(levo[j])
    livo=int(levo[j])
    for i in range (n+1):
        p.add(livo+i)
o=set([])
for i in range (N):
    o.add(i+1)
o-=p
levo=list(o)
reslis=[]
for i in range (N+1):
    reslis.append(i)
reslis+=levo
reslis.remove(0)
for i in range(N):
    for j in range(len(levo)):
        if(reslis[i]==reslis[N+j]):
            reslis[i]='|'
for i in range(N):
    if(reslis[i]!='|'):
        reslis[i]='.'
del reslis[N:]
print(' '.join(reslis))