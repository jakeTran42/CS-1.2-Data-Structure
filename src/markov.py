import sys, random, string
from dictogram import Dictogram
from sample import weighted_random_choice
from helper import read_textfile, convert_to_list

class Markov(dict):
    def __init__(self, word_list=None, order=1):
        super(Markov, self).__init__()
        self.order = order

    def initiate_markov(self, word_list):
        order = self.order
        # iterate through the word_list to check key
        for i in range(len(word_list) - self.order):
            key = tuple(word_list[i: i + order])
            value = word_list[i + order]
            if key in self:
                self[key].add_count(value)
            else:
                self[key] = Dictogram([value])

    def generate_sentence(self, count=10):

        # Find random word
        rand_string = ""
        random_word = random.choice(list(self))
        rand_followup = weighted_random_choice(self[random_word])
        rand_string = rand_string + ' '.join(random_word) + ' ' + rand_followup

        # add follow-up word to tuple
        for i in range(count - self.order - 1):

            temp = list(random_word)
            temp.append(rand_followup)
            temp = temp[1:]
            random_word = tuple(temp)

            # Handle KeyError
            try:
                rand_followup = weighted_random_choice(self[random_word])
            except KeyError:
                random_word = random.choice(list(self))
                rand_followup = weighted_random_choice(self[random_word])

                # Edge Case
            while rand_followup == None:
                rand_followup = weighted_random_choice(self[random_word])
                print(rand_followup)

            rand_string = rand_string + " " + rand_followup

        return rand_string

def main():
    text = read_textfile("sample_text.txt")
    txt_list = convert_to_list(text)
    markov_chain = Markov(txt_list, 2)
    markov_chain.initiate_markov(txt_list)
    print(markov_chain.generate_sentence(15))

if __name__ == '__main__':
    main()
