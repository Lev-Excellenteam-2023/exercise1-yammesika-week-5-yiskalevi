# Yiska Levi

def join(*l, sep='-'):
    if len(l) == 0:
        return None
    all_list = []
    for lis in l:
        all_list = all_list + lis
        if lis != l[len(l) - 1]:
            all_list.append(sep)
    return all_list

#A correctness test
print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
