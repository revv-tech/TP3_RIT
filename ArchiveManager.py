import csv
import os
from Document import Document
from ClassDocs import ClassDocs

# LISTAS GLOBALES QUE SE ENCARGAN DE GUARDAR LOS DOCUMENTOS
# ARCHIVOS DE TEST-SET
TEST = []
# CLASES
CLASSES = []
# ARCHIVOS DE TRAINING-SET
TRAIN = []

PATH = os.path.dirname(__file__)
#   PATHS A LOS CSVs
TEST_PATH = os.path.realpath("...\\Archivos\\test-set.csv")
TRAINING_PATH = os.path.realpath("...\\Archivos\\training-set.csv")
CLASS_PATH = os.path.realpath("...\\Archivos\\clases.csv")


# LEE EL ARCHIVO DE CLASES Y CREA LA LISTA DE CLASSES EN VARIABLES GLOBALES
def readClasesCSV(path):
    global CLASSES
    classLine = []
    fCSV = open(path, "r")
    reader = csv.reader(fCSV)
    for row in reader:
        classLine.append(row[0].split("\t"))
    classLine = classLine[1:]

    for classElem in classLine:
        newClass = ClassDocs(classElem[0])
        CLASSES.append(newClass)

    return


# E: El path de la lista que desee revisar (si es test o training) y la lista (global) a la que lo desea agregar
# S: Ninguna (opcional que devuelva la lista en vez de guardar globales)
def readCSV(path, listDocs):
    global TEST
    global TRAIN
    fileLists = []
    fCSV = open(path, "r")
    reader = csv.reader(fCSV)

    for row in reader:
        # Maneja la lista para crear la estructura
        line = row[0].split("\t")

        newTerms = termsList(line[3])
        line.pop(3)
        line.append(newTerms)
        fileLists.append(line)

    fileLists = fileLists[1:]
    # Crea la estructura Documento
    for doc in fileLists:
        newDocument = Document(doc[0], doc[1], doc[2], doc[3])
        listDocs.append(newDocument)
        # newDocument.printDoc()

    return


def termsList(terms):
    newTermsAux = terms.split(" ")
    newTerms = []
    for term in newTermsAux:
        term = term.split("/")
        newTerms.append(term)

    return newTerms


def initializer():
    readClasesCSV(CLASS_PATH)
    readCSV(TRAINING_PATH, TRAIN)
    readCSV(TEST_PATH, TEST)
    print("Archivos CSV leidos correctamente")
    return
