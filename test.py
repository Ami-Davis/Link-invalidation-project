def compare_Object(dict1, dict2, p):
    elem_to_compare = ""
    for object in dict2.items():
        for property, val in object[1].items():
            if property == p:
                obj_val = val.split("/")[-1]
            if object[0] == obj_val:
                elem_to_compare = val
    if elem_to_compare != "":
        for object in dict1.items():
            for property, value in object[1].items():
                if property == p:
                    if value.split("/")[-1].strip().lower() == elem_to_compare.strip().lower():
                        print("FOUND MATCH")
                        return 1.0
    return 0.0

dictii = {
    "Kenya": {
        "has_capital": "http://oaei.ontologymatching.org/2010/IIMBDATA/en/nairobi",
        "name": "Tuvalu"
    },
    "tuvadlu": {
        "has_capital": "http://oaei.ontologymatching.org/2010/IIMBDATA/en/funadfuti",
        "name": "Tudvalu"
    }
}


dicti = {
    "item234": {
        "has_capital" : "http://oaei.ontologymatching.org/2010/IIMBDATA/en/item5732486154834428052",
        "name": "Kenya"
    },
    "item5732486154834428052": {
        "name": "Nairobi"
    }
}

compare_Object(dictii, dicti, 'has_capital')