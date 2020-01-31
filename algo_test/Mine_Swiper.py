import random
# define O: undiscovered    F: Flag    X: Mine
# define input: E: expose  S: set flag  D: deflag
board_length = 3 # width is the same
num_mine = 2
num_flag = 0
limit_flag = num_mine
board = [['O' for _ in range(board_length)] for _ in range(board_length)]
board_for_user = [['O' for _ in range(board_length)] for _ in range(board_length)]
winning_status = False
mine_repos = []
flag_repos = []

def winner_judge():
    global winning_status
    if num_flag == num_mine:
        winning_status = True
        return True

def random_mine():
    for _ in range(num_mine):
        a,b = random.randint(0,board_length-1),random.randint(0,board_length-1)
        while board[a][b] != 'O':
            a, b = random.randint(0, board_length-1), random.randint(0, board_length-1)
        mine_repos.append((a,b))
        board[a][b] = 'X'

def show_board():
    for i in board_for_user:
        for j in i:
            print(j,end = ' ')
        print('\n')

def input_validation(input,pos):
    if input not in 'ESD' and len(input) != 1:
        return False
    for elem in pos:
        if elem not in range(0,board_length):
            return False
    return True

def excursion(user_pos):
    direction = [(0,1),(0,-1),(1,0),(-1,0),(-1,1),(1,-1),(1,1),(-1,-1)]
    count = 0
    for i in direction:
        if user_pos[0]+i[0] in range(board_length) and user_pos[1]+i[1] in range(board_length):
            if board[user_pos[0]+i[0]][user_pos[1]+i[1]] == 'X':
                count += 1
    board_for_user[user_pos[0]][user_pos[1]] = str(count)
    return count


def set_flag(user_pos):
    global num_flag, limit_flag
    if board_for_user[user_pos[0]][user_pos[1]] != 'F':
        limit_flag -= 1
        if limit_flag < 0:
            return False
        board_for_user[user_pos[0]][user_pos[1]] = 'F'
        if user_pos not in flag_repos:
            flag_repos.append(user_pos)
            if user_pos in mine_repos:
                num_flag += 1
        return True
    return False

def deflag(user_pos):
    global num_flag,limit_flag
    if board_for_user[user_pos[0]][user_pos[1]] != 'O':
        board_for_user[user_pos[0]][user_pos[1]] = 'O'
        if user_pos in flag_repos:
            flag_repos.remove(user_pos)
            limit_flag += 1
            if user_pos in mine_repos:
                num_flag -= 1
        return True
    return False




def ini_game():
    random_mine()
    while not winning_status:
        show_board()
        user_input = (input('Please enter"E/S/D" E: expose  S: set flag  D: deflag : ').strip()).upper()
        user_pos = tuple(map(int,input('Select a position: ').split()))
        if not input_validation(user_input,user_pos):
            print('Invalid input!')
            continue
        if user_input == 'E':
            if board[user_pos[0]][user_pos[1]] == 'X':
                print('You hit the mine!')
                break
            else:
                excursion(user_pos)
        if user_input == 'S':
            if not set_flag(user_pos):
                print('Invalid input, Or you must deflag!')
                continue
        if user_input == 'D':
            if not deflag(user_pos):
                print('Invalid input!')
                continue
        if winner_judge():
            print('You win!!!!!!!')




ini_game()



