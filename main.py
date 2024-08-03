import random
Pwins=0
Cwins=0
print("""Welcome to Morra! In this game, you'll decide how many fingers
    to hold up (from one hand) and then the computer will randomly
    do the same. You'll need to guess the total number of fingers
    to win the round, before seeing how many fingers the computer
    has decided to hold up!
    """)
name=input("What is your name?\n")
rounds= int(input("How many rounds would you like to play? ex:1,3,5\n"))
currentRounds=0
while rounds > currentRounds:
    currentRounds+=1
    Pfingers=int(input("How many fingers would you like to hold up?\n"))
    if Pfingers>5:
        print(str(Pfingers)+" fingers is an invalid amount. Must be 5 or less")
        continue
    Cfingers=random.randint(1,5)
    total=Pfingers+Cfingers
    Pguess=int(input("What do you think the total will be?\n"))
    if Pguess>10:
        print("Guess must be below 10")
        continue
    Cguess=Cfingers+random.randint(1,5)
    print(f"The computer held up {str(Cfingers)} and guessed {str(Cguess)}")
    print(f"The total was {Pfingers+Cfingers}.")
    if Pguess !=total and Cguess !=total:
        print("No one wins!")
    elif Pguess==total and Cguess==total:
        print("It's a tie!")
        Pwins+=1
        Cwins+=1
    elif Pguess==total:
        print(f"{name} wins!")
        Pwins+=1
    else:
        print("Computer wins!")
        Cwins+=1
    print(f"Round {currentRounds}/{rounds} over")
print(f"Results:\n----------\n{name}:{Pwins}\nComputer:{Cwins}\n----------\nThanks for playing!")
