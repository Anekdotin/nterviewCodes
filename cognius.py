#Test For Cognius code challenge
import time

WORDS_TO_SCORE = (
    "something",
    "red",
    "anything",
    "green",
    "mother",
    "yellow",
    "father",
    "blue",
    "foo",
    "purple",
    "bar",
    "orange",
    "baz",
    "black",
    "white",
)

def loadfile(file_list):
    list_of_lists = []
    with open(file_list, 'r') as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(',')]

            list_of_lists.append(inner_list)

    return list_of_lists
def score_word_pair(w1, w2):

    return len(w1)* len(w2)




def get_highest_scoring_pair(words):
    pass

if __name__ == "__main__":
    start_time = time.time()
    file_list = 'words_en.txt'
    filein = loadfile(file_list)

    best_pair = get_highest_scoring_pair(WORDS_TO_SCORE)
    #final_score = score_word_pair(*best_pair)

    print("--- %s seconds ---" % (time.time() - start_time))
