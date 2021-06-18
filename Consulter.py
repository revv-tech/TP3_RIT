from ArchiveManager import *
from Document import SimDoc
from AssumptionClass import AssumptionClass


def getWeight(pTerm, pDoc):
    """
    :param pTerm: Termino que esta buscando
    :param pDoc: Documento donde se busca el termino
    :return: El peso del termino en pDoc
    """
    for term in pDoc.terms:
        if term[0] == pTerm:
            return term[1]
        elif term[0] > pTerm:
            return 0
    return 0


def calcWeight(pTrain, pTest):
    """
    :param pTrain: Documento de la coleccion test-set.csv
    :param pTest: Documento de la coleccion training-set.csv
    :return: Peso por la sumatoria de productos de los terminos
    """
    sim = 0
    for term in pTest.terms:
        sim += (float(term[1]) * float(getWeight(term[0], pTrain)))
    return sim


def makeRanking(pTestDoc):
    """
    :param pTestDoc: Documento de la coleccion test-set.csv
    :return: Escalafon de los 10 documentos con mayor similitud a testDoc
    """
    ranking = []
    for doc in TRAIN:
        ranking.append(SimDoc(doc, calcWeight(doc, pTestDoc)))
    ranking.sort(key=lambda simdoc: simdoc.sim)

    print("\n* Doc TEST: ", pTestDoc.id, " \tClase: ", pTestDoc.classDoc, "*\n")
    for i in range(10):
        print("DocID: ", ranking[i].document.id, "  \tClase: ", ranking[i].document.classDoc, "  \tSim: ", ranking[i].sim)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    return ranking[0:10]


def indexObjectList(pClassName, pList):
    for index, assumptionClass in enumerate(pList):
        if assumptionClass.className == pClassName:
            return index
    return -1


def makeAssumption(pRanking):
    """
    :param pRanking: Escalafon con los 10 documentos con mayor similitud
    :return: Devuelve el nombre de la clase con mayor similitud
    """
    averageSim = []

    # Rellena la lista con todas las clases que hay en el doc clases.csv
    for c in CLASSES:
        averageSim.append(AssumptionClass(c.name))

    # Recorre el escalafon para promedia el peso de los docs por clase
    for doc in pRanking:
        averageSim[indexObjectList(doc.document.classDoc, averageSim)].addTotal(doc.sim)

    # Promedia todas las clases y las ordena de mayor a menor
    for assumption in averageSim:
        assumption.average()
    averageSim.sort(key=lambda assumptionClass: assumptionClass.total, reverse=True)

    return averageSim[0].className


def consult():
    """
    :return: N/A : Asigna lo que cree que es la clase de cada documento dentro de test-set.csv
    """
    for doc in TEST:
        ranking = makeRanking(doc)
        doc.classDocAssumption = makeAssumption(ranking)
    return


def fillEvaluation():
    """
    :return: N/A : Recorre la lista de docs y analiza la tabla de evaluacion para cada clase existente
    """
    for doc in TEST:
        for docClass in CLASSES:
            docClass.g += 1
            if doc.classDoc == docClass.name and doc.classDocAssumption == docClass.name:
                docClass.a += 1
                docClass.f += 1
                docClass.c += 1
            elif doc.classDoc == docClass.name and doc.classDocAssumption != docClass.name:
                docClass.b += 1
                docClass.notF += 1
                docClass.c += 1
            elif doc.classDoc != docClass.name and doc.classDocAssumption == docClass.name:
                docClass.d += 1
                docClass.f += 1
                docClass.notC += 1
            elif doc.classDoc != docClass.name and doc.classDocAssumption != docClass.name:
                docClass.e += 1
                docClass.notF += 1
                docClass.notC += 1
    return

def fillMetrics():
    """
    :return: N/A : Recorre las clases y hace los calculos para la metricas de rendimiento
    """
    for docClass in CLASSES:
        docClass.setPresicion()
        docClass.setRecall()
        docClass.setAcierto()
        docClass.setError()
    return