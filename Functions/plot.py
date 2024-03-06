from __future__ import annotations
import matplotlib.pyplot as plt
import numpy as np

def plot(height, width, target, robots, walls):
    fig, ax = plt.subplots()
    
    # plot target
    ax.scatter(target.get_x() + 0.5, target.get_y() + 0.5, color=target.get_color(), marker='*', s=150)

    # plot robots
    for robot in robots.values():
        ax.scatter(robot.get_x() + 0.5, robot.get_y() + 0.5, c=robot.get_color(), linewidths=0.5, edgecolors='black')
    
    # plot walls
    for wall in walls:
        coord_start = [wall.get_x(), wall.get_x() + int(wall.is_horizontal())]
        coord_end = [wall.get_y(), wall.get_y() + int(wall.is_vertical())]
        ax.plot(coord_start, coord_end, c="black")
    
    # hide tick labels and dashes
    ax.set(xlim=(0, width), xticks=np.arange(1, width), xticklabels=[],
           ylim=(0, height), yticks=np.arange(1, height), yticklabels=[])
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='x', colors='white')
    
    # show grid
    ax.grid(True)
    
    plt.show()