from playboard import *
from ai import *
import time
import sympy as sp

def endgame_solved(moves:int, movelist:list, time:float):
    print("Solution found in " + str(moves) + " moves.")
    print("----------------------------------------------------")
    print("Movelist: ")
    for move in movelist:
        print(move + ' - ')
    print("----------------------------------------------------")
    print("Total time: " + str(sum(time)))
    print("----------------------------------------------------")

def endgame_unsolved(moves:int, movelist:list, time:float):
    print("Position unsolvable :(   -   moves tried: " + str(moves))
    print("----------------------------------------------------")
    print("Movelist: ")
    for move in movelist:
        print(move + ' - ')
    print("----------------------------------------------------")
    print("Total time: " + str(sum(time)))
    print("----------------------------------------------------")

# Greedy best-first search
board = Board()
board.plot(block=False)
player_1 = GreedyBFS(board, board.robots[ElementColor.GREEN], plotter = False)
player_2 = GreedyBFS(board, board.robots[ElementColor.YELLOW], plotter = False)
elapsed_time = []

try:
    print("Game started with Greedy BFS.")
    print("----------------------------------------------------")
    while not board.finished:
        start_time = time.time()
        #player_1.traverse(player_1.robot.get_coord())
        player_2.traverse(player_2.robot.get_coord())
        end_time = time.time()
        elapsed_time.append(end_time - start_time)

    endgame_solved(player_2.moves, player_2.movelist, elapsed_time)
except UnboundLocalError:
    endgame_unsolved(player_2.moves, player_2.movelist, elapsed_time)
except Exception as e:
    print(e)
    
print("Visited nodes (with -1 = visited, inf = not visited, number = f(n)):")
sp.pprint(player_2.map)
print("----------------------------------------------------\n")

# A*
board = Board()
board.plot(block=False)
player_2 = A_star(board, board.robots[ElementColor.YELLOW])
elapsed_time = []

try:
    print("Game started with A* (g(n) = distance).")
    print("----------------------------------------------------")
    while not board.finished:
        start_time = time.time()
        # player_1.traverse(player_1.robot.get_coord())
        player_2.traverse(player_2.robot.get_coord())
        end_time = time.time()
        elapsed_time.append(end_time - start_time)

    endgame_solved(player_2.moves, player_2.movelist, elapsed_time)
except UnboundLocalError:
    endgame_unsolved(player_2.moves, player_2.movelist, elapsed_time)
except Exception as e:
    print(e)

print("Visited nodes (with -1 = visited, inf = not visited, number = f(n)):")
sp.pprint(player_2.map)
print("----------------------------------------------------\n")

# DFS
board = Board()
board.plot(block=False)
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

    endgame_solved(player_2.moves, player_2.movelist, elapsed_time)
except UnboundLocalError:
    endgame_unsolved(player_2.moves, player_2.movelist, elapsed_time)
except Exception as e:
    print(e)

print("Visited nodes (with -1 = visited, inf = not visited:")
sp.pprint(player_2.map)
print("----------------------------------------------------\n")