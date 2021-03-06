
import rdflib as rdf


class Ontology:
    '''

    This class is building rdf graph for each ontology. Can use them using: a = Ontology(path) and use the ontology: a.onto

    '''

    def __init__(self, path):

        self.onto = rdf.Graph().parse(source=path, format='xml')

    def __len__(self):
        return len(self.onto)

    def uniqueSubjects(self):
        subjsList = []
        subjs = self.onto.subjects()
        for subj in subjs:
            subjsList.append(subj)
        return list(set(subjsList))

    def uniqueProps(self):
        propsList = []
        props = self.onto.predicates()
        for prop in props:
            propsList.append(prop)
        return list(set(propsList))


    def uniqueObjects(self):
        objsList = []
        objs = self.onto.objects()
        for obj in objs:
            objsList.append(obj)
        return list(set(objsList))

    def rdfToDict(self):
        subjsDict = {}
        for s, p, o in self.onto.triples((None, None, None)):
            if o == rdf.URIRef("http://www.w3.org/2002/07/owl#ObjectProperty"):
                continue
            if s not in subjsDict.keys():
                subjsDict[s] = {}
            if p not in subjsDict[s].keys():
                subjsDict[s][p] = []

            subjsDict[s][p].append(o)
        return subjsDict