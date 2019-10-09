#word_frequency.py
'''THos module takes in text file then...
        returns a histogram of all the words 
        return the number of unique words within the text file
        return number of occurences of a word.'''

import sys, string
from helper import read_textfile, convert_to_list

'''Returns a histogram as a dictionary'''
def histogram(text):
    histogram_dict = {}
    for word in text:
        if histogram_dict.get(word) is None:
            histogram_dict[word] = 1
        else:
            histogram_dict[word] += 1
    return histogram_dict

'''Returns number of unique words'''
def unique_words(dict):
    return len(dict.keys())

'''Returns number of times that word occurs within the dictionary'''
def frequency(word, histogram):
    count = 0
    for key in histogram:
        if word == key:
            count = histogram[key]
    return count
