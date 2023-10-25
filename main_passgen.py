'''This program is meant to generate a password for the user. To do this they would have to
first input how long they need the password at a minimum of 5 characters long. This project is to
help with security and privacy. A lot of times people don't know that personal information in passwords
can jeapordize their privacy. I hope it helps
Author: [Andrew Dana]
'''

import characters as ch
import random

# info
print("This program is meant to generate a password for the user. To do this they would have to first input how\nlong they need the password at a minimum of 5 characters long. This project is to\nhelp with security and privacy. A lot of times people don't know that personal information in passwords\ncan jeapordize their privacy.")

# This will take the input of the user for the question of how many characters will be in the password.
# I will try and do this recursively for validation
def characters():
    question = int(input('How many characters do you require for this password: '))
    if question <= 5 :
        print('Your entry is invalid, try again.')
        characters()

characters()
        