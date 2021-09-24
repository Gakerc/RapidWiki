import wikipedia
import os


def resultWiki():

    richiesta = input("Wiki > ")
    if richiesta == "cls" or richiesta == "clear":
        os.system("cls")
        print("Clear fatto!")
        resultWiki()
    elif richiesta == "help" or richiesta == "Help":
        print("cls || clear: Pulisce lo schermo")
        resultWiki()

    print("Lingue it en fr es")

    lingua = input("Scegli una lingua: ")

    wikipedia.set_lang(lingua)
    
    try :
        ricerca = wikipedia.page(richiesta)
        result = wikipedia.summary(richiesta)
        link = ricerca.url
    

        print(result)
        print("")
        print("--------------------------------------------------------------------------")
        print("")
        print(link)
        print("")
    except:
        print("Non abbiamo trovato - " + richiesta)
        pass

while True:
    resultWiki()

