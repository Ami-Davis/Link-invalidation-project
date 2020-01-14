from xml.dom import minidom
import pandas as pd


def transformRefToTsv(path):


    xmldoc = minidom.parse(path)

    entity1_onto_source = xmldoc.getElementsByTagName('entity1')
    entity2_onto_target = xmldoc.getElementsByTagName('entity2')

    sources = []
    targets = []
    res = pd.DataFrame()

    for i in range(len(entity1_onto_source)):
        source = entity1_onto_source[i].attributes['rdf:resource'].value
        target = entity2_onto_target[i].attributes['rdf:resource'].value
        sources.append(source)
        targets.append(target)

    res['source'] = sources
    res['traget'] = targets
    print(res.head())
    res.to_csv('data/transformed_refalign.tsv', sep='\t', index=False)


def addErrorToRefAlign(source,target,refalign,threshhold=0.8):
    '''
    :param source: source triple
    :param target: target triple
    :param refalign: refalign dataframe
    :param threshhold: if 0 no error will be added, if 1: add error in the size of refalign
            for example: if we have 100 refalign, we will add 100 error ==> now we have 200 rows.
    :return:
            a dataframe containig everything in 2 columns.

    We should randomly add errors.
    '''


    #TODO