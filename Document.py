class Document:

    def __init__(self, id, classDoc, numTerms, terms):
        self.id = id
        self.classDoc = classDoc
        self.numTerms = numTerms
        self.terms = terms
        self.classDocAssumption = ""

    def printDoc(self):
        print("ID del Documento: ", self.id)
        print("Clase del Doc. ", self.classDoc)
        if self.classDocAssumption != "":
            print("Clase que determina el algoritmo: ", self.classDocAssumption)
        print("Numero de Terminos: ", self.numTerms)
        print("Terminos: ")
        for term in self.terms:
            print("t: ", term[0], " peso: ", term[1])


class SimDoc:

    def __init__(self, document, sim):
        self.document = document
        self.sim = sim

    def printSimDoc(self):
        print("Similitud: ", self.sim)
        self.document.printDoc()
