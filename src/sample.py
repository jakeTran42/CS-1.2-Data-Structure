import sys, random
from dictionary_words import read_in_txtfile, convert_to_list
from word_frequency_dict import histogram


def get_random_word(histogram):
    '''Takes in histogram, returns random word '''
    rand_word = random.choice(list(histogram.keys()))
    return rand_word

def get_sample(storage_list):
    '''builds a sample dictionary using a list'''

    '''dictionary'''
    sample_list = {}

    for word in storage_list:
        if sample_list.get(word) is None:
            sample_list[word] = 1
        else:
            sample_list[word] += 1
    return sample_list

def weighted_random_choice(histogram):
    '''This function will return a random word based on a
    weighted probability -use random.randint'''

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

def test_uniform_randomness(histogram):
    uniform_list = []
    for i in range(10000):
        uniform_list.append(get_random_word(histogram))
    test = get_sample(uniform_list)
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
    txt = read_in_txtfile("short_story.txt")
    txt_list = convert_to_list(txt)

    #create histogram based on list
    my_histogram = histogram(txt_list)

    test_uniform_randomness(my_histogram)
    test_weighted_randomness(my_histogram)

if __name__ == '__main__':
    main()
