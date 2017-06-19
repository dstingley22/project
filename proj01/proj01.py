# Name:Damian Stingley
# Date:6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!


name=raw_input('Enter your name ')
age = int(raw_input('How old are you '))
birth = raw_input('have you already had your birthday this year ')
if birth == 'no':
    print name, ', if you somehow make it this long, you will be 100 years old in ', (2017-age+99)
elif birth == 'yes':
    print name, ', if you somehow make/made it this long, you will be 100 years old in ', (2017-age+100)
if age > 17:
    print 'you can watch whatever you like ;0'
elif age > 12:
    print 'you can watch anything except for R rated movies :|'
elif age > 5:
    print 'you can watch PG and G stuff :('
else:
    print 'you can only watch G :( :('
if name == 'Damian':
    print 'you are the GOAT'