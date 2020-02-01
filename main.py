import rdflib as rdf
from ontology import Ontology
from functional_properties import buildDictTofindFunctionalProperties,listOFPropertiesByThr
from comparing import Comparing

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

    compare = Comparing(propScores, s, t)
    functionalProp = compare.create_functional_prop(threshold=0.8)
    twins = compare.find_twins(threshold=0.8)
    print (twins)
