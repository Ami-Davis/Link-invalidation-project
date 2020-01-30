import textdistance
import difflib

def similar(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()

def hamming_similarity(l1,l2):
    a = ''.join(l1)
    b = ''.join(l2)
    return textdistance.hamming.normalized_similarity(a,b)

def levenshtein_distance(l1,l2):
    a = ''.join(l1)
    b = ''.join(l2)
    return textdistance.levenshtein.normalized_similarity(a,b)

#for lists
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

#for strings such as for the currency
def jaccard_sim(str1,str2):
#   return textdistance.jaccard.normalized_similarity(a, b)
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


print("jaccard",jaccard_sim("USD ana are mere ","N4ZfD ana are mere albe"))
#sim = similar(["dj ana ajd"],[ "dj ana ajd", ""])
#print(sim)

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

#a = changeGender("M")
#print(a)

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

def changeName(name):
    res = []
    output = ""
    splittedName = name.split()
    for subname in splittedName:
        res.append(subname[0])
    for letter in res:
        output = output + letter + '. '
    return output.rstrip()

#changeName("ana Maria Jacob H")

#rel = changeReligion("Roman Cha t o l ")
#print(rel)

#date = changeBirthDate("May 26, 1913")
#print(date)

def compare_Birthdate(l1, l2):
    l2[0] = changeBirthDate(l2[0])
    if l1[0].strip() == l2[0].strip():
        return 1
    return 0

def compare_Gender(l1, l2):
    l2[0] = changeGender(l2[0])
    if l1[0].strip() == l2[0].strip():
        return 1
    return 0

def compare_Religion(l1, l2):
    l2[0] = changeReligion(l2[0])
    l1[0] = changeReligion(l1[0])
    if l1[0].strip() == l2[0].strip():
            return 1
    return 0

def compare_ByLength(l1,l2):
    if len(l1) == len(l2):
        return 1
    return 0

def compare_Equality(l1,l2):
    if l1[0] == l2[0]:
        return 1
    return 0

def compare_Names(l1,l2):
    l1[0] = changeName(l1[0])
    if l1[0].rstrip() == l2[0].rstrip():
        return 1
    return 0

def compareStrings(l1, l2):
    return jaccard(l1,l2)

#print(compare_ActedBy([12,32,3],["aa",3,3]))

'''
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

            if "gender" in p and "gender" in pp:
                oo = changeGender(oo)
                if o.strip() == oo.strip():
                    print("g---------")

            if "religion" in p and "religion" in pp:
                oo = changeReligion(oo)
                o = changeReligion(o)
                if o.strip() == oo.strip():
                    print("r---------")
'''


