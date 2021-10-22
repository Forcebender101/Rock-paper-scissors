import random

i = 0
winNoLose = 0
winInRow = 0
winTotal = 0
error = 0

#This picks computer input

while i < 10:
    randomNumber = int(random.random() * 3) + 1
    if (randomNumber == 1):
        computerPick = "Rock"
    elif (randomNumber == 2):
        computerPick = "Paper"
    elif (randomNumber == 3):
        computerPick = "Scissors"
    else:
        print("Something has gone wrong!")
        exit
#This is for player pick and making it so capitalization doesnt matter
    playerPick = input("Enter your choice (Rock, Paper or Scissors):\n")
    string = playerPick

    #This is for exiting

    if string.lower() in ["stop", "quit", "exit", "goodbye", "cya", "bye bye"]:
        goodbyeMessage = int(random.random() * 3) + 1
        if (goodbyeMessage == 1):
            print("Bye Bye!")
        elif (goodbyeMessage == 2):
            print("Goodbye!")
        elif (goodbyeMessage == 3):
            print("See you later!")
        exit()
    print("You picked {0} and I picked {1}".format(playerPick, computerPick))

    #This is for choosing the winner

    if string.lower() in ["r", "rock"]:
        if computerPick == "Rock":
            print("Its a tie!")
            winInRow = 0
        elif computerPick == "Paper":
            print("I'm sorry, you lose.")
            winNoLose = 0
            winInRow = 0
        elif computerPick == "Scissors":
            print("You win, good job!")
            winNoLose = winNoLose + 1
            winInRow = winInRow + 1
            winTotal = winTotal + 1
    elif string.lower() in ["paper", "p"]:
        if computerPick == "Rock":
            print("You win, good job!")
            winNoLose = winNoLose + 1
            winInRow = winInRow + 1
            winTotal = winTotal + 1
        elif computerPick == "Paper":
            print("Its a tie!")
            winInRow = 0
        elif computerPick == "Scissors":
            print("I'm sorry, you lose.")
            winNoLose = 0
            winInRow = 0
    elif string.lower() in ["scissors", "s"]:
        if computerPick == "Rock":
            print("I'm sorry, you lose.")
            winNoLose = 0
            winInRow = 0
        elif computerPick == "Paper":
            print("You win, good job!")
            winNoLose = winNoLose + 1
            winInRow = winInRow + 1
            winTotal = winTotal + 1
        elif computerPick == "Scissors":
            print("Its a tie!")
            winInRow = 0
    else:
        print("Sorry I dont recognize what you said, check your spelling.")
        error = 1

    if winNoLose > 1:
        print("%s without losing" % winNoLose)
    if winInRow > 1:
        print("%s in a row!" % winInRow)
    if error == 0:
        if winTotal > 1 or winTotal == 0:
            print("You have won %s times!" % winTotal)
        elif winTotal == 1:
            print("You have won %s time" % winTotal)
    else:
        error = 0
