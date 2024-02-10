import requests
import json
import spacy
def downloadSupInfo():
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    #print(response.status_code)
    #print(type(response))
    supfile = open("supfile.json", "w")
    json.dump(response.json(), supfile, indent =6)
    supfile.close()
def keywordparser(text):
    negatives = {"aliases", "lb", "hairColor", "appearance", "eyeColor", "intelligence", "kg", "groupAffiliation", "lg", "cm", "race", "powerstats", "connections", "strength", "speed", "power", "images", "name"}
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    nouns = set()
    for token in doc:
        if token not in negatives:
            if token.pos_ == "NOUN" or token.pos_ == "PROPN" or token.pos_ == "ADJ":
                nouns.add(str(token))
    #print(nouns)
    return nouns
def getInfo(info):
    delimiter = " "
    result = ""
    result += (info["name"]) + " "
    result += (info["slug"]) + " "
    result += (info["appearance"]["gender"]) + " "
    if(type(info["appearance"]["race"]) == str):
     result += (info["appearance"]["race"]) + " "
    result += (info["appearance"]["eyeColor"]) + " "
    result += (info["appearance"]["hairColor"]) + " "
    result += (info["biography"]["fullName"]) + " "
    result += (info["biography"]["alterEgos"]) + " "
    result += delimiter.join(info["biography"]["aliases"]) + " "
    result += (info["biography"]["placeOfBirth"]) + " "
    if(type(info["biography"]["publisher"]) == str):
     result += (info["biography"]["publisher"]) + " "
    result += (info["biography"]["alignment"]) + " "
    result += (info["work"]["occupation"]) + " "
    result += (info["work"]["base"]) + " "
    result += (info["connections"]["groupAffiliation"]) + " "
    result += (info["connections"]["relatives"]) + " "
    result = result.lower()
    result = result.split(" ")
    return result
def findsupe(info):
    file = open('supfile.json')
    max = -1
    id = 1
    data = json.load(file)
    num = -1
    for i in data:
        count = 0
        temp = getInfo(i)
        #print(temp)
        num += 1
        for j in info:
            #print(info)
            #print(i)
            #print(type(j))
            if j.lower() in temp:
                #print(j)
                count = count + 1
        if max < count:
            max = count
            #print(str(i["id"]) + " " + str(count))
            #id = i["id"]
            id = num
            #test = i["id"]
    #print(test)
    #print(max)
    return id


#text = ("As an influential archetype of the superhero genre,"
#         "Superman possesses extraordinary powers, "
#         "with the character traditionally described " 
#         "as faster than a speeding bullet, more powerful than a locomotive, " 
#         "and able to leap tall buildings in a single bound, a phrase coined "
#         "by Jay Morton and first used in the Superman DC Comics")
#keywordparser(text)
#test1 = {"Superman", "Clark Kent", "DC Comics"}
#test2 = {"aliases"}
#test3 = {"Keystone", "City", "man", "Flash"}
#print(findsupe(test3))