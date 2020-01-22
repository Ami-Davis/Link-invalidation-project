
from ontology import Ontology
from measures import changeBirthDate
from measures import changeGender
from measures import changeReligion
from measures import compare


if __name__ == '__main__':

    refalignrdfToTsv = True

    source = Ontology("data/000/onto.owl")
    target = Ontology("data/001/onto.owl")
    subjList = source.uniqueSubjects()
    #some test about how deal with triples that come from class Ontology:

    iter=0
    for i,j,k in source.onto:
        print(source.uniqueProps())
        print(len(source.uniqueProps()))
        iter+=1
        if iter==1:
            break

    compare(source.onto, target.onto)
