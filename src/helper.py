#dictionary_words.py
'''This helper module reads in from a text file and transform the text to array of text'''

import sys, random, string

'''Save text file to an array'''
def read_textfile(text):
    with open(text, encoding="utf8") as f:
        data = f.read()
    return data

'''Convert String of text to a list of text'''
def convert_to_list(text_string):
    word_list = text_string.split()
    return word_list
