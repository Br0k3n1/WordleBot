def GetFreqAndLocFreq(wordlst):
    letterFreq = dict([(chr(i),0) for i in range(97,123)])
    letterFreqLoc = dict([(chr(i),[0, 0, 0, 0, 0]) for i in range(97,123)])

    # Get the the amount of times a letter shows up and its location
    for word in wordlst:
        for i, c in enumerate(word):
            letterFreq[c] = letterFreq[c] + 1
            letterFreqLoc[c][i] = letterFreqLoc[c][i] + 1
    
    return letterFreq, letterFreqLoc

def GetMostCommonLetters(wordlst, letterFreq = True, letterFreqLoc = True):
    if letterFreq or letterFreqLoc:
        letterFreq, letterFreqLoc = GetFreqAndLocFreq(wordlst)
    
    # Sort Letter Frequency
    letterFreqSorted = sorted(letterFreq.items(), key=lambda x: x[1], reverse=True)

    letterSorted, valueSorted = map(list, zip(*letterFreqSorted))
    return letterSorted