def solution(n):
    a = [0] * 300
    a[0] = 1
    a[1] = 1
    out = list(a)

    for i in range(2, 201):
        for index, element in enumerate(a):
            if index < 205 and element > 0:
                try:
                    out[index + i] += element
                except IndexError:
                    pass
        a = list(out)
    a = [i-1 for i in a]
    return a[n]