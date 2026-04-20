import gsClassesMisc as gsClasses    
dict_shapes = {'1': 'square', '2':'rectangle'}
dict_direction = {'1': 'frwd', '2':'rwd', '3':'down', '4':'up'}
# Create a new Canvas object that is 30 units wide by 30 units tall 
canvas = gsClasses.GsCanvas(30, 30)
# Create a new Scribe object passing the canvas and the characters to use
scribe = gsClasses.GsTerminalScribe(canvas, '*', '.')

print("What would you like to draw today?")
print("Pick 1 for Square \nPick 2 for Rectangle")
figure = input()

print("In which direction?")
print("Pick 1 for Forward \nPick 2 for Rewind \nPick 3 for Down \nPick 4 for Up")
direction = input()

input_valid = (figure in dict_shapes) and (direction in dict_direction)

if (input_valid):
    print("Give the width: ")
    width = input()
    print("Give the height: ")
    height = input()
    # Create a new Drawing object with the canvas, scribe and the type of figure.
    shape = gsClasses.GsDrawShapes(canvas, scribe, dict_shapes[figure], dict_direction[direction], int(width), int(height))
    # Draw a small square
    shape.draw_shape()
else:
    print("Invalid options, try again!")



