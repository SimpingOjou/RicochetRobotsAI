from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum
import string

class ElementColor(Enum):
    RED="red"
    GREEN="green"
    YELLOW="orange"
    BLUE="blue"
    VIOLET="violet"

class Directions(Enum):
    UP="UP"
    DOWN="DOWN"
    LEFT="LEFT"
    RIGHT="RIGHT"
    
class Orientation(Enum):
    HORIZONTAL=0
    VERTICAL=1

class Coord():
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        
    def __eq__(self, other: Coord) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: Coord) -> bool:
        return not self.__eq__(other)
    
    def __add__(self, other: Coord) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)
    
    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def __str__(self) -> str:
        return "({},{})".format(self.get_x(), self.get_y())

class Wall():
    def __init__(self, x: int = 0, y: int = 0, ori: Orientation = Orientation.HORIZONTAL):
        self._coord = Coord(x,y)
        self._orientation = ori

    def __eq__ (self, other: Coord):
        return self.get_coord() == other.get_coord() and self.get_orientation() is other.get_orientation()

    def __ne__ (self, other: Coord):
        return not self.__eq__(other)
    
    def is_horizontal(self) -> bool:
        return self.get_orientation() == Orientation.HORIZONTAL
    
    def is_vertical(self) -> bool:
        return not self.is_horizontal()
    
    def is_coord_equal(self, other: Coord) -> bool:
        return self.coord == other.coord
    
    def get_x(self) -> int:
        return self.get_coord().get_x()
    
    def get_y(self) -> int:
        return self.get_coord().get_y()
    
    def get_coord(self) -> Coord:
        return self._coord

    def add_coord(self, coord: Coord):
        self._coord += coord
        return    
    
    def get_orientation(self) -> Orientation:
        return self._orientation
    
    def __str__(self):
        return "Wall coordinates: {}, orientation: {}".format(self.get_coord().__str__(), self.get_orientation())

class BoardElement():
    def __init__(self, name = "Element", x: int = 0, y: int = 0, color: ElementColor = None):
        self._name = name
        self._coord = Coord(x,y)
        self._color = color

    def __eq__ (self, other) -> bool:
        return self.get_coord() == other.get_coord() and self.get_color() == other.get_color()

    def __ne__ (self, other) -> bool:
        return not self.__eq__(other)
    
    def is_coord_equal(self, other) -> bool:
        return self.get_coord() == other.get_coord()
    
    def get_x(self) -> int:
        return self.get_coord().get_x()
    
    def get_y(self) -> int:
        return self.get_coord().get_y()
    
    def add_coord(self, coord: Coord):
        self._coord += coord
        return
    
    def get_coord(self) -> Coord:
        return self._coord
    
    def get_color(self) -> string:
        return self._color.value
    
    def __str__(self):
        return "{} coordinates: {}, color: {}".format(self._name, self.get_coord().__str__(), self.get_color())
    
    def set_coord(self, x, y) -> None:
        self._coord = Coord(x,y)
    
class Robot(BoardElement):
    def __init__(self, x: int, y: int, color: ElementColor):
        super().__init__("Robot", x, y, color)

class Target(BoardElement):
    def __init__(self, x: int, y: int, color: ElementColor):
        super().__init__("Target", x, y, color)

