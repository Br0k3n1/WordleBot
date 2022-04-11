# Compare geuss and answer
def compare(geuss, ANSWER):
    geuss = str(geuss).lower()
    result = [None, None, None, None, None]
    used_letters = []
    
    for i, letter in enumerate(geuss):
        if geuss[i] not in used_letters and geuss[i] == ANSWER[i]:
            used_letters.append(geuss[i])
            result[i] = "G"
        elif geuss[i] not in used_letters and letter in ANSWER:
            used_letters.append(geuss[i])
            result[i] = "Y"
        else:
            used_letters.append(geuss[i])
            result[i] = "O"
    
    result = ''.join(result)
    if geuss == ANSWER:
        return result, True
    return result, False