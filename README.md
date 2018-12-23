# AlphaBetaPruning-Algo

I use alpha beta pruning to create a simple AI for two games - chess and ROTA (a more complicated variant of tic tac toe).

Alpha Beta Pruning reduces the exponential outcomes of a regular minimax search tree, which is particularly useful in chess due to its extremely large set of game states.  When creating a simple AI an objective function is used that "scores" a position.  For ROTA this is simple as you either win with a move or lose with a move.  In chess, creating a simple AI requires some chess knowledge - without using a sort of unsupervised learning technique, the AI relies on some set of rules to be able to tell how a game is going, which I wrote myself in this case using my chess background.

I utilize the python chess library for the visualization as well as the legal move list each turn (the visualisation is not included in these files as this is inteded to be just the algorithm).  For ROTA, I created my own class for the game that behaves similarly to the chess library.
