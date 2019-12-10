n = int(input('Please enter the number of nodes: '))
m = int(input('Please enter the number of color: '))
sum = 0
color = [None for i in range(n)]

def creatmap():
    #edge represents the number of vertices
    edge = int(input('Please enter the number of vertices: '))
    #initializing the 2d array map
    map = [[0 for _ in range(edge)] for _ in range(edge)]
    for i in range(edge):
        u,v = input().split()
        u = int(u)
        v = int(v)
        map[u][v] = map[v][u] = 1
    return map


map = creatmap()


def OK(current):
    #iterate each point if it's next to current, if it has same color, return false
    for j in range(current):
        if map[current][j] == 1 and color[j] == color[current]:
            return False
    return True


def backtrack(current):
    global sum,color
    if current >= n:
        # if reached above the last node
        sum += 1
        print('Method '+str(sum)+': ')
        for i in color:
            print(i+1,end=' ')
        print('\n')
    else:
        for i in range(m):
            #attempt to use a color within the range m (since we only have m colors)
            color[current] = i
            if OK(current):
                #iterate the next node, if not, it will repeat
                backtrack(current+1)

backtrack(0)
# 7
# 3
# 12
# 0 1
# 0 2
# 0 3
# 1 2
# 1 4
# 2 3
# 2 4
# 3 4
# 3 6
# 4 5
# 4 6
# 5 6





    





