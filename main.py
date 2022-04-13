from getFrequency import *
from rankWords import *
from updateVariables import *
import trie
from os import path
import sys

# Get Possible Guesses
with open(path.join(sys.path[0], "words/words.txt"), "r") as f:
    words = f.readlines()
for i, word in enumerate(words):
    words[i] = word.strip()

# Get Posible Answers
with open(path.join(sys.path[0], "words/answer_words.txt"), "r") as f:
    answer_words = f.readlines()
for i, answer_word in enumerate(answer_words):
    answer_words[i] = answer_word.strip()

# Turn list of answers into trie data stucture
answer_words_trie = trie.Trie()
for answer in answer_words:
    answer_words_trie.add_word(answer)

letterFreq, letterFreqLoc = GetFreqAndLocFreq(answer_words)
needed_letters = GetMostCommonLetters(answer_words, letterFreq, letterFreqLoc)

lateGame = False
roundNum = 1
while True:
    found_words = getAvalWords(words, needed_letters)
    found_words_ranked = rankWords(
        found_words, letterFreq, letterFreqLoc, lateGame, answer_words_trie, roundNum
    )

    # Sort ranked words
    words_ranked_sorted = sorted(
        found_words_ranked.items(), key=lambda x: x[1], reverse=True
    )
    words_sorted, values_sorted = map(list, zip(*words_ranked_sorted))
    top_ten = words_sorted[0:10]

    if values_sorted[0] - values_sorted[1] > 50000:
        print("\n")
        for word in top_ten:
            if word == top_ten[0]:
                print(f"*{word}: {found_words_ranked[word]}")
            else:
                print(f"{word}: {found_words_ranked[word]}")
        print("\n")
    else:
        print("\n")
        for word in top_ten:
            print(f"{word}: {found_words_ranked[word]}")
        print("\n")

    chosen_word = input("What Word Did you Choose: ")
    result = input(
        "\nInput One Of These Words Into Wordle and Input Reults in Terminal O = Grey, G = Green, Y = Yellow (ex. OOGOY) (CTRL C to End): "
    )

    needed_letters, letterFreq, letterFreqLoc = update(
        result, chosen_word, needed_letters, letterFreq, letterFreqLoc
    )
    roundNum += 1

    if roundNum == 3:
        lateGame = True
