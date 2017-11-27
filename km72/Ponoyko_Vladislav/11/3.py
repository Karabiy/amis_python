def func(x, iteration=0):
    if iteration == 0:
        return x[iteration]
    else:
        return str(x[iteration]) + ' ' + str(func(x, iteration-1))


n = ' '
a = n
while(n != ''):
    n = input()
    a = a + ' ' + n
a = a.split(' ')
it = len(a)
print((func(a, it-1))[1:])
