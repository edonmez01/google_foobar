def solution(room_dimensions, your_pos, guard_pos, max_bullet_distance):
    from math import sqrt
    from itertools import groupby
    from fractions import gcd
    from bisect import bisect_left

    def distance(n1, n2):
        return sqrt((n1[0] - n2[0])**2 + (n1[1] - n2[1])**2)

    def simple_direction(n1, n2):
        fat = (n1[0]-n2[0],n1[1]-n2[1])
        gcds = (abs(gcd(fat[0], fat[1])), abs(gcd(fat[0], fat[1])))
        return (fat[0] // gcds[0], fat[1] // gcds[1])

    def is_free(p, direction_list, distance_list):
        i = bisect_left(direction_list,p[0])
        return i >= len(direction_list) or direction_list[i] != p[0] or distance_list[i] >= p[1]

    guardReplicas_h = set()
    for i in range(-max_bullet_distance // room_dimensions[0] - 1, max_bullet_distance // room_dimensions[0] + 2):
        guardReplicas_h.add(2 * i * room_dimensions[0] + guard_pos[0])
        guardReplicas_h.add(2 * i * room_dimensions[0] - guard_pos[0])
    guardReplicas_h = list(guardReplicas_h)

    guardReplicas_v = set()
    for i in range(-max_bullet_distance // room_dimensions[1] - 1, max_bullet_distance // room_dimensions[1] + 2):
        guardReplicas_v.add(2 * i * room_dimensions[1] + guard_pos[1])
        guardReplicas_v.add(2 * i * room_dimensions[1] - guard_pos[1])
    guardReplicas_v = list(guardReplicas_v)

    guardReplicas = [(x, y) for x in guardReplicas_h for y in guardReplicas_v if distance((x, y), your_pos) <= max_bullet_distance]

    guardReplicas_direction_distances = sorted([[simple_direction(i, your_pos), distance(i, your_pos)] for i in guardReplicas])
    guardReplicas_final = [list(group)[0] for i, group in groupby(guardReplicas_direction_distances, lambda x: x[0])]

    yourReplicas_h = set()
    for i in range(-max_bullet_distance // room_dimensions[0] - 1, max_bullet_distance // room_dimensions[0] + 2):
        yourReplicas_h.add(2 * i * room_dimensions[0] + your_pos[0])
        yourReplicas_h.add(2 * i * room_dimensions[0] - your_pos[0])
    yourReplicas_h = list(yourReplicas_h)

    yourReplicas_v = set()
    for i in range(-max_bullet_distance // room_dimensions[1] - 1, max_bullet_distance // room_dimensions[1] + 2):
        yourReplicas_v.add(2 * i * room_dimensions[1] + your_pos[1])
        yourReplicas_v.add(2 * i * room_dimensions[1] - your_pos[1])
    yourReplicas_v = list(yourReplicas_v)

    yourReplicas = [(x,y) for x in yourReplicas_h for y in yourReplicas_v if distance((x, y), your_pos) <= max_bullet_distance and (x, y) != tuple(your_pos)]

    yourReplicas_direction_distances = sorted([[simple_direction(i, your_pos), distance(i, your_pos)] for i in yourReplicas])
    yourReplicas_final = [list(group)[0] for i, group in groupby(yourReplicas_direction_distances, lambda x: x[0])]

    blocked_directions = list(map(lambda x: x[0], yourReplicas_final))
    blocked_distances = list(map(lambda x: x[1], yourReplicas_final))

    return len([i[0] for i in guardReplicas_final if is_free(i, blocked_directions, blocked_distances)])
