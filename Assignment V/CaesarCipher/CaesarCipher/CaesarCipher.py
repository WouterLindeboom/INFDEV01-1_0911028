string = raw_input("Enter a word to decode: ")
key = int(raw_input("Enter a key: "))
encodedString = ""
string = string.lower()


for character in string:
    if character.isalpha():
        result = ord(character) + key
        if result > 122:
            abovez = result - 122
            character = 96 + abovez
            char = chr(character)
        else:
            char = chr(ord(character) + key)
    encodedString += char


print(encodedString)