import chess

def initialize():
    board = chess.Board()
    
def show():
    return board
    
def turn():
    show()
    n = input('make a move' + '\n')
    board.push(chess.Move.from_uci(n))
    cop = board
    z = get_move(board,4)
    print('\n' + str(z))
    board.push(z)
    return board
    
def get_move(board1, depth1):
    return minimaxbaby(board1, depth1)[1]
    
def minimaxbaby(board, depth, m_or_m = True, alpha = -1000, beta = 1000):
    #hit the bottom of your tree
    if depth == 0:
        return (evaluate(board), 'hi')
    if board.is_variant_end():
        return (100000, 'hi')
    
    if m_or_m:
        for node in board.legal_moves:
            board.push(node)
            temp = minimaxbaby(board, depth - 1, not m_or_m, alpha, beta)[0]
            if (temp > alpha):
                bestNode = node
                alpha = temp
            board.pop()
            if (beta <= alpha):
                break
        try:
            return (alpha, bestNode)
        except:
            return (alpha, 0)
    
    else:
        for node in board.legal_moves:
            board.push(node)
            temp = minimaxbaby(board, depth - 1, not m_or_m, alpha, beta)[0]
            if (temp < beta):
                bestNode = node
                beta = temp
            board.pop()
            if (beta <= alpha):
                break
        try:
            return (beta, bestNode)
        except:
            return (beta, 0)
            
def evaluate(board):
    chess_dict = {'P': 1 ,'N':3, 'B':3, 'R':5, 'Q':9, 'K':100000000,'p': -1 ,'n':-3, 'b':-3, 'r':-5, 'q':-9, 'k':-100000000}
    center = [18,19,20,21,26,27,28,29,34,35,36,37,42,43,44,45]
    evaluation = 0
    layout = board.piece_map()
    #check pieces on the board
    count = 0
    opp_count = 0
    for key, value in layout.items():
        if value == 'b':
            count += 1
        if count == 2:
            evaluation += 1

        if value == 'B':
            opp_count += 1
        if opp_count == 2:
            evaluation -= 0.5

        evaluation += -1 * chess_dict[value.symbol()]
        if layout[key].symbol() == 'K' and key <= 55:
            evaluation -= 2
        if layout[key].symbol() == 'k' and key >= 8:
            evaluation += 2
    #check for having pieces in the center
    for j in center:
        if j in layout:
            if layout[j].symbol().islower():
                evaluation += 1
            else: 
                evaluation -= 1
    return evaluation
