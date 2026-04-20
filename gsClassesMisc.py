import os
import time
from termcolor import colored

# This is the GsCanvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribe is moving.
class GsCanvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        # This is a grid that contains data about where the 
        # TerminalScribe has visited.
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hits_wall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    # Set the given position to the provided character on the canvas
    def set_position(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

# This is the GsTerminalScribe class.
class GsTerminalScribe:
    def __init__(self, canvas, mark, trail):
        self.canvas = canvas
        self.trail = trail
        self.mark = mark
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hits_wall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hits_wall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hits_wall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hits_wall(pos):
            self.draw(pos)

    def draw(self, pos):
        # Set the old position to the "trail" symbol
        self.canvas.set_position(self.pos, colored(self.trail, 'red'))
        # Update position
        self.pos = pos
        # Set the new position to the "mark" symbol
        self.canvas.set_position(self.pos, colored(self.mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

# This is the GsDrawShapes class.
class GsDrawShapes:    
    def __init__(self, canvas, scribe, *args):        
        self._canvas = canvas
        self._scribe = scribe
        self._shape = args[0]
        self._dir = args[1]

        if (self._shape == 'square'):
            self._width = args[2] - 1
            self._height = args[2] - 1
        else: #(self._shape == 'rectangle')
            self._width = args[2] - 1
            self._height = args[3] - 1

        if (self._dir == 'rwd' ):
            self._scribe.pos = [self._width, 0]
        if (self._dir == 'up'):
            self._scribe.pos = [self._width, self._height]

    def draw_shape(self):
        if (self._dir == 'frwd'):
            self.draw_frwd()
        elif (self._dir == 'rwd'):
            self.draw_rwd()
        elif (self._dir == 'down'):
            self.draw_down()
        else: # (self._dir == 'up')
            self.draw_up()

    def draw_frwd(self):
        for times in range(self._width):
            self._scribe.right()
        for times in range(self._width):
            self._scribe.down()
        for times in range(self._width):
            self._scribe.left()
        for times in range(self._width):
            self._scribe.up()

    def draw_rwd(self):
        for times in range(self._width):
            self._scribe.left()
        for times in range(self._width):
            self._scribe.down()
        for times in range(self._width):
            self._scribe.right()
        for times in range(self._width):
            self._scribe.up()  
    
    def draw_down(self):
        for times in range(self._height):
            self._scribe.down()
        for times in range(self._width):
            self._scribe.right()
        for times in range(self._height):
            self._scribe.up()
        for times in range(self._width):
            self._scribe.left()
    
    def draw_up(self):
        for times in range(self._height):
            self._scribe.up()
        for times in range(self._width):
            self._scribe.left()
        for times in range(self._height):
            self._scribe.down()
        for times in range(self._width):
            self._scribe.right()