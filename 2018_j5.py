# def choose_your_own_path(pathways,reachable,cur,local_min,global_min):
#     if cur == len(pathways)-1:
#         reachable = True
#         global_min = local_min if local_min < global_min
#         return
#     for i in range(pathways[cur]):
#         choose_your_own_path()

class Solution(object):
    def exist(self, board, word):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.exit(board, word, x, y, 0):
                    return True
        return False
    def exit(self, board, word, x, y, i):
        if i == len(word):
            return True
        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = board[y][x].swapcase()
        isexit = self.exit(board, word, x + 1, y, i + 1) or self.exit(board, word, x, y + 1, i + 1) or self.exit(board,word, x - 1, y ,i + 1) or self.exit(board, word, x, y - 1, i + 1)
        board[y][x] = board[y][x].swapcase()
        return isexit

board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
a = Solution()
print(a.exist(board,'ABCESA'))
