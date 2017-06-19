# Name:Damian Stingley
# Date:6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name=raw_input('Enter your name ')
age = int(raw_input('How old are you '))
print(2017-age+100)
if age == 10:
    print "you're 10"
elif age == 20:
    print "you're 20"
else:
    print "you're not 10 or 20."