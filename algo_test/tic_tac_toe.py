from termcolor import *
chessboard = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
ai = 'O'
human = 'X'
score_lookup_table = {'O': 10, 'X': -10, 'tie': 0}


def draw_chessboard(last_turn=None):
    for i in range(3):
        for j in range(3):
            cur = '|'+chessboard[i][j]
            if last_turn and i == last_turn[0] and j == last_turn[1]:
                print(colored(cur, 'red'), end=' ')
            else:
                print(cur, end=' ')
        print('|')
        print('----------')


def equal(a,b,c):
    return a == b == c and a != ' '


def winner_judge():
    # row check
    for row in range(3):
        if equal(chessboard[row][0],chessboard[row][1],chessboard[row][2]):
            return chessboard[row][0]

    #col check
    for col in range(3):
        if equal(chessboard[0][col],chessboard[1][col],chessboard[2][col]):
            return chessboard[0][col]

    #diagonal check
    if equal(chessboard[0][0],chessboard[1][1],chessboard[2][2]):
        return chessboard[0][0]
    if equal(chessboard[0][2],chessboard[1][1],chessboard[2][0]):
        return chessboard[0][2]

    #tie check
    for i in chessboard:
        for j in i:
            if j != ' ':
                continue
            else:
                return 'game_not_ended'
    return 'tie'


def human_turn():
    human_input = input('Your turn: ').split()
    x,y = int(human_input[0]),int(human_input[1])
    if -1 < x < 3 and -1 < y < 3 and chessboard[x][y] == ' ':
        chessboard[x][y] = human
    else:
        print('Your input is invalid, please enter two integers that between 0 to 2, inclusive, seperate with a blank space')
        human_turn()
    return [x,y]


def minimax(ismaximizing):
    result = winner_judge()
    if result != 'game_not_ended':
        return score_lookup_table[result]

    if ismaximizing:
        bestscore = float('-inf')
        for i in range(3):
            for j in range(3):
                if chessboard[i][j] == ' ':
                    chessboard[i][j] = ai
                    score = minimax(False)
                    chessboard[i][j] = ' '
                    bestscore = max(bestscore,score)
                    # We essentially want to keep the best score in order to win,
                    # if our score is 10, that means we've won, then we don't need to check other possibilities
                    # The stradegy of cutting branches also can be used in human move iteration
                    if bestscore >= 10:
                        break
        return bestscore
    if not ismaximizing:
        bestscore = float('inf')
        for i in range(3):
            for j in range(3):
                if chessboard[i][j] == ' ':
                    chessboard[i][j] = human
                    score = minimax(True)
                    chessboard[i][j] = ' '
                    bestscore = min(bestscore,score)
                    if bestscore <= -10:
                        break
        return bestscore


def ai_turn():
    best_score = float('-inf')
    move = [0,0]
    for i in range(3):
        for j in range(3):
            if chessboard[i][j] == ' ':
                chessboard[i][j] = ai
                score = minimax(False)
                chessboard[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = [i,j]
    chessboard[move[0]][move[1]] = ai
    return move


def game_setup():
    while winner_judge() == 'game_not_ended':
        thismove = human_turn()
        first_judge = winner_judge()
        if first_judge != 'game_not_ended':
             draw_chessboard()
             print(first_judge)
             break
        else:
            draw_chessboard(thismove)
        #AI wants to maximize the point, while human trys to stop AI, using minimax
        thatmove = ai_turn()
        second_judge = winner_judge()
        if second_judge != 'game_not_ended':
            draw_chessboard()
            print(second_judge)
            break
        else:
            draw_chessboard(thatmove)


if __name__ == '__main__':
    game_setup()