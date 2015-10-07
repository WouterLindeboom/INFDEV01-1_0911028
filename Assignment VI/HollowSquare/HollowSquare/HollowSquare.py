height = int(raw_input("Height: ")) #10 15 makes a nice square.
width = int(raw_input("Width: "))
figureString = ""

for y in range(0, height):
    if (y == 0 or y == (height - 1) ):
        for x in range(0, width):
            figureString += "*"
    else:
        for x in range(0, width):
            if (x == 0 or x == (width - 1) ):
                figureString += "*"
            else:
                figureString += " "
    figureString += "\n"
print(figureString)