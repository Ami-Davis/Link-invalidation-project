import pandas as pd
import rdflib as rdf
from ontology import Ontology
from refalign import transformRefToTsv, addErrorToRefAlign

TYPE = rdf.URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type")

if __name__ == '__main__':

    refalignrdfToTsv = True

    source = Ontology("data/000/onto.owl")
    target = Ontology("data/001/onto.owl")
    subjList = source.uniqueSubjects()

    """
    if refalignrdfToTsv:
        transformRefToTsv("data/refalign.rdf")

    refalign = pd.read_csv('data/transformed_refalign.tsv', sep='\t')

    print('Number of refalign before adding errors: ',refalign.shape[0])

    newRefalign = addErrorToRefAlign(source.onto,target.onto,refalign,threshhold=0.5)

    print('Number of refalign after adding errors: ',newRefalign.shape[0])


    """
    # some test about how deal with triples that come from class Ontology:
    s = source.rdfToDict()
    iter = 0
    for keys, values in s.items():
        print(keys)
        print(values)
        print()
        iter += 1
        if iter==10:
            break
