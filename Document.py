

class Document:

    def __init__(self,id,classDoc,numTerms, terms):
        self.id = id
        self.classDoc = classDoc
        self.numTerms = numTerms
        self.terms = terms
    def printDoc(self):
        print("ID del Documento: ", self.id)
        print("Clase del Doc. ", self.classDoc)
        print("Numero de Terminos: ", self.numTerms)
        print("Terminos: ")
        for term in self.terms:
            print("t: ",term[0], " peso: ", term[1])




