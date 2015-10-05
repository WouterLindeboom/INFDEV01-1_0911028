string = raw_input("Enter a word to decode: ")
key = int(raw_input("Enter a key: "))
encodedString = ""

for character in string:
    if character.isalpha():
        character = chr(ord(character) + key)
    encodedString += character

print(encodedString)