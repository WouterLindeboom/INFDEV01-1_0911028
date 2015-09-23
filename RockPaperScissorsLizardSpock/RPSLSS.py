while True:
    player1 = raw_input("Player one, choose either Rock, Paper, Scissors, Lizard or Spock: ").lower()
    player2 = raw_input("Player two, choose either Rock, Paper, Scissors, Lizard or Spock: ").lower()

    p1v = 0
    p2v = 0

    if player1 == "rock" or player1 == "paper" or player1 == "scissors" or player1 == "lizard" or player1 == "spock":
        p1v = 1
    else:
        print "Player 1, %s is not an accepted value." % (player1)

    if player2 == "rock" or player2 == "paper" or player2 == "scissors" or player2 == "lizard" or player2 == "spock":
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
        elif player1 == "lizard" and player2 == "rock":
            print "Rock crushes lizard, Player 2 wins!"
        elif player1 == "lizard" and player2 == "paper":
            print "Lizard eats paper, Player 1 wins!"
        elif player1 == "lizard" and player2 == "scissors":
            print "Scissors decapacitate lizard, Player 2 wins!"
        elif player1 == "lizard" and player2 == "spock":
            print "Lizard poisons spock, Player 1 wins!"
        elif player1 == "spock" and player2 == "rock":
            print "Spock vaporizes rock, Player 1 wins!"
        elif player1 == "spock" and player2 == "paper":
            print "Paper disproves spock, Player 2 wins!"
        elif player1 == "spock" and player2 == "scissors":
            print "Spock smashes scissors, Player 1 wins!"
        elif player1 == "spock" and player2 == "lizard":
            print "Lizard poisons spock, Player 2 wins!" 
        elif player1 == "rock" and player2 == "spock":
            print "Spock vaporizes rock, Player 2 wins!"
        elif player1 == "paper" and player2 == "spock":
            print "Paper disproves spock, Player 1 wins!"
        elif player1 == "scissors" and player2 == "spock":
            print "Spock smashes scissors, Player 2 wins!"
        elif player1 == "paper" and player2 == "lizard":
            print "Lizard eats paper, Player 2 wins!"
        elif player1 == "rock" and player2 == "lizard":
            print "Rock crushes lizard, Player 1 wins!" 
        elif player1 == "scissors" and player2 == "lizard":
            print "Scissors decapacitate lizard, Player 1 wins!"
        elif player1 == "spock" and player2 == "lizard":
            print "Lizard poisons spock, Player 2 wins!"
         


    else:
        print "Nope"