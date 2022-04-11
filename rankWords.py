def getAvalWords(wordlst, needed_letters):
    # Find Words that dont repeat letter and have the wanted letters in them
    found_words = []
    for word in wordlst:
        wanted = True
        for c in word:
            if c not in needed_letters:
                wanted = False

        if wanted:
            found_words.append(word)
    return found_words

def rankWords(found_words, freq_ranker, loc_ranker, lategame, answer_words, roundNum):
    # Rank words based on the amount of times they've show up in words and there location 
    used_letters = []
    words_ranked = dict([(i,0) for i in found_words])
    for word in found_words:
        value = 0
        for i, c in enumerate(word):
            if c in used_letters:
                value += loc_ranker[c][i] - 10000
                value += freq_ranker[c] - 10000
            else:
                value += loc_ranker[c][i]
                value += freq_ranker[c]
            used_letters.append(c)
        if lategame and word in answer_words:
            value += 100000 * (roundNum - 2)
        
        words_ranked[word] = value
        used_letters = []
    
    return words_ranked