class Board:
    def __init__(self, board):
        self.turn = 1
        self.players = {-1:"c", 1:"p"}
        self.board = board
        self.moveList = []

    def make_move(self, move, player = None, forwards = True):
        if player is None:
            player = self.players[self.turn]
        self.turn *= -1
        if isinstance(move, int):
            self.board = self.board[:move] + player + self.board[move+1:]
            if forwards:
                self.moveList.append(player + str(move))
        else:
            lesser = min(move[0], move[1])
            if move[0] == lesser:
                self.board = self.board[:lesser] + '-' + self.board[lesser+1 : move[1]] + player + self.board[move[1] + 1:]
            else:
                self.board = self.board[:lesser] + player + self.board[lesser+1 : move[0]] + '-' + self.board[move[0] + 1:]
            if forwards:
                self.moveList.append(player + str(move[0]) + str(move[1]))
    def pop(self):
        move = [int(s) for s in self.moveList[-1][1:]][::-1]
        self.moveList = self.moveList[:-1]
        if len(move) == 1:
            self.make_move(move[0], player = '-', forwards = False)
        else:
            self.make_move(move, player = self.players[self.turn * -1], forwards = False)
        
    def gen_moves(self):
        adjacency = {0: [1,3,4], 1:[0,2,4], 2:[1,4,5], 3:[0,4,6], 4:[1,3,5,7], 
                        5:[2,4,8], 6:[3,4,7], 7:[6,4,8], 8:[7,4,5]}
        moves = []
        empty_space = []
        counter = 0
        for ind, i in enumerate(self.board):
            if i == "-": 
                counter += 1
                empty_space.append(ind)
        if counter > 3:
            return empty_space

        for ind, i in enumerate(self.board):
            if i == self.players[self.turn]:
                for j in list(set(adjacency[ind]).intersection(empty_space)):
                    moves.append([ind, j])
        return moves
                    
    def evaluate(self):
        evaluation = 0
        if self.check_winner('c'): evaluation = -10
        elif self.check_winner('p'): evaluation = 10
        return evaluation
    
    def check_winner(self, player):
        board = self.board
        evaluation = 0
        if (board[0] == player):
            if (board[0] == board[1] and board[0] == board[2]): 
                evaluation -=10
            if (board[0] == board[3] and board[0] == board[6]): 
                evaluation -=10
            if (board[0] == board[4] and board[0] == board[8]):
                evaluation -=10
            if (board[0] == board[1] and board[0] == board[3]):
                evaluation -=10
        if (board[1] == player):
            if (board[1] == board[4] and board[1] == board[7]):
                evaluation -=10
            if (board[1] == board[2] and board[1] == board[5]): 
                evaluation -=10
        if (board[5] == player):
            if (board[5] == board[4] and board[5] == board[3]): 
                evaluation -=10
            if (board[5] == board[7] and board[5] == board[8]): 
                evaluation -=10
            if (board[5] == board[2] and board[5] == board[8]): 
                evaluation -=10
        if (board[6] == player):
            if (board[6] == board[2] and board[6] == board[4]): evaluation -=10
            if (board[6] == board[7] and board[6] == board[8]): evaluation -=10
            if (board[6] == board[3] and board[6] == board[7]): evaluation -=10
        if evaluation != 0: return True
        return False
    
    def is_variant_end(self):
        if self.evaluate() != 0: return True
        return False
    
def get_move(board1, depth1 = 3):
    return minimaxbaby(board1, depth1)[1]
    
def minimaxbaby(board, depth, maxxer = True, alpha = -1000, beta = 1000):
    #hit the bottom of your tree
    if depth == 0 or board.is_variant_end():
        #print("evaluate  " + str(board.evaluate()))
        return (board.evaluate(), 'hi')
    
    if maxxer:
        for node in board.gen_moves():
            #print("turn " + board.players[board.turn])
            #print("board beofre move  " + board.board)
            board.make_move(node)
            #print("board after move  " + board.board)
            temp = minimaxbaby(board, depth - 1, not maxxer, alpha, beta)[0]
            if (temp > alpha):
                bestNode = node
                alpha = temp
            board.pop()
            #print("board after pop  " + board.board)
            if (beta <= alpha):
                break
        try:
            return (alpha, bestNode)
        except:
            return (alpha, 0)
    
    else:
        for node in board.gen_moves():
            #print("turn " + board.players[board.turn])
            #print("board beofre move  " + board.board)
            board.make_move(node)
            #print("board after move  " + board.board)
            temp = minimaxbaby(board, depth - 1, not maxxer, alpha, beta)[0]
            if (temp < beta):
                bestNode = node
                beta = temp
            board.pop()
            #print("board after pop  " + board.board)
            if (beta <= alpha):
                break
        try:
            return (beta, bestNode)
        except:
            return (beta, 0)

