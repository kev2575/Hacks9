# Hacks9
Members: Kevin Howard
Purpose of project: The purpose was to create a small app where you can put in keywords and will give you a superhero or villian related to those words. The app will give you a picture of the villian or hero, a biography, and their stats.
Tools: I used python to create this project and I used the libaries spacy, tkinter, PIL, json, urlopen, requests and os.path
Difficulties: Python is not my best language which is part of the reason I chose to do this project using python because I wanted to learn more about it. So one difficulty I had was with comparing the keywords with the words in the json. It was a challenge to find a way to get the information out of json and make it easy to compare that info with the keywords. Eventually I decided to create a function that added all the info I needed to a string then split it into a list and that worked. Another challenge was making the card was a little difficult especially getting the image out of the json and onto the popup but eventually I found a video that described the best way to do that.
credits:
https://commons.wikimedia.org/wiki/File:Placeholder_male_superhero_c.png
to get superhero picture.
used https://akabab.github.io/superhero-api/api/
That is the api I used to get all the information on the superheros. It is a open source api.
How to run this program
run gui.py