height = int(raw_input("Height: "))
width = int(raw_input("Width: "))

square = ""
for y in range(0, height):
    for x in range(0, width):
        square += "*"
    square += "\n"
print square