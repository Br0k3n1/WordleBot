def update(result, chosen_word, needed_letters, freq_ranker, loc_ranker):
    used_letters = []
    for i, c in enumerate(result):
        if c == "O" and chosen_word[i] not in used_letters:
            if chosen_word[i] in needed_letters:
                needed_letters.remove(chosen_word[i])
                used_letters.append(chosen_word[i])
        elif c == "G" and chosen_word[i] not in used_letters:
            loc_ranker[chosen_word[i]][i] += 100000
            used_letters.append(chosen_word[i])
        elif c == "Y" and chosen_word[i] not in used_letters:
            freq_ranker[chosen_word[i]] += 10000
            loc_ranker[chosen_word[i]][i] += -100000
            used_letters.append(chosen_word[i])

    return needed_letters, freq_ranker, loc_ranker
