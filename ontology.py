
import rdflib as rdf


class Ontology:

    def __init__(self, path):

        self.onto = rdf.Graph().parse(source=path, format='xml')
        self.functional_properties = []


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



if __name__ == "__main__":

    g = Ontology("data/000/onto.owl")
    subjList = g.uniqueSubjects()
    print(len(subjList))








