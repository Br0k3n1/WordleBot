from Wordle.main import *
from getFrequency import *
from rankWords import *
from updateVariables import *
import trie
from random import randrange
import matplotlib.pyplot as plt
from os import path
import sys

## DOES NOT WORK 100% ##

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

# Variables
runAmount = 10
GUESSES = 6
data = dict([(i, 0) for i in range(1, GUESSES + 1)])
data[-1] = 0

for _ in range(0, runAmount):
    # More Variables
    GUESSES = 6
    ANSWER = answer_words[randrange(0, len(answer_words))]
    lateGame = False
    letterFreq, letterFreqLoc = GetFreqAndLocFreq(answer_words)
    needed_letters = GetMostCommonLetters(answer_words, letterFreq, letterFreqLoc)

    for roundNum in range(1, GUESSES + 1):
        # Get geuss
        found_words = getAvalWords(words, needed_letters)
        found_words_ranked = rankWords(
            found_words, letterFreq, letterFreqLoc, lateGame, answer_words_trie, roundNum
        )

        # Sort ranked words
        words_ranked_sorted = sorted(
            found_words_ranked.items(), key=lambda x: x[1], reverse=True
        )
        try:
            words_sorted, values_sorted = map(list, zip(*words_ranked_sorted))
        except:
            GUESSES = 1

        # Get best geuss and then get Results
        geuss = words_sorted[0]
        result, done = compare(geuss, ANSWER)

        needed_letters, letterFreq, letterFreqLoc = update(
            result, words_sorted[0], needed_letters, letterFreq, letterFreqLoc
        )

        if GUESSES == 3:
            lateGame = True

        print(f"Guessed: {geuss}")
        print(f"Result: {result}")

        # If Correct
        if done == True:
            print("\nCORRECT\n")
            data[roundNum] += 1
            break
        # If Wrong
        else:
            if GUESSES == 1:
                print(f"\nYou Failed :( the answer was {ANSWER}\n")
                data[-1] += 1
            GUESSES -= 1

# Print Data
dataSorted = sorted(data.items(), key=lambda x: x[1], reverse=True)
roundLenSorted, valueSorted = map(list, zip(*dataSorted))

print(data)

# Make Bar Graph
plt.bar(roundLenSorted, valueSorted)
plt.title("Amount of Attempts for Correct Answer")
plt.xlabel("Amount of Attempts")
plt.ylabel("Times this Occured")
plt.show()
