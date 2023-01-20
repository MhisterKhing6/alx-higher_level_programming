# this is the project about finding peak in a list
0
# When the list has only on element
# Whe the list has only tow element
# When there is more than two element
# return the first peak element find


def peak(a):
    equal = True
    if len(a) == 0:
        return None
    if len(a) == 1:
        return list[0]
    else:
        for i in range(0, len(a) -1):
            if i == 0:
                if a[i] > a[i + 1]:
                    return a[i]
            else:
                if a[i] > a[i+1] and a[i] > a[i-1]:
                    return a[i]
            if a[i] != a[i+1]:
                equal = False
    if a[len(a) - 1] > a[len(a) -2]:
        return a[len(a) - 1]
    elif equal:
        return a[0]
    else:
        return  None
    # check if all are equal

print(peak([1,2,3,4,5]))
print(peak([2,2,2,2,2,2]))
print(peak([]))