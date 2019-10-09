"""This file is to test the sampling from histogram"""

from sample import get_random_word, weighted_random_choice, get_sample
from helper import convert_to_list, read_textfile
from word_frequency import histogram

def test_randomness(histogram):
    output_list = []
    for i in range(10000):
        output_list.append(get_random_word(histogram))
    test = get_sample(output_list)
    print(test)

def test_weighted_randomness(histogram):
    weighted_list = []
    for i in range(10000):
        rand_word = weighted_random_choice(histogram)
        weighted_list.append(rand_word)
    weighted_sample = get_sample(weighted_list)
    print(weighted_sample)

def main():
    '''This program reads in a histogram and returns a random word'''
    #read in text file, store as list
    txt = read_textfile("short_story.txt")
    txt_list = convert_to_list(txt)

    #create histogram based on list
    my_histogram = histogram(txt_list)

    test_randomness(my_histogram)
    test_weighted_randomness(my_histogram)

if __name__ == '__main__':
    main()