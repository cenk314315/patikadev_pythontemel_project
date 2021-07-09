arr = [[1, 2], [3, 4], [5, 6, 7]]


def reverse_arr(x):
    x.reverse()
    for arr in x:
        if(type(arr) == list):
            reverse_arr(arr)


reverse_arr(arr)
print(arr)