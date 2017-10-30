poslid=input('Введіть ріст кожного учня, окрім Петра ')
mas=[]
mas=poslid.split(' ')
mas.append('0')
petya=int(input())
i=0
for i in range (len(mas)):
    if(int(mas[i])<petya):
        number=i+1
        break
print(number)
