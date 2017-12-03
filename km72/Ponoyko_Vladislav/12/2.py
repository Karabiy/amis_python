def minlist(x, iteration=0):
    """
    Function is max element in list

    Args:
        x: list, in which we are looking for a max
        it: integer, iterator

    Returns:
        max element of list

    Raises:
        OverflowError
        ValueError

    Examples:
    3 3 3
    3
    1 2 3 4 3
    4

    """
    if(iteration == (len(x)-1)):
        return float(x[iteration])
    if(float(x[iteration]) > float(minlist(x, iteration+1))):
        return x[iteration]
    else:
        return float(minlist(x, iteration+1))


a = input()
a = a.split(' ')
c = str(int(minlist(a)))
print(a.count(c))