class Board():
    def __init__(self):
        self.height = 16
        self.width = 16
        self.walls = [Wall(5,0,Orientation.VERTICAL),
                      Wall(12,0,Orientation.VERTICAL),
                      Wall(3,1),
                      Wall(4,1,Orientation.VERTICAL),
                      Wall(10,1,Orientation.VERTICAL),
                      Wall(2,2,Orientation.VERTICAL),
                      Wall(10,2),
                      Wall(15,2,Orientation.VERTICAL),
                      Wall(2,3),
                      Wall(8,3,Orientation.VERTICAL),
                      Wall(14,3),
                      Wall(9,4),
                      Wall(10,4,Orientation.VERTICAL), 
                      Wall(15,4),
                      Wall(0,5),
                      Wall(6,5,Orientation.VERTICAL),
                      Wall(4,6),
                      Wall(4,6,Orientation.VERTICAL),
                      Wall(13,6),
                      Wall(13,6,Orientation.VERTICAL),
                      Wall(7,7),
                      Wall(7,7,Orientation.VERTICAL),
                      Wall(8,7),
                      Wall(9,7,Orientation.VERTICAL),
                      Wall(7,8,Orientation.VERTICAL),
                      Wall(9,8,Orientation.VERTICAL),
                      Wall(1,9,Orientation.VERTICAL),
                      Wall(7,9),
                      Wall(8,9),
                      Wall(12,9),
                      Wall(12,9,Orientation.VERTICAL),
                      Wall(7,10),
                      Wall(7,10,Orientation.VERTICAL),
                      Wall(0,11),
                      Wall(3,11,Orientation.VERTICAL),
                      Wall(15,11,Orientation.VERTICAL),
                      Wall(9,12,Orientation.VERTICAL),
                      Wall(14,12),
                      Wall(5,13),
                      Wall(6,13,Orientation.VERTICAL),
                      Wall(9,13),
                      Wall(13,14),
                      Wall(14,14,Orientation.VERTICAL),
                      Wall(15,14),
                      Wall(4,15,Orientation.VERTICAL),
                      Wall(10,15,Orientation.VERTICAL)]
        
        for i in range(self.width + 1):
            self.walls.append(Wall(i, 0))
            self.walls.append(Wall(i, self.height))
        for i in range(self.height + 1):
            self.walls.append(Wall(0, i, Orientation.VERTICAL))
            self.walls.append(Wall(self.width, i, Orientation.VERTICAL))
            
        self.robots = { 
            ElementColor.RED: Robot(0, 15, ElementColor.RED), 
            ElementColor.BLUE: Robot(1, 13, ElementColor.BLUE),
            ElementColor.YELLOW: Robot(7, 11, ElementColor.YELLOW),
            ElementColor.GREEN: Robot(14, 5, ElementColor.GREEN)
        }
        self.target = Target(6, 7, ElementColor.VIOLET)
        self.plotter = Figure()
        
    def get_robot(self, robot_color: ElementColor) -> Robot:
        return self.robots[robot_color]
    
    def plot(self, pause: float = 0.3, block: bool = False):
        self.plotter.plot(self.height, self.width, self.target, self.robots, self.walls, pause, block)
        
    def wall_exists(self, wall: Wall) -> bool:
        return wall in self.walls
    
    def robot_exists(self, coord: Coord) -> bool:
        return len(list(filter(lambda robot: robot.get_coord() == coord, self.robots.values()))) > 0
    
    def move(self, robot: Robot, direction: Directions, plot=True):
        moving_coord = Coord((Directions.LEFT == direction)*(-1) + (Directions.RIGHT == direction)*(1),
                            (Directions.DOWN == direction)*(-1) + (Directions.UP == direction)*(1))
        blocking_wall_orientation = (Orientation.VERTICAL if direction in [Directions.LEFT, Directions.RIGHT]
                                else Orientation.HORIZONTAL)
        robot_to_move = self.robots[robot]
        blocking_wall_x = moving_coord.get_x() + robot_to_move.get_coord().get_x() + 1 * (direction == Directions.LEFT)
        blocking_wall_y = moving_coord.get_y() + robot_to_move.get_coord().get_y() + 1 * (direction == Directions.DOWN)
        blocking_wall = Wall(blocking_wall_x, blocking_wall_y, blocking_wall_orientation)

        while (not self.wall_exists(blocking_wall) and not self.robot_exists(robot_to_move.get_coord() + moving_coord)):
            robot_to_move.add_coord(moving_coord)
            blocking_wall.add_coord(moving_coord)
            if (plot):
                self.plot()

class Figure():
    def __init__(self):
        self.fig, self.ax = plt.subplots()

    def plot(self, height:int, width:int, target:Target, robots:Robot, walls:Wall, pause:float, block:bool):
        # plot target
        self.ax.scatter(target.get_x() + 0.5, target.get_y() + 0.5, color=target.get_color(), marker='*', s=150)

        # plot robots
        for robot in robots.values():
            self.ax.scatter(robot.get_x() + 0.5, robot.get_y() + 0.5, c=robot.get_color(), linewidths=0.5, edgecolors='black')
        
        # plot walls
        for wall in walls:
            coord_start = [wall.get_x(), wall.get_x() + int(wall.is_horizontal())]
            coord_end = [wall.get_y(), wall.get_y() + int(wall.is_vertical())]
            self.ax.plot(coord_start, coord_end, c="black")
        
        # hide tick labels and dashes
        self.ax.set(xlim=(0, width), xticks=np.arange(1, width), xticklabels=[],
            ylim=(0, height), yticks=np.arange(1, height), yticklabels=[])
        self.ax.tick_params(axis='y', colors='white')
        self.ax.tick_params(axis='x', colors='white')
        plt.title("Ricochet Robots")
        self.ax.grid(True)
        
        if block:
            plt.show(block=True)
            self.__init__()
        else: 
            plt.draw()
            self.fig.canvas.flush_events()
            plt.pause(pause)
            self.ax.cla()
        