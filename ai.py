from playboard import *
import numpy as np

# Like A*, but only H is needed
class GreedyBFS: 
    # Create initial state and goal
    def __init__(self, board:Board, controlled_robot:Robot) -> None:
        self.board = board
        self.robot = controlled_robot
        self.s0 = self.robot.get_coord()
        self.goal = self.board.target.get_coord()
        self.moves = 0
        self.movelist = []
        self.map = np.full((16, 16), np.inf) # if negative, is visited node

    # Cost from the current state to the goal
    # Heuristic
    def h_function(self, state:Coord) -> int: 
        return self.manhattan_distance(state, self.goal)

    # Cost of each move is always one 
    # Cost from initital state to the current state
    def g_function(self) -> int:
        return self.moves 
    
    # Function to minimize
    def f_function(self, state:Coord) -> int:
        return self.h_function(state) + self.g_function()
    
    def manhattan_distance(self, source:Coord, destination:Coord) -> int:
        return abs(destination.x - source.x) + abs(destination.y - source.y)

    def traverse(self, state:Coord) -> None:
        f = np.inf
        
        self.map[state.get_x(), state.get_y()] = -1

        for direction in Directions:
            if not self.board.wall_exists(self.board.get_blocking_wall(self.robot.get_element_color(), direction)):
                # Iterate through every possibe f
                self.board.move(self.robot.get_element_color(), direction, plot = False)
                temp_f = self.f_function(self.robot.get_coord())

                if not self.map[self.robot.get_x(), self.robot.get_y()] == -1:
                    self.map[self.robot.get_x(), self.robot.get_y()] = temp_f
                
                if temp_f < f and not self.map[self.robot.get_x(), self.robot.get_y()] == -1:
                    f = temp_f
                    best_direction = direction
                    self.movelist.append(best_direction.value)

            # Reset
            self.robot.set_coord(state.x, state.y)

        self.board.move(self.robot.get_element_color(), best_direction, plot = True)
        self.moves += 1

# "A*" considering the distance as the g function
# ONLY G CHANGES
class A_star:
    # Create initial state and goal
    def __init__(self, board:Board, controlled_robot:Robot) -> None:
        self.board = board
        self.robot = controlled_robot
        self.s0 = self.robot.get_coord()
        self.goal = self.board.target.get_coord()
        self.moves = 0
        self.movelist = []
        self.map = np.full((16, 16), np.inf) # if negative, is visited node

    # Cost from the current state to the goal
    # Heuristic
    def h_function(self, state:Coord) -> int: 
        return self.manhattan_distance(state, self.goal)

    # Cost of each move is always one 
    # Cost from initital state to the current state
    def g_function(self, state:Coord) -> int:
        return self.manhattan_distance(self.s0, state)
    
    # Function to minimize
    def f_function(self, state:Coord) -> int:
        return self.h_function(state) + self.g_function(state)
    
    def manhattan_distance(self, source:Coord, destination:Coord) -> int:
        return abs(destination.x - source.x) + abs(destination.y - source.y)

    def traverse(self, state:Coord) -> None:
        f = np.inf
        
        self.map[state.get_x(), state.get_y()] = -1

        for direction in Directions:
            if not self.board.wall_exists(self.board.get_blocking_wall(self.robot.get_element_color(), direction)):
                # Iterate through every possibe f
                self.board.move(self.robot.get_element_color(), direction, plot = False)
                temp_f = self.f_function(self.robot.get_coord())

                if not self.map[self.robot.get_x(), self.robot.get_y()] == -1:
                    self.map[self.robot.get_x(), self.robot.get_y()] = temp_f
                
                if temp_f < f and not self.map[self.robot.get_x(), self.robot.get_y()] == -1:
                    f = temp_f
                    best_direction = direction
                    self.movelist.append(best_direction.value)

            # Reset
            self.robot.set_coord(state.x, state.y)

        self.board.move(self.robot.get_element_color(), best_direction, plot = True)
        self.moves += 1

class DFS:
    def __init__(self, board:Board, controlled_robot:Robot) -> None:
        self.board = board
        self.robot = controlled_robot
        self.s0 = self.robot.get_coord()
        self.cost = 0
        self.moves = 0
        self.movelist = []
        self.map = np.full((16, 16), np.inf)

    def traverse(self, state:Coord) -> None:
        self.map[state.get_x(), state.get_y()] = -1

        for direction in Directions:
            if not self.board.wall_exists(self.board.get_blocking_wall(self.robot.get_element_color(), direction)):
                # Iterate through every possibe f
                self.board.move(self.robot.get_element_color(), direction, plot = False)
                self.moves += 1
                self.cost += 1
                print("Cost: " + str(self.cost))
                self.movelist.append(direction)

                if not self.map[self.robot.get_x(), self.robot.get_y()] == -1: 
                    self.traverse(self.robot.get_coord())
                else:
                    # Reset
                    self.moves -= 1
                    self.movelist.pop()
                    self.robot.set_coord(state.x, state.y)
            
            if self.board.finished:
                return