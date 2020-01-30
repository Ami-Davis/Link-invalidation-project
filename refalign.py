from xml.dom import minidom
import panda as pd
import random

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
    res['target'] = targets
    res.to_csv('data/transformed_refalign.tsv', sep='\t', index=False)


def addErrorToRefAlign(source, target, refalign, threshhold=0.8):
    '''
    :param source: source triple
    :param target: target triple
    :param refalign: refalign dataframe
    :param threshhold: if 0 no error will be added, if 1: add error in the size of refalign
            for example: if we have 100 refalign, we will add 100 error ==> now we have 200 rows.
    :return:
            return and save a dataframe containig everything in 2 columns.

    We should randomly add errors.
    '''

    refSize = refalign.shape[0]
    AddErrorCount = int(refSize*threshhold)
    result = pd.DataFrame()
    wrongSource = []
    wrongTarget = []
    counter = 0

    for source_candidate, target_candidate in zip(sorted(source.subject_objects(), key=lambda k: random.random()),sorted(target.subject_objects(), key=lambda k: random.random())):
        refCandidate = refalign[refalign.source == str(source_candidate[0])]
        if refCandidate.shape[0] == 0:
            continue
        else:
            if str(target_candidate[0]) != str(refCandidate.target.iloc[0]):
                wrongSource.append(source_candidate[0])
                wrongTarget.append(target_candidate[0])
                counter += 1

        if counter == AddErrorCount:
            result['source'] = wrongSource
            result['target'] = wrongTarget
            result = pd.concat([refalign,result])

            result.to_csv('data/refalign_addedWorng.tsv',sep='\t', index=False)
            return result
            break


