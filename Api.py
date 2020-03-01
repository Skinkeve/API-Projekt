import json
import requests
import os
from random import randint

class GetArticle():

    def GetArticles(self):
        self.articleResponse = requests.get("https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key="+start.apiKey) #henter en json fil fra api-1
        self.articleJtext = json.dumps(self.articleResponse.json(), sort_keys=False, indent=4) #gør json filen til en str, og sætter det pænt op :
        self.articlePtext = json.loads(self.articleJtext) #parser json filen til et python dict
        self.articleContainer = self.articlePtext['results'] #får fat i det der lå under results i dictionariet som var en liste... desværre
        for x in self.articleContainer: #for antallet af elementer i listen
            self.stringingOne = str(self.articleContainer[start.counter]) #gør elementer til str
            self.splitOne = self.stringingOne.split("title") #splitter string ved "title" og gør det derfor til typen lis0t
            del self.splitOne[0] #sletter første element i listen
            self.stringingTwo = str(self.splitOne) #gør listen til string
            self.splitTwo = self.stringingTwo.split("abstract") #splitter stringen ved "abstract" og gør det derved til en liste igen
            del self.splitTwo[1]# sletter element 1 i listen
            self.stringingThree = str(self.splitTwo) #gør listen til en string igen igen
            self.splitThree = self.stringingThree.split("\\\'") #splitter listen igen igen
            start.articleList.append(self.splitThree[2]) #smider det 3. element i listen ind i listen articlelist
            start.counter += 1 #gør tælleren 1 større
        start.counter = 0 # gør tælleren til 0

class Structure():
    def __init__(self): # laver en masse variabler
        self.articleList = []
        self.assignedLetterList = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        self.counter = int(0)
        self.chosen = str("")
        self.languageList = ["Yoda", "Chef", "Doge", "Groot", "Shakespear", "Random"]
        self.clear = None
        self.apiKey = ""

    def Main(self):# denne funktion styrer primært flowet i programmet, og er her primært for at skabe overblik
        self.clearCommandment = input("is your computer 1.windows or 2.linux \n") #henter input fra brugeren
        while True: #endless loop
            if self.clearCommandment == "1": #er førnævnte input == 1?
                self.clear = lambda: os.system('cls')#så kører du windows og derfor rydder vi på denne måde
                break # så bryder vi loopet
            elif self.clearCommandment == "2": # ellers hvis inputter er 2
                self.clear = lambda: os.system('clear') # så kører du linux og derfor rydder vi på denne måde
                break # bryder loop
            else: #ellers så prøv at se om du kan skrive 1 eller 2 igen...
                self.clearCommandment = input("Error, try again\n")
        self.apiKey = input("Insert api-key here\n") #henter bruger input
        self.clear() #rydder pythons console
        fetch.GetArticles() #kør denne funktion fra klassen
        start.ChooseArticle(self.articleList) #kør denne funktion med listen af artikler som parameter
        self.clear() # ryd pythons console
        start.ChooseLanguage(self.languageList) # kør denne funktion med listen af sprog som parameter
        self.clear() # rydder ligesom 10 eller joker i røvhul
        process.translation(self.chosen, self.chosen2) #kører denne funktion
        print('Original:',self.chosen,'\nTranslated:',process.translatedContainer,'\nTranslated with:',self.chosen2) #printer alt det vigtige der skal printes såsom den oversatte, den originale og sproget

    def ChooseArticle(self, list): #lader brugeren vælge en artikel
        print("Choose the title of your choice\n",) # printer
        for x in self.articleList: #kør samme antal gane som elementer i listen
            print(self.assignedLetterList[self.counter], ":", self.articleList[self.counter]) # print tal+" : "+artikel
            self.counter += 1#tælleren bliver en større
        self.choose = input('\nChoose title by typing the corresponding number\n') #få input fra brugeren
        while True: #endless loop
            if self.choose in self.assignedLetterList: #hvis inputtet findes i listen med tal
                self.chosen = self.articleList[int(self.choose)-1] # så er den valgte artikel den med pladsen[det tal brugeren skrev -1]
                break # bryder loop
            else:#ellers så prøv igen at se om du kan skrive et tal mellem 1 og 20
                self.choose = input('Error, try again\n') #
        self.counter = 0 #tælleren = 0

    def ChooseLanguage(self, list):#denne funktion lader brugeren vælge sprog
        print("Choose the language of your choice\n")#printer
        for x in self.languageList:#kør for hvert antal elementer i listen
            print(self.assignedLetterList[self.counter], ":", self.languageList[self.counter])#print på samme måde som før med artiklerne
            self.counter += 1#tælleren bliver 1 større
        self.choose2 = input('\nChoose language by typing the corresponding number\n')#henter input
        while True:#endless loop
            if self.choose2 in self.assignedLetterList:# hvis input er i listen af tal
                self.chosen2 = self.languageList[int(self.choose2)-1] #vælg det korrekte element ligesom før
                break # bryd loop
            else:#ellers prøv igen
                self.choose2 = input('Error, try again\n')
        self.counter = 0 # tæller = 0

class Translate():
    def __init__(self):#variabler
        self.chosenOne = None

    def translation(self, Tstring, Lstring):#denne funktion bruger fun translations api'en til at oversætte teksten som den får som parameter
        while True:#endless loop
            if Lstring == start.languageList[0] or self.chosenOne == 0:# hvis Lstring er det samme som det første element af mulige sprog i listen, dvs yoda == yoda eller hvis chosenOne blev lig med 0
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/yoda.json?text="+Tstring) #hent en json fil som har oversat Tstring
                break#bryd loop
            elif Lstring == start.languageList[1] or self.chosenOne == 1: #samme som før bare med chef
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/chef.json?text="+Tstring)
                break
            elif Lstring == start.languageList[2] or self.chosenOne == 2:#osv.
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/doge.json?text="+Tstring)
                break
            elif Lstring == start.languageList[3] or self.chosenOne == 3:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/groot.json?text="+Tstring)
                break
            elif Lstring == start.languageList[4] or self.chosenOne == 4:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/shakespeare.json?text="+Tstring)
                break
            elif Lstring == start.languageList[5]:#hvis det brugeren valgte var random
                self.chosenOne = randint(0, 4)#lav et random int mellem 0-4
                print('You got', start.languageList[self.chosenOne])#printer det sprog man fik
        if self.translateResponse.status_code == 200:#hvis alt funker
            self.jsonText = json.dumps(self.translateResponse.json(), sort_keys=False, indent=4)#gør json filen til en json str
            self.pyText = json.loads(self.jsonText) #gør det til et python dict
            self.textContainer = self.pyText['contents'] # åben contents
            self.translatedContainer = self.textContainer['translated'] # åben Translated
        elif self.translateResponse.status_code == 429: #hvis du har lavet for mange calls
            print("Woah slow down there, try again in an hour")#prøv igen senere
            quit()#sluk
        else:#ellers
            print("Whoops an error",self.translateResponse.status_code,"has appeared, that might be a problem")#jeg aner ikke hvad der er galt, her er error coden
            quit()#slut


start = Structure()
fetch = GetArticle()
process = Translate()
start.Main()
