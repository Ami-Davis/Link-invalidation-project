import pandas as pd

from ontology import Ontology
from refalign import transformRefToTsv, addErrorToRefAlign
from measures import changeBirthDate
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

    for s, p, o in source.onto:
        for ss, pp, oo in target.onto:
            #print('subject: ', s)
            #print('property: ', p)
            #print('object: ', o)
            #print('subject: ', ss)
            #print('property: ', pp)
            #print('object: ', oo)

            if "date_of_birth" in p and "date_of_birth" in pp:
                print("oo before", oo)
                oo = changeBirthDate(oo)
                print("oo after", oo)
                print("o is", o)
                if o == oo:
                    print("----------")
                    break






