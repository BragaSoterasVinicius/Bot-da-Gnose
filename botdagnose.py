from random import randrange as r
from math import floor 
from googlesearch import search as s
import pickle as p 

def trivia_search(lwrd):
    for j in s("wikipedia " + lwrd, tld="co.in", num=1, stop=1, pause=2):
        print(j)
        return j
    
def gnose_maker(originalString):
    if counterLoader() > 3:
        trivia = trivia_search(loadLastWords())
        counterSaver(0)
        finalString = trivia
    else:
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
    num = counterLoader()
    print(counterLoader)
    counterSaver(num+1)
    saveLastWords(originalString)
    return finalString
    

def loadLastWords():
    with open('gnoseWords.pkl', 'rb') as t:
        e = p.load(t)
        print(e)
        return e
    
def saveLastWords(w):
    with open('gnoseWords.pkl', "wb") as outp:
        p.dump(w, outp, p.HIGHEST_PROTOCOL)

def counterSaver(n): 
    with open('gnose0.pkl', 'wb') as outp:
        p.dump(n, outp, p.HIGHEST_PROTOCOL)

def counterLoader():
    with open('gnose0.pkl', 'rb') as t:
        e = p.load(t)
        print(e)
        return e


if __name__ == "__main__":
    import sys
    print("run")
    sys.argv = sys.argv[1:]
    gnose_maker(sys.argv)


