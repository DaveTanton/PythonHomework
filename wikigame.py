import requests
import random

def searchFun(link):
    se = requests.session()
    re = se.get(link)
    html = re.text
    html = html.lower()
    links = html.split("href=")
    listoflinks = []
    for l in links:
        parts = l.split("\"")
        if ("http" in parts[1]):
            listoflinks .append(parts[1])
    return listoflinks

search = searchFun ("https://en.wikipedia.org/wiki/Special:Random")
comparelist=[]
count = 0

while True:

    randomcall = random.randint(3, 9)
    newsite = search[randomcall]
    """
    if not search:
        print("Thats it! its all over. no more valid links")
        print("I have followed ", count, "links")
        print(comparelist)
        break
    """
    if newsite in comparelist:
        print("I have followed ", count, "links before I repeated myself")
        print ("last valid link was",newsite)
        for link in comparelist:
            print(link)
        break
    else:
        comparelist.append(newsite)
    count += 1
