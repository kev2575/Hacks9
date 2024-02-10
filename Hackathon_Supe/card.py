import tkinter as tk
import json
from urllib.request import urlopen
from PIL import ImageTk
class Card:
    def __init__(self, id):
        #super().__init__()
        #print(id)
        file = open('supfile.json')
        data = json.load(file)
        #print(len(data))
        info = data[id]
        root = tk.Toplevel()
        pic = tk.Frame(root)
        pic.pack()
        image_url = info["images"]["sm"]
        u = urlopen(image_url)
        raw = u.read()
        u.close()
        photo = ImageTk.PhotoImage(data=raw)
        label = tk.Label(pic,image=photo)
        label.image = photo
        label.pack()
        bottomframe = tk.Frame(root)
        bottomframe.pack()
        stats = tk.Text(bottomframe, height=20, width=15)
        for k,v in info["powerstats"].items():
            stats.insert(tk.END, "{}, {}\n".format(k,v))
        stats.pack(side = "left")
        bio = tk.Text(bottomframe, height= 20, width= 40)
        for i,j in info["biography"].items():
            bio.insert(tk.END, "{}, {}\n".format(str(i),str(j)))
        bio.pack(side = "right")
        tk.mainloop()
#card = Card(233)
