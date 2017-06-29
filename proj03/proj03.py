# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

var3 = 'yes'
while var3 == 'yes':
    import random
    var = random.randint(1,1000)
    #print var
    y = int(raw_input("How many guesses would you like to have?")) - 1
    x = int(raw_input("Guess a number between 1 and 1000 or type 0 to quit: "))
    while  y > 0:
        if x != 0:
            x = int(x)
            if x > var:
                print ""
                x = raw_input("Too high.  Guess again")
            elif x < var:
                print ""
                x = raw_input("Too low.  Guess again")
            elif x == 'exit':
                x = var
                print "Game over.  The answer is", var
                break
            if x == var:
                 print "Correct.  The answer is", var
                 break
        else:
            if x == var:
                print 'Correct. The answer is', var
                break
            else:
                print "Game over. The answer is", var
                break
        y = y - 1
    var3 = raw_input("Would you like to play again?")