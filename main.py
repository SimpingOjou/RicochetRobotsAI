import sys
sys.path.append(".\Functions")
from Functions import *

def test_moving_robot(robot: ElementColor, direction: Directions, start_coord: Coord, end_coord: Coord, plot=False):
    assert board.get_robot(robot).get_coord() == start_coord, f"expected starting coord {start_coord} but got {board.get_robot(robot).get_coord()} instead"
    board.move(robot, direction, plot)
    assert board.get_robot(robot).get_coord() == end_coord, f"expected ending coord {end_coord} but got {board.get_robot(robot).get_coord()} instead"

board = Board()
board.plot()

test_moving_robot(ElementColor.GREEN, Directions.LEFT, Coord(12, 10), Coord(7, 10), True)
test_moving_robot(ElementColor.YELLOW, Directions.DOWN, Coord(7, 11), Coord(7, 11), True)
test_moving_robot(ElementColor.BLUE, Directions.LEFT, Coord(1, 13), Coord(0, 13), True)
test_moving_robot(ElementColor.RED, Directions.UP, Coord(0, 15), Coord(0, 15), True)
test_moving_robot(ElementColor.RED, Directions.DOWN, Coord(0, 15), Coord(0, 14), True)
test_moving_robot(ElementColor.YELLOW, Directions.UP, Coord(7, 11), Coord(7, 15), True)
test_moving_robot(ElementColor.GREEN, Directions.RIGHT, Coord(7, 10), Coord(15, 10), True)