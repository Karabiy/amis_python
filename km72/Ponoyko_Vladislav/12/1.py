def minlist(x):
    """
    Function is counting pre highest element in list

    Args:
        x: some list

    Returns:
        pre highest element in list

    Raises:
        OverflowError
        ValueError

    Examples:
    1 2 3
    2
    1 3 2 3 2 4 3
    3

    """
    x = x.split(' ')
    x = set(a)
    x = list(x)
    return sorted(x)[len(x)-2]


a = input('input list, please ')
print(minlist(a))
