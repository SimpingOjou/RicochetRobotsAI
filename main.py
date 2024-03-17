from playboard import *
from ai import *
import time
import sympy as sp

board = Board()
board.plot(block=False)

# # Greedy best-first search
# player_1 = GreedyBFS(board, board.robots[ElementColor.GREEN])
# player_2 = GreedyBFS(board, board.robots[ElementColor.YELLOW])
# elapsed_time = []

# try:
#     print("Game started with Greedy BFS.\n")
#     print("----------------------------------------------------\n")
#     while not board.finished:
#         start_time = time.time()
#         #player_1.traverse(player_1.robot.get_coord())
#         player_2.traverse(player_2.robot.get_coord())
#         end_time = time.time()
#         elapsed_time.append(end_time - start_time)

#     print("Game ended.\n")
#     print("----------------------------------------------------\n")
#     print("Winner: " + board.winner.get_color() + " in " + str(player_2.moves) + " moves!\n")
#     print("----------------------------------------------------\n")
#     print("Movelist: \n")
#     print(player_2.movelist)
#     print("\nTotal time: " + str(sum(elapsed_time)))
# except UnboundLocalError:
#     print("Game ended.\n")
#     print("----------------------------------------------------\n")
#     print("Position unsolvable :(   -   moves tried: " + str(player_2.moves))
#     print("\n----------------------------------------------------\n")
#     print("Movelist: \n")
#     print(player_2.movelist)
#     print("\nTotal time: " + str(sum(elapsed_time)))
    
# print("\n Visited nodes (with -1 = visited, inf = not visited, number = f(n)):")
# sp.pprint(player_2.map)

# # A*
# player_2 = A_star(board, board.robots[ElementColor.YELLOW])
# elapsed_time = []

# try:
#     print("Game started with A* (g(n) = distance).\n")
#     print("----------------------------------------------------\n")
#     while not board.finished:
#         start_time = time.time()
#         # player_1.traverse(player_1.robot.get_coord())
#         player_2.traverse(player_2.robot.get_coord())
#         end_time = time.time()
#         elapsed_time.append(end_time - start_time)

#     print("Game ended.\n")
#     print("----------------------------------------------------\n")
#     print("Winner: " + board.winner.get_color() + " in " + str(player_2.moves) + " moves!\n")
#     print("----------------------------------------------------\n")
#     print("Movelist: \n")
#     print(player_2.movelist)
#     print("\nTotal time: " + str(sum(elapsed_time)))
# except UnboundLocalError:
#     print("Game ended.\n")
#     print("----------------------------------------------------\n")
#     print("Position unsolvable :(   -   moves tried: " + str(player_2.moves))
#     print("\n----------------------------------------------------\n")
#     print("Movelist: \n")
#     print(player_2.movelist)
#     print("\nTotal time: " + str(sum(elapsed_time)))

# print("\n Visited nodes (with -1 = visited, inf = not visited, number = f(n)):")
# sp.pprint(player_2.map)

# DFS

player_2 = DFS(board, board.robots[ElementColor.YELLOW])
elapsed_time = []

try:
    print("Game started with DFS.\n")
    print("----------------------------------------------------\n")

    start_time = time.time()
    # player_1.traverse(player_1.robot.get_coord())
    player_2.traverse(player_2.robot.get_coord())
    end_time = time.time()
    elapsed_time.append(end_time - start_time)

    player_2.robot.set_coord(player_2.s0.get_x(), player_2.s0.get_y())

    for move in player_2.movelist:
        player_2.board.move(player_2.robot.get_element_color(), move, plot=False)

    print("Game ended.\n")
    print("----------------------------------------------------\n")
    print("Winner: " + board.winner.get_color() + " in " + str(player_2.moves) + " moves!\n")
    print("----------------------------------------------------\n")
    print("Movelist: \n")
    print(player_2.movelist)
    print("\nTotal time: " + str(sum(elapsed_time)))
except UnboundLocalError:
    print("Game ended.\n")
    print("----------------------------------------------------\n")
    print("Position unsolvable :(   -   moves tried: " + str(player_2.moves))
    print("\n----------------------------------------------------\n")
    print("Movelist: \n")
    print(player_2.movelist)
    print("\nTotal time: " + str(sum(elapsed_time)))

print("\n Visited nodes (with -1 = visited, inf = not visited:")
sp.pprint(player_2.map)