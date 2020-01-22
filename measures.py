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
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
        }
    return switcher.get(month)

def changeGender(gender):
    gender = gender.strip()
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
    res = ""
    if len(t) == 3:
        res = t[2]+"-"+t[0]+"-"+t[1]
    return res

def changeReligion(religion):
    return religion.replace(" ","")

rel = changeReligion("Roman Cha t o l ")
print(rel)

date = changeBirthDate("May 26, 1913")
print(date)


def compare(ont1, ont2):
    output = []
    for s, p, o in ont1:
        for ss, pp, oo in ont2:
            if "date_of_birth" in p and "date_of_birth" in pp:
                #print("oo before", oo)
                oo = changeBirthDate(oo)
                #print("oo after", oo)
                #print("o is", o)
                if o.strip() == oo.strip():
                    print("d---------")
                    output.append((s,ss))
    print(output)
            if "gender" in p and "gender" in pp:
                oo = changeGender(oo)
                if o.strip() == oo.strip():
                    print("g---------")

            if "religion" in p and "religion" in pp:
                oo = changeReligion(oo)
                o = changeReligion(o)
                if o.strip() == oo.strip():
                    print("r---------")
