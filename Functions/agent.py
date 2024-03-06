from __future__ import annotations
from enum import Enum

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
    