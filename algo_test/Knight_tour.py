direction = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]  # possible directions of knight
board = [[0 for _ in range(8)] for _ in range(8)]
initial_position = (0,0)
total_method = 0
current_steps = 1
board[initial_position[0]][initial_position[1]] = 1
desire_outcomes = 1000


def qualified(x,y):
    return x in range(8) and y in range(8) and board[x][y] == 0


def take_second(elem):
    return elem[1]

def print_board(method_number):
    print('--------------  Method {} -----------------'.format(method_number))
    for i in board:
        for j in i:
            print(j,end=' ')
        print('\n')
    print('-------------------------------------------')

def greed_algorithm(this_x,this_y):  # choosing the least # of next step is going to be the next point
    qualified_queue = []
    prior_queue = []
    for i in direction:
        if qualified(this_x+i[0],this_y+i[1]):
            qualified_queue.append((this_x+i[0],this_y+i[1]))  # add to qualified queue
    while len(qualified_queue) >= 1:  # sort the next least step
        cursor = qualified_queue.pop()
        count = 0
        for j in direction:
            if qualified(cursor[0]+j[0],cursor[1]+j[1]):
                count += 1
        prior_queue.append([cursor,count])
    prior_queue.sort(key=take_second)
    return prior_queue


def knight_tour(cur_pos,cur_steps):
    global total_method
    if cur_steps == 64:
        total_method += 1
        print_board(total_method)
        if desire_outcomes == total_method:
            return 1
        else:
            return 0
    best_choices_queue = greed_algorithm(cur_pos[0],cur_pos[1])
    for this_step in best_choices_queue:
        this_x = this_step[0][0]
        this_y = this_step[0][1]
        cur_steps += 1
        board[this_x][this_y] = cur_steps
        ret = knight_tour((this_x,this_y),cur_steps)
        if ret: return ret
        board[this_x][this_y] = 0
        cur_steps -= 1


knight_tour(initial_position,current_steps)





