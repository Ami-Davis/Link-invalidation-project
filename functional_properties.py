def buildDictTofindFunctionalProperties(rdfToDictProperty):

    dp  = {}
    countP = {}
    for subj in rdfToDictProperty.keys():
        for prop in rdfToDictProperty[subj].keys():

            if prop not in dp.keys():
                dp[prop] = []
                countP[prop] = 0

            if set(rdfToDictProperty[subj][prop]) not in dp[prop]:
                dp[prop].append(set(rdfToDictProperty[subj][prop]))
            countP[prop] += 1

    return countP, dp


def listOFPropertiesByThr(countP, dp):

    propScore = {}

    props = list(dp.keys())
    for prop in props:

        score = len(dp[prop])/countP[prop]
        propScore[prop] = score

    return propScore
