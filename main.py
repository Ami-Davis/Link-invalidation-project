import pandas as pd

from ontology import Ontology
from refalign import transformRefToTsv, addErrorToRefAlign

import textdistance

if __name__ == '__main__':

    refalignrdfToTsv = True

    source = Ontology("data/000/onto.owl")
    target = Ontology("data/001/onto.owl")
    subjList = source.uniqueSubjects()

    if refalignrdfToTsv:
        transformRefToTsv("data/refalign.rdf")

    refalign = pd.read_csv('data/transformed_refalign.tsv', sep='\t')

    print('Number of refalign before adding errors: ',refalign.shape[0])

    newRefalign = addErrorToRefAlign(source.onto,target.onto,refalign,threshhold=0.5)

    print('Number of refalign after adding errors: ',newRefalign.shape[0])


 
    #some test about how deal with triples that come from class Ontology:

    iter=0
    for i,j,k in source.onto:
        print('subject: ', i)
        print('property: ', j)
        print('object: ', k)

        iter+=1
        if iter==10:
            break

