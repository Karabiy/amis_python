from math import e


def inp_float():
    '''
    Функція для введення чисел типу float
    Args:
        None
    Returns:
        c: float, число
    Raises:
        None
    Examples:
    '''
    b = 0
    a = input('Введіть число! ')
    a = str.strip(a)
    if (a.find('-') == a.rfind('-') == 0):
        a = a[1:]
        b = 1
    if (((a.rfind('.')) == a.find('.') != -1)):
        a = a.split('.')
        if((float_help(a[0])) & (float_help(a[1]))):
            if (b == 1):
                return (-float(mas_str(a)))
            else:
                return float(mas_str(a))
        else:
            a = inp_float()
            return float(mas_str(a))
    else:
        if (float_help(a)):
            if (b == 1):
                return (-float(a))
            else:
                return float(a)
        else:
            a = inp_float()
            return (a)


def float_help(a):
    '''
    Helper function
    '''
    return str.isdigit(a)


def mas_str(a):
    '''
    Helper function
    '''
    if((type(a)) == list):
            a = '.'.join(a)
            return a
    else:
        return str(a)


def kvadvpryamo(x, y, c=30):
    '''
    Функція для обрахунку

    Args:
        x:float, argument
        y:float, argument
        c:int

    Returns:
        c: float, число

    Raises:
        None

    Examples:

    '''
    c = (x*y)//(c**2)
    return c


def power(x, y):
    return x**y


def count(x):
    n = power(e, x)-x-2+power(1+x, x)
    return n


a = '1'
while ((a == '1') | (a == '2')):
    a = input('Якщо бажаєте спробувати першу програму, то введіть 1 ' + '\n' +
              'Якщо бажаєте спробувати другу програму, то введіть 2 ' + '\n' +
              'Якщо не бажаєте використовувати наступні програми, ' +
              'натисніть щось відмінне від 1 чи 2' + '\n')
    if (a == '1'):
        print('Введіть аргумент функції')
        x = inp_float()
        print(count(x), 'Значення формули при вказаному аргументі  ')
    if (a == '2'):
        print('Ширина прямокутника' + '\n')
        x = inp_float()
        print('Висота прямокутника' + '\n')
        y = inp_float()
        print(kvadvpryamo(x, y), 'квадрата зі стороною 30 може \
                                  вміститись в даному прямокутнику')
