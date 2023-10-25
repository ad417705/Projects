''' This program takes in text as input and converts it into a bag of words, using the build_dictionary() function
to build a word frequency dictionary from a list of words.
Author: [Andrew Dana]
'''

test_list = [1,2,3,4,5,5,5]
counter = 0
def build_dictionary(string):
    string = string.lower()
    words = string.split()
    word_freq_dict = {}
    for word in words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1
    return word_freq_dict

word_input = input('Please enter your string: ')
word_freq = build_dictionary(word_input)
sorted_word_freq = sorted(word_freq.items(), key=lambda item: item[1])

for word, frequency in sorted_word_freq:
    print(f'{word} - {frequency}')




