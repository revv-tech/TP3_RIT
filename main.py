from Consulter import *


def main():
    initializer()
    consult()
    fillEvaluation()
    fillMetrics()
    for docClass in CLASSES:
        print("Clase: ", docClass.name)
        docClass.printEvaluation()
        docClass.printMetrics()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return 0


main()
