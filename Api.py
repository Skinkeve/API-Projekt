import json
import requests

class GetArticle():
    pass


class Structure():
    def Main(self):
        response = requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key=yourkey")
        print(response)


class Translate():
    pass

#https://www.dataquest.io/blog/python-api-tutorial/

start = Structure()
start.Main()
