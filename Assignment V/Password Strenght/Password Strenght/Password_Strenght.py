while 1==1:
    input = raw_input("Enter password to test: ")
    score = 0
    uppercase = 0
    lowercase = 0
    numbers = 0
    special = 0
    passwordstrenght = "weak"


    for character in input:
        if character.isdigit():
            score += 2
            numbers += 1
        elif character.isupper():
            score += 2
            uppercase += 1
        elif character.isalpha():
            score += 1
            lowercase += 1
        else:
            score += 2
            special += 1

    if special > 0 and numbers > 0 and uppercase > 0 and lowercase > 0:
        score += 5

    if len(input) < 10:
        score += (len(input) / 10) * 2
    else:
        score += 4

    if score > 10 and score <= 20:
        passwordstrenght = "medium"
    elif score > 20:
        passwordstrenght = "strong"
    print("Your passsword is %s") % (passwordstrenght) 