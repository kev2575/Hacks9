import tkinter as tk
import os.path
from card import Card
from util import downloadSupInfo, findsupe, keywordparser
from PIL import Image, ImageTk
root = tk.Tk()
pic = tk.Frame(root)
pic.pack()
descript = tk.Label(pic, text = "Please put in a description of a hero or villain\n Also if you haven't used this before please click download")
descript.pack(side = "bottom")
load = Image.open("suppic.png")
load = load.resize((200,200))
render = ImageTk.PhotoImage(load)
img = tk.Label(image=render)
img.pack(side = "top")
top = tk.Frame(root)
top.pack()
root.title("heros and villains app")
T = tk.Text(top, height=4, width=40)
T.pack()
bottom = tk.Frame(root)
bottom.pack()
def clicked():
    downloadSupInfo()
download = tk.Button(bottom,text = "Download", fg = "black", command = clicked)
download.pack(side = "left")
def press():
    if os.path.isfile('supfile.json'):
        text = T.get("1.0", 'end-1c')
        info = keywordparser(text)
        #print(type(info))
        result = findsupe(info)
        #print(result)
        card = Card(int(result))
        #print(result)
infobtn = tk.Button(bottom, text = "get Superhero", fg = "black", command= press)
infobtn.pack(side="left")
tk.mainloop()