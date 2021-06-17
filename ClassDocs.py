class ClassDocs:
    def __init__(self, name):
        self.name = name
        # # docs de clase A que el clasif. asignó a clase A
        self.a = 0
        # docs de clase A que el clasif. asignó a otra clase
        self.b = 0
        # docs en clase A (viene en clases.csv)
        self.c = 0
        # docs que el clasif. asignó a clase A y NO son de clase A
        self.d = 0
        # docs que el clasif. NO asignó a clase A y NO son de clase A (no importa si las clases no coinciden, lo importante es que ambas sean ¬A)
        self.e = 0
        #contar los casos en que el clasif. asigna clase A (Provisional)
        self.f = 0
        # # de docs en test-set
        self.g = 0
        # contar los casos en que el clasif. asigna otra clase
        self.notC = 0
        # contar los casos en que el clasif. asigna otra clase
        self.notF = 0

        #METRICAS
        self.presicion = 0
        self.recall = 0
        self.acierto = 0
        self.error = 0

    def setPresicion(self):
        if self.f != 0:
            self.presicion = self.a / self.f
            return self.presicion
        else:
            return 0

    def setRecall(self):
        if self.c != 0:
            self.recall = self.a / self.c
            return self.recall
        else:
            return 0

    def setAcierto(self):
        if self.g != 0:
            self.acierto = (self.a + self.e) / self.g
            return self.acierto
        else:
            return 0

    def setError(self):
        if self.g != 0:
            self.error = (self.b + self.d) / self.g
            return self.error
        else:
            return 0

    def printMetrics(self):
        print("\t~Metricas~")
        print("\t\t-Precision: ", self.presicion)
        print("\t\t-Recall: ", self.recall)
        print("\t\t-Acierto: ", self.acierto)
        print("\t\t-Error: ", self.error)
        return

    def printEvaluation(self):
        print(" \t\t\t", " Pertenece\t", "~Pertenece\t", " ")
        print(" Clasificado\t", self.a, " \t\t", self.d, " \t\t", self.f)
        print("~Clasificado\t", self.b, " \t\t", self.e, " \t\t", self.notF)
        print(" \t\t\t\t", self.c, " \t\t", self.notC, " \t\t", self.g)
        return
