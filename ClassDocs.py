
class ClassDocs:
    def __init__(self,name,n_Test,n_Train,total):
        self.name = name
        # # docs de clase A que el clasif. asignó a clase A
        self.a = 0
        # docs de clase A que el clasif. asignó a otra clase
        self.b = 0
        # docs en clase A (viene en clases.csv)
        self.c = total
        # docs que el clasif. asignó a clase A y NO son de clase A
        self.d = 0
        # docs que el clasif. NO asignó a clase A y NO son de clase A (no importa si las clases no coinciden, lo importante es que ambas sean ¬A)
        self.e = 0
        #contar los casos en que el clasif. asigna clase A (Provisional)
        self.f = n_Train
        # # de docs en test-set
        self.g = n_Test

        #METRICAS
        self.presicion = 0
        self.recall = 0
        self.acierto = 0
        self.error = 0


