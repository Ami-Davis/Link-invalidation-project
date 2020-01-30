
from ontology import Ontology
from measures import changeBirthDate
from measures import changeGender
from measures import changeReligion



if __name__ == '__main__':

    refalignrdfToTsv = True

    source = Ontology("data/000/onto.owl")
    target = Ontology("data/001/onto.owl")
    subjList = source.uniqueSubjects()
    #some test about how deal with triples that come from class Ontology:

    iter=0
    for i,j,k in source.onto:
        print("i",i)
        print("j",j)
        print("k",k)
        #print(source.uniqueProps())
        #print(len(source.uniqueProps()))
        if iter == 10:
            break

    for i,j,k in target.onto:
        print("i",i)
        print("j",j)
        print("k",k)
        #print(source.uniqueProps())
        #print(len(source.uniqueProps()))
