# don't bother writing this, I know how to, but too repetitive to realize

import random

def e(unit):
    if unit == 'X':
        return 1
    else:
        return 0
def solve(map):
    for rows in [0,1,2]:
        if map[rows].count('X') == 1:
            if map[rows][0] == "X":
                map[rows][0] = str(2*int(map[rows][1])-int(map[rows][2]))
            elif map[rows][1] == "X":
                if (int(map[rows][2])-int(map[rows][0])) % 2 == 0:
                    diff = (int(map[rows][2])-int(map[rows][0])) // 2
                else:
                    return False
                map[rows][1] = str(int(map[rows][0])+diff)
            else:
                map[rows][2] = str(2*int(map[rows][1])-int(map[rows][0]))
    if e(map[0][0])+e(map[1][0])+e(map[2][0]) == 1:


    # end condition
    if map[0].count('X') + map[1].count('X') + map[2].count('X') == 0:
        return map

    # recursive
    i,j = 0,0
    while i < 3:
        while j < 3:
            if map[i][j] == "X":
                map[i][j] = str(random.randint(-1000000000,1000000001))
                a = solve(map)
                if a:
                    return a
            j += 1
        i += 1




map = []
for _ in range(3):
    map.append(input().split())
solve(map)
print(map)