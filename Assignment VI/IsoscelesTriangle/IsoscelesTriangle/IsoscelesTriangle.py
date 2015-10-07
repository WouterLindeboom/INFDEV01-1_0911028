height = int(raw_input("Please fill in a number: "))
output = ""
for currentRow in range(0, height):                                                                           # For each row in range of the height entered
    width = (height * 2)
    for currentLocation in range(1, width):                                                                   # For each character in row between 1 and entered height times two
        if currentLocation - height + currentrow < 0 or currentLocation - height - currentrow > 0:            # If current character location - height + current row is below 0 |OR| curcharloc - height - currow is above 0
            output += "."                                                                                     # Add a space to the row
        else :      
            output += "*"                                                                                     # Add an asterisk to the row
    output += "\n"                                                                                            # New line after every row
print(output)                                                                                                 # Print the thing