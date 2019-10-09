import sys, random
from helper import read_textfile, convert_to_list
from word_frequency import histogram


def get_random_word(histogram):
    '''Takes in histogram, returns random word'''
    rand_word = random.choice(list(histogram.keys()))
    return rand_word

def get_sample(given_list):
    '''builds a sample dictionary using a list'''
    sample_list = {}
    for word in given_list:
        if sample_list.get(word) is None:
            sample_list[word] = 1
        else:
            sample_list[word] += 1
    return sample_list

def weighted_random_choice(histogram):
    '''This function return random word based on weighted list'''

    # converts list of keys and values
    words, weights = zip(*histogram.items())
    weight_list = []
    curr_weight = 0
    for weight in weights:
        curr_weight += weight
        weight_list.append(curr_weight)
    rand_num = random.randint(1, curr_weight)
    for word, weight in zip(words, weight_list):
        if rand_num <= weight:
            return word

def main():
    '''Return random word from histogram'''
    txt = read_textfile("sample_text.txt")
    txt_list = convert_to_list(txt)
    histogram1 = histogram(txt_list)

if __name__ == '__main__':
    main()
