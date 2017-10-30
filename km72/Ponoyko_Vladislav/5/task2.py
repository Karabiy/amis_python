spisok=input('Введіть послідовність чисел ')
mas=[]
mas=spisok.split(' ')
n=len(mas)
i=0
counter=0
for i in range (n):
    j=0
    for j in range(n):
        if ((mas[i]==mas[j])&(i!=j)& (mas[i]!='k')&(mas[j]!='k')):
            counter+=1
            mas[i]='k'
print('Кількість пар в даній послідовності = ',counter*2)