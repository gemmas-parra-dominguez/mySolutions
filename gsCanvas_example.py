import gsClassesMisc as gsClasses    
dict_shapes = {'1': 'square', '2':'rectangle'}
dict_direction = {'1': 'fwrd', '2':'rwd'}
# Create a new Canvas object that is 30 units wide by 30 units tall 
canvas = gsClasses.GsCanvas(30, 30)
# Create a new Scribe object passing the canvas and the characters to use
scribe = gsClasses.GsTerminalScribe(canvas, '*', '.')
print("What would you like to draw today?")
print("Pick 1 for Square \nPick 2 for Rectangle")
shape = input()
print("In which direction?")
print("Pick 1 for Forward \nPick 2 for Rewind")
direction = input()
# Create a new Drawing object with the canvas, scribe and the type of figure.
shape = gsClasses.GsDrawShapes(canvas, scribe, dict_shapes[shape], dict_direction[direction], 7, 3)
# Draw a small square
shape.draw_shape()



