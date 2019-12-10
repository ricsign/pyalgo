n = int(input('The size of chessboard: '))
chessboard = [[0 for _ in range(n)] for n in range(n)]
sum = 0

def OK():
    pass

def backtrack(row):
    global sum
    if row >= n:
        print('Chessboard '+ str(sum))
        for i in chessboard:
            for j in i:
                print(j, end=' ')
            print('\n')
    else:
        for i in range(n):
            if (OK(row,i)):
                chessboard[row][i] = 1


