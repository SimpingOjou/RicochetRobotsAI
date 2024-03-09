import sys
sys.path.append("C:/Users/Simone/Documents/DTU/IntroAI/Project/GameFunctions")
from playboard import *
from agent import *
import matplotlib.pyplot as plt

board = Board()
board.plot()


controlled_robot = ElementColor.GREEN
#test_moving_robot(controlled_robot, Directions.LEFT, board.get_robot(controlled_robot).get_coord(), True)
board.move(controlled_robot, Directions.LEFT)
board.plot(block=True)

# plt.plot()
# test_moving_robot(ElementColor.YELLOW, Directions.DOWN, Coord(7, 11), Coord(7, 11), True)
# test_moving_robot(ElementColor.BLUE, Directions.LEFT, Coord(1, 13), Coord(0, 13), True)
# test_moving_robot(ElementColor.RED, Directions.UP, Coord(0, 15), Coord(0, 15), True)
# test_moving_robot(ElementColor.RED, Directions.DOWN, Coord(0, 15), Coord(0, 14), True)
# test_moving_robot(ElementColor.YELLOW, Directions.UP, Coord(7, 11), Coord(7, 15), True)
# test_moving_robot(ElementColor.GREEN, Directions.RIGHT, Coord(7, 10), Coord(15, 10), True)