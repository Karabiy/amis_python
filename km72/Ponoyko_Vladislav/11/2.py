def minlist(x, iteration=1):
    if iteration == (len(x)-2):
        return float(x[iteration])
    if float(x[iteration]) < float(minlist(x, iteration+1)):
        return x[iteration]
    else:
        return float(minlist(x, iteration+1))


n = ' '
x = ''
while (n != ''):
    n = input()
    x = x + ' ' + n
x = x.split(' ')
print(x)
print(minlist(x))
