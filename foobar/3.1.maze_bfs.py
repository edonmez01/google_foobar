def solution(map):
    def solve(map):
        map = [[[n, -1] for n in i] for i in map]
        q = [(0,0)]
        while True:
            if not q:
                return 0

            ptr = q.pop(0)

            if ptr == (0,0):
                map[ptr[0]][ptr[1]][1] = 1
            
            if ptr == (len(map) - 1, len(map[0]) - 1):
                return map[ptr[0]][ptr[1]][1]

            available_neighbors = []
            if not(ptr[0] == 0) and map[ptr[0]-1][ptr[1]][0] == 0:
                available_neighbors.append((ptr[0]-1, ptr[1]))
            if not(ptr[0] == len(map) - 1) and map[ptr[0]+1][ptr[1]][0] == 0:
                available_neighbors.append((ptr[0]+1, ptr[1]))
            if not(ptr[1] == 0) and map[ptr[0]][ptr[1]-1][0] == 0:
                available_neighbors.append((ptr[0], ptr[1]-1))
            if not(ptr[1] == len(map[0]) - 1) and map[ptr[0]][ptr[1]+1][0] == 0:
                available_neighbors.append((ptr[0], ptr[1]+1))

            for i in available_neighbors:
                if map[i[0]][i[1]][1] == -1:
                    q.append(i)
                    map[i[0]][i[1]][1] = map[ptr[0]][ptr[1]][1] + 1

    out = []
    out.append(solve(map))
    for row in map:
        for column_index, element in enumerate(row):
            if element == 1:
                row[column_index] = 0
                out.append(solve(map))
                row[column_index] = 1

    return min(filter(lambda x: x > 0, out))


        
