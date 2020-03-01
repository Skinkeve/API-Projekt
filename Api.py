import json
import requests
import os
from random import randint

class GetArticle():

    def GetArticles(self):
        self.articleResponse = requests.get("https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key="+start.apiKey)
        self.articleJtext = json.dumps(self.articleResponse.json(), sort_keys=False, indent=4)
        #print(self.text)
        self.articlePtext = json.loads(self.articleJtext)
        #print(self.y)
        self.articleContainer = self.articlePtext['results']
        #print(self.x[0], "\n", type(self.x))
        for x in self.articleContainer:
        #    print(x)
            self.stringingOne = str(self.articleContainer[start.counter])
            self.splitOne = self.stringingOne.split("title")
            del self.splitOne[0]
            self.stringingTwo = str(self.splitOne)
            self.splitTwo = self.stringingTwo.split("abstract")
            del self.splitTwo[1]
            self.stringingThree = str(self.splitTwo)
            self.splitThree = self.stringingThree.split("\\\'") #1
            start.articleList.append(self.splitThree[2])
            start.counter += 1
        start.counter = 0

class Structure():
    def __init__(self):
        self.articleList = []
        self.assignedLetterList = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        self.counter = int(0)
        self.chosen = str("")
        self.languageList = ["Yoda", "Chef", "Doge", "Groot", "Shakespear", "Random"]
        self.clear = None
        self.apiKey = ""

    def Main(self):
        self.clearCommandment = input("is your computer 1.windows or 2.linux \n")
        while True:
            if self.clearCommandment == "1":
                self.clear = lambda: os.system('cls')
                break
            elif self.clearCommandment == "2":
                self.clear = lambda: os.system('clear')
                break
            else:
                self.clearCommandment = input("Error, try again\n")
        self.apiKey = input("Insert api-key here\n")
        self.clear()
        fetch.GetArticles()
        start.ChooseArticle(self.articleList)
        self.clear()
        start.ChooseLanguage(self.languageList)
        self.clear()
        process.translation(self.chosen, self.chosen2)
        print('Original:',self.chosen,'\nTranslated:',process.translatedContainer,'\nTranslated with:',self.chosen2)

    def ChooseArticle(self, list):
        print("Choose the title of your choice\n",)
        for x in self.articleList:
            print(self.assignedLetterList[self.counter], ":", self.articleList[self.counter])
            self.counter += 1
        self.choose = input('\nChoose title by typing the corresponding number\n')
        while True:
            if self.choose in self.assignedLetterList:
                self.chosen = self.articleList[int(self.choose)-1]
                break
            else:
                self.choose = input('Error, try again\n')
        self.counter = 0

    def ChooseLanguage(self, list):
        print("Choose the language of your choice\n")
        for x in self.languageList:
            print(self.assignedLetterList[self.counter], ":", self.languageList[self.counter])
            self.counter += 1
        self.choose2 = input('\nChoose language by typing the corresponding number\n')
        while True:
            if self.choose2 in self.assignedLetterList:
                self.chosen2 = self.languageList[int(self.choose2)-1]
                break
            else:
                self.choose2 = input('Error, try again\n')
        self.counter = 0

class Translate():
    def __init__(self):
        self.chosenOne = None

    def translation(self, Tstring, Lstring):
        while True:
            if Lstring == start.languageList[0] or self.chosenOne == 0:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/yoda.json?text="+Tstring)
                break
            elif Lstring == start.languageList[1] or self.chosenOne == 1:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/chef.json?text="+Tstring)
                break
            elif Lstring == start.languageList[2] or self.chosenOne == 2:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/doge.json?text="+Tstring)
                break
            elif Lstring == start.languageList[3] or self.chosenOne == 3:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/groot.json?text="+Tstring)
                break
            elif Lstring == start.languageList[4] or self.chosenOne == 4:
                self.translateResponse = requests.get("https://api.funtranslations.com/translate/shakespeare.json?text="+Tstring)
                break
            elif Lstring == start.languageList[5]:
                self.chosenOne = randint(0, 4)
                print('You got', start.languageList[self.chosenOne])
        if self.translateResponse.status_code == 200:
            self.jsonText = json.dumps(self.translateResponse.json(), sort_keys=False, indent=4)
            self.pyText = json.loads(self.jsonText)
            self.textContainer = self.pyText['contents']
            self.translatedContainer = self.textContainer['translated']
            #thinning.collectingAll(self.container)
        elif self.translateResponse.status_code == 429:
            print("Woah slow down there, try again in an hour")
            quit()
        else:
            print("Whoops an error",self.translateResponse.status_code,"has appeared, that might be a problem")
            quit()


start = Structure()
fetch = GetArticle()
process = Translate()
start.Main()
