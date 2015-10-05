input = raw_input("Text to reverse: ")
location = 0
output = ""

while location < len(input):
    output = input[location] + output
    location+=1
print output