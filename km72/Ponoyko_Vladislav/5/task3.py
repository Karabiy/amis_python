spisok=input('Введіть послідовність чисел ')
mas=[]
mas=spisok.split(' ')
l=len(mas)
i=0
for i in range (l):
    j=0
    k=0
    for j in range(l):
        if ((mas[i]==mas[j])&(i!=j)):
            k+=1
    if(k==0):
        print(mas[i])