#   Python:     3.10.2
#
#   Author:     Jeremy DeLain
#
#   Purpose:    TTA - Python Course, Creating our first program together.
#               Demonsttrating how to pass variables from function to function
#               while producing a funcional game



def start(nice = 0, mean = 0, name = ""):
    #get user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
        check if this is a new game or not
        if it is new, get the user's name
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger blushes...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger steps into traffic...")
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) #pass the 3 variables to the score()

def show_score(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    if mean >2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    print("\nNice job {}, you win! \nEveryone is chanting your name. \nYou are a god. You cannot die.".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    print("\nAhhhhh too bad, game over! \n{}, everyone thinks you stink, \nand they are correct!".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nGood bye!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', (N) for 'NO':\n>>> ")
            
def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)


if __name__ == "__main__":
    start()
