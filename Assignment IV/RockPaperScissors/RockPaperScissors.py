while True:
    player1 = raw_input("Player one, choose either Rock, Paper or Scissors: ").lower()
    player2 = raw_input("Player two, choose either Rock, Paper or Scissors: ").lower()
    p1v = 0
    p2v = 0

    if player1 == "rock" or player1 == "paper" or player1 == "scissors":
        p1v = 1
    else:
        print "Player 1, %s is not an accepted value." % (player1)

    if player2 == "rock" or player2 == "paper" or player2 == "scissors":
        p2v = 1
    else:
        print "Player 2, %s is not an accepted value." % (player2)

    if p1v == 1 and p2v == 1:
        if player1 == player2:
            print "%s and %s, it's a draw!" % (player1, player2)

        elif player1 == "rock" and player2 == "paper":
            print "Paper wraps around rock, Player 2 wins!"
        elif player1 == "rock" and player2 == "scissors":
            print "Rock beats scissors, Player 1 wins!"
        elif player1 == "paper" and player2 == "rock":
            print "Paper wraps around rock, Player 1 wins!"
        elif player1 == "paper" and player2 == "scissors":
            print "Scissors cut paper, Player 2 wins!"
        elif player1 == "scissors" and player2 == "rock":
            print "Rock beats scissors, Player 2 wins!"
        elif player1 == "scissors" and player2 == "paper":
            print "Scissors cut paper, Player 1 wins!"


    else:
        print "Nope"