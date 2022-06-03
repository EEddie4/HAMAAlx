def max_integer(my_list=[]):
    if len(my_list) == 0:
        return(None)
    maxe = my_list[0]
    for n in my_list:
        if n > maxe:
            maxe = n
    return (maxe)
