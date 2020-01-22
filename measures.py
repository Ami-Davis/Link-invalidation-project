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

def changeMonth(month):
    switcher = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "Juin": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
        }
    return switcher.get(month)

def changeGender(gender):
    switcher = {
        "F": "Female",
        "M": "Male"
        }
    return switcher.get(gender)

a = changeGender("M")
print(a)

def changeBirthDate(a):
    #May 26, 1913
    # 1930 - 04 - 18
    t = a.replace(",","").split()
    t[0] = changeMonth(t[0])
    res = a
    if len(t) == 3:
        res = ""
        res = t[2]+"-"+t[0]+"-"+t[1]
    return res

def religion(religion):
    return religion.replace(" ","")

rel = religion("Roman Cha t o l ")
print(rel)

date = changeBirthDate("May 26, 1913")
print(date)

