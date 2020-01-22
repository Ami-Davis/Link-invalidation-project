import textdistance

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def hamming_similarity(a,b):
    return textdistance.hamming.normalized_similarity(a,b)

def levenshtein_distance(a,b):
    return textdistance.levenshtein.normalized_similarity(a,b)

def jaccard(a,b):
    tokens_1 = a.split()
    tokens_2 = b.split()
    return textdistance(tokens_1, tokens_2)

def changeMonth(s):


def changeBirthDate(a):
    #May 26, 1913
    t = a.split()

    print(t)

changeBirthDate("May 26, 1913")




