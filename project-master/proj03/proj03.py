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
    print var
    y = int(raw_input("How many guesses would you like to have?"))
    x = int(raw_input("Guess a number between 1 and 1000"))
    var2 = 6-y
    while x != var and var2 < 5:
        if x != 'exit':
            x = int(x)
            if x == var:
                print "Correct.  The answer is", var
            if x > var:
                x = raw_input("Too high.  Guess again")
                if x == var:
                    print 'Correct. The answer is', var
                #else:
                 #   print "Game over. The answer is", var
            elif x < var:
                x = raw_input("Too low.  Guess again")
                if x == var:
                    print 'Correct. The answer is', var
            elif x == 'exit':
                x = var
                print "Game over.  The answer is", var
 #           if x == var:
#                print "Correct.  The answer is", var
            elif var2 == 5:
                if x == var:
                    print 'Correct. The answer is', var
                else:
                    print "Game over. The answer is", var
        var2 = var2 + 1
    var3 = raw_input("Game over, would you like to play again?")