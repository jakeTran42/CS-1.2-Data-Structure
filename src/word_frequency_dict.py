#word_frequency.py

'''This program takes in a word file, and then returns a histogram of all the words, the number of unique words within
   the text file, as well as the number of occurences of a particular word.

   USAGE: python3 ./word_frequency_dict.py'''

import sys, string
from dictionary_words import read_in_txtfile, convert_to_list

'''Takes in a list of text, returns a histogram as a dictionary'''
def histogram(source_text):
    histogram_dict = {}
    for word in source_text:
        if histogram_dict.get(word) is None:
            histogram_dict[word] = 1
        else:
            histogram_dict[word] += 1
    return histogram_dict

'''Takes in a histogram, returns number of unique words'''
def unique_words(histogram_dict):
    count = 0
    for key in histogram_dict:
        count += 1
    return count

'''Take in a word and histogram, returns number of times that word occurs within the dictionary'''
def frequency(word, histogram):
    count = 0
    for key in histogram:
        if word == key:
            count = histogram[key]
    return count

def main():
    file_txt = read_in_txtfile('word.txt')
    txt_list = convert_to_list(file_txt)
    txt_list[:] = [i.translate(str.maketrans('', '', string.punctuation)) for i in txt_list]
    my_histogram = histogram(txt_list)
    print(my_histogram)

    number_of_unique_words = unique_words(my_histogram)
    print("Number of unique words: {}".format(number_of_unique_words))

    word = "The"
    word_count = frequency(word, my_histogram)
    print("Number of occurences for \'{}\': {}".format(word, word_count))

if __name__ == '__main__':
    main()
