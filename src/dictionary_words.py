#dictionary_words.py
'''This program reads in from a text file and outputs a randomly generated sentence using the words read in.

USAGE: python3 ./dictionary_words.py

or

python3 ./dictionary_words.py <insert # here>

^^^Users can specify how many words they want to use to generate random sentence'''

import sys, random, time, string

'''reads in from text file and saves to an array'''
def read_in_txtfile(text):
    with open(text) as f:
        word_data = f.read()
    return word_data

'''Takes in string of text, converts to and returns a list'''
def convert_to_list(text_string):
    word_bank = text_string.split()
    return word_bank

'''Takes in text string returns tuple'''
def convert_to_tuple(text_string):
    word_bank_tuple = tuple(text_string.split())
    return word_bank_tuple

'''grabs the number user enters to specify # of words for sentence'''
def get_word_count():
    try:
        count_string = str(sys.argv[1])
        return int(count_string)
    except IndexError:
        print("Error: Please enter a number.")
        exit()

'''generates and prints out random sentence string'''
def print_random_sentence(word_bank, num_of_words):
    rand_sentence_string = ""
    for index in range(0, num_of_words):
        rand_item = word_bank.pop(random.randint(0, len(word_bank) - 1))
        rand_sentence_string = rand_sentence_string + " " + rand_item
    print(rand_sentence_string)

'''generates and prints out random sentence string using tuple'''
def get_random_sentence_tuple(word_bank_tuple, num_of_words):
    rand_string = ""
    for i in range(num_of_words):
        rand_index = random.randint(0, len(word_bank_tuple) - 1)
        rand_word = word_bank_tuple[rand_index]
        rand_string = " ".join([rand_string, rand_word])
    return rand_string

def main():
    start = time.time()
    file_text = read_in_txtfile('word.txt')
    text_list = convert_to_tuple(file_text)
    random_sentence = get_random_sentence_tuple(text_list, get_word_count())
    print(random_sentence)
    end = time.time()
    print(end - start)

if __name__ == '__main__':
    main()
