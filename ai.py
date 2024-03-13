from playboard import *

class a_star:
    # Create initial state and goal
    def __init__(self, board:Board, controlled_robot:Robot) -> None:
        self.s0 = controlled_robot.get_coord()
        self.goal = board.target.get_coord()
        self.moves = 0
        self.current_heuristic = self.manhattan_distance(self.s0, self.goal)

    def h_function(self, state:Coord) -> int:
        return self.manhattan_distance(state, self.goal)

    def g_function(self, state:Coord) -> int:
        return self.manhattan_distance(self.s0, state)
    
    def f_function(self, state):
        return self.h_function(state) + self.g_function(state)
    
    def manhattan_distance(self, source:Coord, destination:Coord) -> int:
        return abs(destination.x - source.x) + abs(destination.y - source.y)
