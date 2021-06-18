from Consulter import *


def main():
    initializer()
    print("Escalafon de cada documento:")
    consult()
    fillEvaluation()
    fillMetrics()
    menu()
    return 0


def menu():
    print("\n***************SELECCIONE UNA OPCION****************")
    print("*\t1) Mostrar test-set.csv")
    print("*\t2) Mostrar training-set.csv")
    print("*\t3) Mostrar clases.csv")
    print("*\t0) Salir")
    print("*****************************************************")
    opt = input("Que accion desea realizar? ")
    print(opt)
    if opt == '1':
        for doc in TEST:
            print("DocID: ", doc.id)
            print("Pertenece a la clase: ", doc.classDoc, "\tSe le asigno la clase: ", doc.classDocAssumption)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif opt == '2':
        for doc in TRAIN:
            doc.printDoc()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif opt == '3':
        for docClass in CLASSES:
            print("Clase: ", docClass.name)
            docClass.printEvaluation()
            docClass.printMetrics()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        return
    menu()


main()
