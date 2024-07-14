from random import randrange as r
from math import floor 

def gnose_maker(originalString):
    #Adicionar um conversor de lista para string aqui, vai melhorar a orga-
    #nização pra quando rodar esse arquivo isolado em testes.
    if isinstance(originalString,str):
        print("or" + originalString)
        textSize = len(originalString.split())
        if textSize > 3:
            if textSize > 10: #retirar linha no futuro?
                for n in range(floor(10/3)):
                    randomWord = r(len(originalString.split()))
                    originalString = originalString.replace(originalString.split(" ")[randomWord], "gnose", 1)
                    print(originalString)
        randomWord = r(len(originalString.split()))
        finalString = originalString.replace(originalString.split(" ")[randomWord], "gnose", 1)
        print(finalString)
    else:
        randomWord = r(len(originalString))
        originalString[randomWord] = "gnose"
        finalString = " ".join(map(str,originalString))
        print(finalString)
    return finalString

if __name__ == "__main__":
    import sys
    print("run")
    sys.argv = sys.argv[1:]
    gnose_maker(sys.argv)


