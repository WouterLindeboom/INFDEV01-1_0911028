height = int(raw_input("Height: "))
output = ""

for row in range(0, height + 1):
    output += "*" * row
    output += "\n"
print output