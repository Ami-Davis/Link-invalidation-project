
import rdflib as rdf
from ontology import Ontology
from functional_properties import buildDictTofindFunctionalProperties,listOFPropertiesByThr
from comparing import Comparing
import matplotlib.pyplot as plt
import pandas as pd

TYPE = rdf.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")


if __name__ == '__main__':

    source = Ontology("data/000/onto.owl")
    target = Ontology("data/001/onto.owl")
    subjList = source.uniqueSubjects()

    # some test about how deal with triples that come from class Ontology:
    s = source.rdfToDict()
    t = target.rdfToDict()
    countPsource, DPsource = buildDictTofindFunctionalProperties(s)

    propScores = listOFPropertiesByThr(countPsource, DPsource)

    refalignPath = 'data/refalign.tsv'
    ra = pd.read_csv(refalignPath, sep='\t')
    trueSimilars = []
    for i, row in ra.iterrows():
        trueSimilars.append((str(row.values[0]), str(row.values[1])))
    compare = Comparing(propScores, s, t)

    precision = []
    recall = []
    fscore = []
    thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    i = 0
    for thr in thresholds:
        functionalProp = compare.create_functional_prop(threshold=thr)
        twins = compare.find_twins(threshold=thr)
        TP = 0.0
        FP = 0.0
        FN = 0.0
        for x, y in twins:
            ok = True
            for xx, yy in trueSimilars:
                if x == xx and y == yy:
                    ok = False
                    TP += 1.0
                elif x == xx:
                    ok = False
                    FP += 1.0
            if ok:
                FN += 1.0


        print(TP)
        print(FP)
        print(FN)
        if TP == 0.0 and FP == 0.0 and FN == 0.0:
            precision.append(0.0)
            recall.append(0.0)
            fscore.append(0.0)
            i += 1
            continue
        precision.append(TP / (TP + FP))
        recall.append(TP / (TP + FN))
        fscore.append(2 * (precision[i] * recall[i]) / (precision[i] + recall[i]))
        i += 1


    plt.figure(1)
    plt.plot(thresholds, precision)
    plt.xlabel("Threshold")
    plt.ylabel("Precision")

    plt.figure(2)
    plt.plot(thresholds, recall)
    plt.xlabel("Threshold")
    plt.ylabel("Recall")

    plt.figure(3)
    plt.plot(thresholds, fscore)
    plt.xlabel("Threshold")
    plt.ylabel("F-Score")
    plt.show()
    
