from random import randrange as r

def gnose_maker(originalString):
    print("or" + originalString)
    if isinstance(originalString,str):
        if len(originalString.split()) > 3: 
            randomWord = r(len(originalString.split()))
            finalString = originalString.replace(originalString.split(" ")[randomWord], "gnose")
            print(finalString)
    else:
        randomWord = r(len(originalString))
        originalString[randomWord] = "gnose"
        finalString = " ".join(map(str,originalString))
        print(finalString)
    return finalString
    return None

if __name__ == "__main__":
    import sys
    print("run")
    sys.argv = sys.argv[1:]
    gnose_maker("bom dia")


