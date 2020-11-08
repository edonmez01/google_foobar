def solution(l):
    out = 0
    for ind2 in range(1, len(l) - 1):
        ele2 = l[ind2]
        left_side = 0
        right_side = 0
        for ind1 in range(ind2):
            ele1 = l[ind1]
            if not ele2 % ele1:
                left_side += 1
        for ind3 in range(ind2 + 1, len(l)):
            ele3 = l[ind3]
            if not ele3 % ele2:
                right_side += 1
        out += left_side * right_side

    return out
