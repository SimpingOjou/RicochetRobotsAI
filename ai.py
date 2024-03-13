from playboard import *
import numpy as np

class A_star:
    # Create initial state and goal
    def __init__(self, board:Board, controlled_robot:Robot) -> None:
        self.board = board
        self.robot = controlled_robot
        self.s0 = self.robot.get_coord()
        self.goal = self.board.target.get_coord()
        self.moves = 0

    def h_function(self, state:Coord) -> int:
        return self.manhattan_distance(state, self.goal)

    def g_function(self) -> int:
        return self.moves # cost of each move is always one
    
    def f_function(self, state:Coord):
        return self.h_function(state) + self.g_function(state)
    
    def manhattan_distance(self, source:Coord, destination:Coord) -> int:
        return abs(destination.x - source.x) + abs(destination.y - source.y)

    def traverse(self, state:Coord) -> None:
        f = np.inf

        for direction in Directions:
            # Iterate through every possibe f
            self.board.move(self.robot, direction, plot = False)
            
            temp_f = self.f_function(self.robot.get_coord())
            if f > temp_f:
                f = temp_f
                best_direction = direction

            # Reset
            self.robot.set_coord(state.x, state.y)

        self.board.move(self.robot, best_direction, plot = True)
        self.moves += 1
