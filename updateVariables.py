def update(result, chosen_word, needed_letters, freq_ranker, loc_ranker):
    for i, c in enumerate(result):
        if c == 'O':
            if chosen_word[i] in needed_letters:
                needed_letters.remove(chosen_word[i])
        elif c == 'G':
            loc_ranker[chosen_word[i]][i] += 100000
        elif c == 'Y':
            freq_ranker[chosen_word[i]] += 10000
            loc_ranker[chosen_word[i]][i] += -100000
    
        
    return needed_letters, freq_ranker, loc_ranker