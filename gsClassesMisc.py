import os
import time
from termcolor import colored

# This is the GsCanvas class. It defines some height and width, and a 
# matrix of characters to keep track of where the TerminalScribe is moving.
class GsCanvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # This is a grid that contains data about where the 
        # TerminalScribe has visited.
        self.canvas = [[' ' for y in range(self.height)] for x in range(self.width)]

    # Returns True if the given point is outside the boundaries of the Canvas
    def hits_wall(self, point):
        return point[0] < 0 or point[0] >= self.width or point[1] < 0 or point[1] >= self.height

    # Set the given position to the provided character on the canvas
    def set_position(self, pos, mark):
        self.canvas[pos[0]][pos[1]] = mark

    # Clear the terminal (used to create animation)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Clear the terminal and then print each line in the canvas
    def print(self):
        self.clear()
        for y in range(self.height):
            print(' '.join([col[y] for col in self.canvas]))

# This is the GsTerminalScribe class.
class GsTerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.framerate = 0.2
        self.position = [0, 0]

    def up(self):
        pos = [self.position[0], self.position[1]-1]
        if not self.canvas.hits_wall(pos):
            self.draw(pos, '^')

    def down(self):
        pos = [self.position[0], self.position[1]+1]
        if not self.canvas.hits_wall(pos):
            self.draw(pos, 'v')

    def right(self):
        pos = [self.position[0]+1, self.position[1]]
        if not self.canvas.hits_wall(pos):
            self.draw(pos, '>')

    def left(self):
        pos = [self.position[0]-1, self.position[1]]
        if not self.canvas.hits_wall(pos):
            self.draw(pos, '<')

    def draw(self, pos, trail='.', mark='*'):
        # Set the old position to the "trail" symbol
        self.canvas.set_position(self.position, colored(trail, 'red'))
        # Update position
        self.position = pos
        # Set the new position to the "mark" symbol
        self.canvas.set_position(self.position, colored(mark, 'red'))
        # Print everything to the screen
        self.canvas.print()
        # Sleep for a little bit to create the animation
        time.sleep(self.framerate)

# This is the GsDrawShapes class.
class GsDrawShapes:    
    def __init__(self, canvas, scribe, *args):        
        self.canvas = canvas
        self.scribe = scribe
        self.shape = args[0]
        self.direction = args[1]

        if (self.shape == 'square'):
            self.w = args[2] - 1
            self.h = args[2] - 1
        else: #(self.shape == 'rectangle')
            self.w = args[2] - 1
            self.h = args[3] - 1

        if (self.direction == 'rwd' ):
            self.scribe.position = [self.w, 0]
        if (self.direction == 'up'):
            self.scribe.position = [self.w, self.h]

    def draw_shape(self):
        if (self.direction == 'frwd'):
            self.draw_frwd()
        elif (self.direction == 'rwd'):
            self.draw_rwd()
        elif (self.direction == 'down'):
            self.draw_down()
        else: # (self.direction == 'up')
            self.draw_up()
        self.print_info()

    def print_info(self):
        print(f"Canva size is [{self.canvas.width}, {self.canvas.height}]")
        print(f"Printed shape is {self.shape}")
        print(f"Printed direction was {self.direction}")
        print(f"Shape size is [{self.w + 1}, {self.h + 1}]")

    def draw_frwd(self):
        for times in range(self.w):
            self.scribe.right()
        for times in range(self.w):
            self.scribe.down()
        for times in range(self.w):
            self.scribe.left()
        for times in range(self.w):
            self.scribe.up()

    def draw_rwd(self):
        for times in range(self.w):
            self.scribe.left()
        for times in range(self.w):
            self.scribe.down()
        for times in range(self.w):
            self.scribe.right()
        for times in range(self.w):
            self.scribe.up()  
    
    def draw_down(self):
        for times in range(self.h):
            self.scribe.down()
        for times in range(self.w):
            self.scribe.right()
        for times in range(self.h):
            self.scribe.up()
        for times in range(self.w):
            self.scribe.left()
    
    def draw_up(self):
        for times in range(self.h):
            self.scribe.up()
        for times in range(self.w):
            self.scribe.left()
        for times in range(self.h):
            self.scribe.down()
        for times in range(self.w):
            self.scribe.right()