'''This program is essentially a game where a dictionary will be created to assign value to certain letters.
The user will provide input to the program, unless that input is q or quit the program will continue to prompt them to
input and print the result of the word they print
Author: [Andrew Dana]
'''

# Dictionary
word_vals ={
    'A' : 1,
    'B' : 3,
    'C' : 3,
    'D' : 2,
    'E' : 1,
    'F' : 4,
    'G' : 2,
    'H' : 4,
    'I' : 1,
    'J' : 8,
    'K' : 5,
    'L' : 1,
    'M' : 3,
    'N' : 1,
    'O' : 1,
    'P' : 3,
    'Q' : 10,
    'R' : 1,
    'S' : 1,
    'T' : 1,
    'U' : 1,
    'V' : 4,
    'W' : 4,
    'X' : 8,
    'Y' : 4,
    'Z' : 10

}

# This will take the word input
word = input('Please enter your word: ')

# This will keep the input in loop unless the word = quit or q
while word != 'quit' and word != 'q':
    worth = 0
    for i in word.upper():
        if i in word_vals:
            x = word_vals.get(i)
            worth += x
    print(f'{word.upper()} is worth worth {worth} points.')
    word = input('Please enter your word: ')
            
