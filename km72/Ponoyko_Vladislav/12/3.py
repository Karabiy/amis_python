a = []


def parties(list, it=0):
    """
    Function is counting elements

    Args:
        list: list, in which elements in groups is counting
        it: integer, iterator

    Returns:
        a: max count of elements in one group

    Raises:
        OverflowError
        ValueError

    Examples:
    3 3 3
    3
    1 2 3 4 3
    1

    """
    if it == len(list):
        return max(a)
    list2 = "".join(list)
    counter = list.count(list[it])
    if (counter - it)*str(list[it]) in list2:
        a.append(counter - it)
    return parties(list, it + 1)


x = input("Enter list ").split()
print(parties(x))
