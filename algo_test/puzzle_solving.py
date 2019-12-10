import random


class puzzle:
    # 0 : undiscovered accessable road
    # 1 : obstacle
    # 2 : discovered unaccessable road
    # P : final path
    def __init__(self,rows,columns):
        self.rows = rows
        self.cols = columns
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        self.setting =['0','1']
        self.ini_puzzle_map = [[random.choice(self.setting) for j in range(self.cols)] for i in range(self.rows)]
        self.end_point = (self.rows - 1, self.cols - 1)
        self._validate_path()
        self.dfs_recursive()
        self.show_puzzle()


    def show_puzzle(self):
        # print the final random puzzle to user
        for rows in self.ini_puzzle_map:
            print(rows)

    def _validate_path(self):
        # validate the puzzle
        self.ini_puzzle_map[0][0] = '0'
        self.ini_puzzle_map[-1][-1] = '0'
        v_x, v_y = 0, 0
        while v_x != self.end_point[0] or v_y != self.end_point[1]:
            if v_x == self.end_point[0]:
                for i in range(len(self.ini_puzzle_map[-1])):
                    self.ini_puzzle_map[-1][i] = '0'
                return
            if v_y == self.end_point[1]:
                for i in range(len(self.ini_puzzle_map)):
                    self.ini_puzzle_map[i][-1] = '0'
                return
            a = random.choice([0,1])
            if a == 0:
                v_x += 1
            else:
                v_y += 1
            self.ini_puzzle_map[v_x][v_y] = '0'
        return

    def dfs_recursive(self,x=0,y=0):
        if x == self.end_point[0] and y == self.end_point[1]:
            self.ini_puzzle_map[x][y] = 'P'
            return

        for i in range(len(self.directions)):
            next_x , next_y = x + self.directions[i][0] , y + self.directions[i][1]
            if next_x >= 0 and next_x <= self.end_point[0] and next_y >= 0 and next_y <= self.end_point[1] and self.ini_puzzle_map[next_x][next_y] == '0':
                self.ini_puzzle_map[x][y] = 'P'
                self.dfs_recursive(next_x,next_y)
                self.ini_puzzle_map[x][y] = ''









    def bfs(self):
        pass

    def min_dis(self):
        pass

    def bfs_multi(self):
        pass

    def dfs_multi(self):
        pass


puzzle(3,5)