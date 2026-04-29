import gsDrawShapes as gsClasses

dict_shapes = {'1': 'Square', '2':'Rectangle'}
dict_direction = {'1': 'Forward', '2':'Rewind', '3':'Down', '4':'Up'}

# Create a new Canvas object that is 30 units wide by 30 units tall
canvas_size = 30

# Create a new Drawing object with the canvas, scribe and the type of figure.
shape = gsClasses.GsDrawShapes(canvas_size, canvas_size, True)

print("What would you like to draw today?")
print("Pick 1 for Square \nPick 2 for Rectangle \nPick 3 for Triangle")
figure = input()

print("In which direction?")
print("Pick 1 for Forward \nPick 2 for Rewind \nPick 3 for Down \nPick 4 for Up")
direction = input()

input_valid = (figure in shape._dict_shapes) and (direction in shape._dict_direction)

if (input_valid):
    print(f"Give the width (max. value is {str(canvas_size)}): ")
    width = input()
    if (figure == '1' or figure == '3'):
        height = width
    else:        
        print(f"Give the height (max. value is {str(canvas_size)}): ")
        height = input()
    
    # Draw a small square
    shape.draw_shape(figure, direction, int(width), int(height))
else:
    print("Invalid options, try again!")



